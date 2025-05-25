import streamlit as st
import sympy as sp
from typing import Tuple
from assets.translations import get_text
from utils.expression_parser import safe_sympify
from utils.validation import validate_function_input

def create_math_input(label: str, default: str = "", key: str = None, 
                     help_text: str = None) -> str:
    """
    Create a math input field with LaTeX preview and validation.
    
    Args:
        label (str): Label for the input field
        default (str): Default value for the input field
        key (str): Unique key for the input field
        help_text (str): Help text to display
    
    Returns:
        str: The input value
    """
    # Set up session state for the input value
    input_key = f"input_value_{key}" if key else "input_value_default"
    if input_key not in st.session_state:
        st.session_state[input_key] = default
    
    # Create a unique text input key
    text_input_key = f"textinput_{key}" if key else "textinput_default"
    
    # Text input field with help
    if help_text:
        input_value = st.text_input(
            label, 
            value=st.session_state[input_key], 
            key=text_input_key,
            help=help_text
        )
    else:
        input_value = st.text_input(
            label, 
            value=st.session_state[input_key], 
            key=text_input_key,
            help=get_text("math_input_help")
        )
    
    # Update session state after user input
    st.session_state[input_key] = input_value
    
    # Display the rendered LaTeX for preview and validation
    if input_value and input_value.strip():
        try:
            # CORRECCIÓN: No evaluar la función, solo validar sintaxis
            # Usar sympy para parsear sin evaluar numéricamente
            expr = sp.sympify(input_value.replace('^', '**'))
            
            with st.expander(get_text("preview"), expanded=False):
                # Mostrar la función tal como está, no evaluada
                st.latex(sp.latex(expr))
                st.success("✅ " + get_text("valid_expression"))
                
        except Exception as e:
            with st.expander(get_text("preview"), expanded=False):
                st.code(input_value)
                st.error(f"❌ Error de sintaxis: {str(e)}")
                
                # Provide helpful suggestions
                st.markdown("**" + get_text("suggestions") + ":**")
                st.markdown(f"- {get_text('check_syntax')}")
                st.markdown(f"- {get_text('use_star_multiplication')}")
                st.markdown(f"- {get_text('check_parentheses')}")
                st.markdown(f"- {get_text('use_valid_functions')}")
    
    return input_value

def create_math_keyboard(prefix: str = "") -> str:
    """
    Create a visual math keyboard for easier input.
    
    Args:
        prefix (str): Prefix for unique keys
        
    Returns:
        str: Selected symbol or function
    """
    st.markdown(f"### {get_text('math_keyboard')}")
    
    # Basic operations
    col1, col2, col3, col4 = st.columns(4)
    
    selected = ""
    
    with col1:
        st.markdown("**" + get_text("basic_operations") + "**")
        if st.button("+", key=f"{prefix}_plus"):
            selected = "+"
        if st.button("−", key=f"{prefix}_minus"):
            selected = "-"
        if st.button("×", key=f"{prefix}_times"):
            selected = "*"
        if st.button("÷", key=f"{prefix}_divide"):
            selected = "/"
    
    with col2:
        st.markdown("**" + get_text("powers_roots") + "**")
        if st.button("x²", key=f"{prefix}_square"):
            selected = "^2"
        if st.button("x³", key=f"{prefix}_cube"):
            selected = "^3"
        if st.button("xⁿ", key=f"{prefix}_power"):
            selected = "^"
        if st.button("√x", key=f"{prefix}_sqrt"):
            selected = "sqrt("
    
    with col3:
        st.markdown("**" + get_text("trigonometric") + "**")
        if st.button("sin", key=f"{prefix}_sin"):
            selected = "sin("
        if st.button("cos", key=f"{prefix}_cos"):
            selected = "cos("
        if st.button("tan", key=f"{prefix}_tan"):
            selected = "tan("
        if st.button("ln", key=f"{prefix}_ln"):
            selected = "log("
    
    with col4:
        st.markdown("**" + get_text("constants") + "**")
        if st.button("π", key=f"{prefix}_pi"):
            selected = "pi"
        if st.button("e", key=f"{prefix}_e"):
            selected = "e"
        if st.button("(", key=f"{prefix}_lparen"):
            selected = "("
        if st.button(")", key=f"{prefix}_rparen"):
            selected = ")"
    
    return selected

