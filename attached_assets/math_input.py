import streamlit as st
import sympy as sp
from typing import Tuple
from assets.translations import get_text

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
    
    # Display the rendered LaTeX for preview
    if input_value and input_value.strip():
        try:
            # Clean up common notations for display
            display_expr = input_value.replace("^", "**")
            display_expr = display_expr.replace("*", " \\cdot ")
            display_expr = display_expr.replace("**", "^")
            
            # Try to parse and display with SymPy
            expr = sp.sympify(input_value.replace("^", "**"))
            
            with st.expander(get_text("preview"), expanded=False):
                st.latex(sp.latex(expr))
                
        except Exception as e:
            # Show input as-is if parsing fails
            with st.expander(get_text("preview"), expanded=False):
                st.code(input_value)
                st.warning(f"{get_text('invalid_expression')}: {str(e)}")
    
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
            selected = "ln("
    
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

def validate_math_expression(expression: str, variable: str = "x") -> Tuple[bool, str]:
    """
    Validate a mathematical expression.
    
    Args:
        expression (str): Expression to validate
        variable (str): Variable name
        
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    if not expression or not expression.strip():
        return False, get_text("empty_expression")
    
    try:
        # Replace common notations
        cleaned_expr = expression.replace("^", "**")
        
        # Try to parse with SymPy
        var = sp.Symbol(variable)
        expr = sp.sympify(cleaned_expr, locals={variable: var})
        
        # Check if expression contains the expected variable or is a constant
        free_symbols = expr.free_symbols
        if free_symbols and var not in free_symbols:
            return False, f"{get_text('variable_not_found')}: {variable}"
        
        return True, ""
        
    except Exception as e:
        return False, f"{get_text('invalid_syntax')}: {str(e)}"

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
        st.code(f"e^(-{variable}^2)")
        
        st.markdown(f"**{get_text('logarithmic_functions')}:**")
        st.code(f"ln({variable})")
        st.code(f"log({variable}, 10)")
        
        st.markdown(f"**{get_text('other_functions')}:**")
        st.code(f"sqrt({variable})")
        st.code(f"abs({variable})")
        st.code(f"1/{variable}")