def create_function_examples(variable: str = "x") -> None:
    """
    Display common function examples for reference.
    
    Args:
        variable (str): Variable name to use in examples
    """
    with st.expander(get_text("function_examples"), expanded=False):
        st.markdown(f"**{get_text('polynomial_functions')}:**")
        st.code(f"{variable}^2 + 3*{variable} + 1")
        st.code(f"2*{variable}^3 - 5*{variable}^2 + 7")
        
        st.markdown(f"**{get_text('trigonometric_functions')}:**")
        st.code(f"sin({variable})")
        st.code(f"cos(2*{variable}) + sin({variable})")
        
        st.markdown(f"**{get_text('exponential_functions')}:**")
        st.code(f"exp({variable})")
        st.code(f"2^{variable}")
        st.code(f"exp(-{variable}^2)")
        
        st.markdown(f"**{get_text('logarithmic_functions')}:**")
        st.code(f"log({variable})")
        st.code(f"log({variable}, 10)")
        
        st.markdown(f"**{get_text('other_functions')}:**")
        st.code(f"sqrt({variable})")
        st.code(f"abs({variable})")
        st.code(f"1/{variable}")

def create_bounds_input(label_lower: str, label_upper: str, 
                       default_lower: str = "0", default_upper: str = "1",
                       key_prefix: str = "") -> Tuple[str, str]:
    """
    Create paired input fields for integration bounds with validation.
    
    Args:
        label_lower (str): Label for lower bound
        label_upper (str): Label for upper bound
        default_lower (str): Default lower bound
        default_upper (str): Default upper bound
        key_prefix (str): Prefix for unique keys
    
    Returns:
        Tuple[str, str]: (lower_bound, upper_bound)
    """
    col1, col2 = st.columns(2)
    
    with col1:
        lower_bound = st.text_input(
            label_lower,
            value=default_lower,
            key=f"{key_prefix}_lower",
            help=get_text("bound_help")
        )
    
    with col2:
        upper_bound = st.text_input(
            label_upper,
            value=default_upper,
            key=f"{key_prefix}_upper",
            help=get_text("bound_help")
        )
    
    # Validate bounds
    if lower_bound.strip() and upper_bound.strip():
        try:
            from utils.validation import validate_bounds
            valid, error, lower_val, upper_val = validate_bounds(lower_bound, upper_bound)
            
            if not valid:
                st.error(f"❌ {error}")
            else:
                st.success(f"✅ {get_text('valid_interval')}: [{lower_val}, {upper_val}]")
        except:
            pass
    
    return lower_bound, upper_bound

def create_variable_input(label: str, default: str = "x", key: str = "") -> str:
    """
    Create input for mathematical variable with validation.
    
    Args:
        label (str): Label for the input
        default (str): Default variable name
        key (str): Unique key
    
    Returns:
        str: Variable name
    """
    variable = st.text_input(
        label,
        value=default,
        key=f"var_{key}",
        help=get_text("variable_help")
    )
    
    # Validate variable name
    if variable.strip():
        if variable.isalpha() and len(variable) == 1:
            st.success(f"✅ {get_text('valid_variable')}: {variable}")
        else:
            st.warning(f"⚠️ {get_text('variable_warning')}")
    
    return variable

def create_subdivisions_input(label: str, default: int = 10, 
                            min_val: int = 1, max_val: int = 1000,
                            key: str = "") -> int:
    """
    Create input for number of subdivisions with validation.
    
    Args:
        label (str): Label for the input
        default (int): Default number of subdivisions
        min_val (int): Minimum value
        max_val (int): Maximum value
        key (str): Unique key
    
    Returns:
        int: Number of subdivisions
    """
    n = st.number_input(
        label,
        min_value=min_val,
        max_value=max_val,
        value=default,
        step=1,
        key=f"subdivisions_{key}",
        help=get_text("subdivisions_help")
    )
    
    # Provide guidance on subdivision count
    if n <= 10:
        st.info(f"ℹ️ {get_text('low_subdivisions_warning')}")
    elif n >= 500:
        st.warning(f"⚠️ {get_text('high_subdivisions_warning')}")
    else:
        st.success(f"✅ {get_text('good_subdivisions')}: {n}")
    
    return n