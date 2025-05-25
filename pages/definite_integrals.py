import streamlit as st
import sympy as sp
import numpy as np
from utils.calculator import solve_integral
from utils.plotting import plot_integral
from components.math_input import create_math_input, create_function_examples
from components.solution_display import display_solution, display_error_message, create_solution_summary
from assets.simple_examples import definite_integral_examples
from assets.study_plans import definite_integrals_study_plan, additional_integral_examples
from assets.enhanced_study_plans import enhanced_definite_integrals_plan
from assets.translations import get_text

def show():
    st.title("📐 " + get_text("definite_integrals_calculator"))
    
    # Initialize page-specific session state
    if "input_value_integral_function" not in st.session_state:
        st.session_state["input_value_integral_function"] = st.session_state.function_str
    
    # Add tabs for calculator and study plan
    tab1, tab2, tab3 = st.tabs([
        "🧮 Calculadora", 
        "📋 Ejemplos",
        "📚 Plan de Estudios"
    ])
    
    with tab1:
        show_calculator_tab()
    
    with tab2:
        show_examples_tab()
    
    with tab3:
        show_study_plan_tab()

def show_calculator_tab():
    """Display the main calculator interface."""
    st.markdown(get_text("definite_integrals_description"))
    
    # Main input section
    st.header(get_text("function_and_interval"))
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Function input
        function_input = create_math_input(
            get_text("function_fx"), 
            st.session_state.function_str, 
            key="integral_function",
            help_text=get_text("function_input_help")
        )
        
        # Save the function input to session state
        st.session_state.function_str = function_input
        
        # Bounds input
        col1a, col1b = st.columns(2)
        with col1a:
            lower_bound = st.text_input(
                get_text("lower_bound_a"), 
                st.session_state.lower_bound, 
                key="integral_lower",
                help=get_text("bound_help")
            )
            st.session_state.lower_bound = lower_bound
        with col1b:
            upper_bound = st.text_input(
                get_text("upper_bound_b"), 
                st.session_state.upper_bound, 
                key="integral_upper",
                help=get_text("bound_help")
            )
            st.session_state.upper_bound = upper_bound
        
        # Variable input
        variable = st.text_input(
            get_text("variable"), 
            st.session_state.variable, 
            key="integral_variable",
            help=get_text("variable_help")
        )
        st.session_state.variable = variable
    
    with col2:
        st.markdown("### " + get_text("example_problems"))
        selected_example = st.selectbox(
            get_text("select_example"),
            list(definite_integral_examples.keys()),
            key="integral_example"
        )
        
        if st.button(get_text("load_example"), key="load_integral_example"):
            example = definite_integral_examples[selected_example]
            # Update the input value first
            st.session_state["input_value_integral_function"] = example["function"]
            # Then update the other session variables
            st.session_state.function_str = example["function"]
            st.session_state.lower_bound = str(example["lower_bound"])
            st.session_state.upper_bound = str(example["upper_bound"])
            st.session_state.variable = example["variable"]
            st.rerun()
        
        # Show function examples
        create_function_examples(variable)
    
    # Calculate button
    st.markdown("---")
    
    col_calc1, col_calc2, col_calc3 = st.columns([1, 2, 1])
    with col_calc2:
        calculate_button = st.button(
            f"🧮 {get_text('calculate_integral')}", 
            key="calculate_integral",
            use_container_width=True,
            type="primary"
        )
    
    if calculate_button:
        try:
            # Validate inputs
            if not function_input.strip():
                st.error(get_text("empty_function"))
                return
            
            if not lower_bound.strip() or not upper_bound.strip():
                st.error(get_text("empty_bounds"))
                return
            
            # Parse inputs
            func_str = function_input
            a = lower_bound
            b = upper_bound
            var = variable if variable else "x"
            
            # Calculate integral
            with st.spinner(get_text("calculating")):
                result, steps = solve_integral(func_str, a, b, var)
            
            # Create summary
            inputs = {
                "function": func_str,
                "lower_bound": a,
                "upper_bound": b,
                "variable": var
            }
            create_solution_summary("definite_integral", inputs, result)
            
            # Display the plot
            st.markdown("### " + get_text("visualization"))
            plot_integral(func_str, a, b, var)
            
            # Display the solution
            display_solution(func_str, a, b, result, steps, var)
            
        except ValueError as e:
            display_error_message("calculation_error", str(e))
        except Exception as e:
            display_error_message("unexpected_error", str(e))
    
    # Theory section
    with st.expander(get_text("learn_about_definite_integrals"), expanded=False):
        st.markdown("### " + get_text("what_is_definite_integral"))
        
        st.markdown(get_text("definite_integral_explanation"))
        
        st.latex(r"\int_{a}^{b} f(x) \, dx")
        
        st.markdown("### " + get_text("fundamental_theorem"))
        
        st.markdown(get_text("fundamental_theorem_explanation"))
        
        st.latex(r"\int_{a}^{b} f(x) \, dx = F(b) - F(a)")
        
        st.markdown(get_text("where_f_is_antiderivative"))
        
        st.markdown("### " + get_text("properties_definite_integrals"))
        
        properties = [
            r"\int_{a}^{b} [f(x) \pm g(x)] \, dx = \int_{a}^{b} f(x) \, dx \pm \int_{a}^{b} g(x) \, dx",
            r"\int_{a}^{b} c \cdot f(x) \, dx = c \cdot \int_{a}^{b} f(x) \, dx",
            r"\int_{a}^{b} f(x) \, dx = -\int_{b}^{a} f(x) \, dx",
            r"\int_{a}^{b} f(x) \, dx = \int_{a}^{c} f(x) \, dx + \int_{c}^{b} f(x) \, dx"
        ]
        
        for i, prop in enumerate(properties, 1):
            st.markdown(f"**{i}.** ")
            st.latex(prop)
        
        st.markdown("### " + get_text("applications"))
        
        applications = [
            get_text("area_under_curve"),
            get_text("volume_solids"),
            get_text("arc_length"),
            get_text("work_by_force"),
            get_text("probability_distributions"),
            get_text("center_of_mass")
        ]
        
        for app in applications:
            st.markdown(f"- {app}")

def show_examples_tab():
    """Display examples from course materials."""
    st.subheader("📋 Ejemplos de Integrales Definidas")
    
    # Original examples section
    st.subheader(get_text("example_problems"))
    
    # Display examples
    col1, col2 = st.columns(2)
    
    with col1:
        example_names = list(definite_integral_examples.keys())
        selected_example = st.selectbox(
            get_text("select_example"),
            example_names,
            key="example_selector"
        )
    
    with col2:
        if st.button(get_text("load_example"), key="load_example_btn"):
            example = definite_integral_examples[selected_example]
            # Store in session state with proper keys
            st.session_state["input_value_integral_function"] = example["function"]
            st.session_state.function_str = example["function"]
            st.session_state.lower_bound = str(example["lower_bound"])
            st.session_state.upper_bound = str(example["upper_bound"])
            st.session_state["integral_lower_bound"] = str(example["lower_bound"])
            st.session_state["integral_upper_bound"] = str(example["upper_bound"])
            st.success("¡Ejemplo cargado! Ve a la pestaña 'Calculadora'.")
            st.balloons()
            st.rerun()
    
    # Display the selected example details
    if selected_example:
        example = definite_integral_examples[selected_example]
        st.info(f"""
        **Función:** `{example['function']}`  
        **Límites:** [{example['lower_bound']}, {example['upper_bound']}]  
        **Variable:** {example['variable']}
        """)

def show_study_plan_tab():
    """Display the enhanced study plan for definite integrals."""
    st.markdown(f"# {enhanced_definite_integrals_plan['title']}")
    st.markdown(enhanced_definite_integrals_plan['description'])
    
    # Display modules with enhanced information
    for i, module in enumerate(enhanced_definite_integrals_plan["modules"]):
        # Color-coded headers based on level
        if module["level"] == "Básico":
            st.markdown(f"## 🟢 {module['title']}")
            st.success(f"**Duración estimada:** {module['duration']}")
        elif module["level"] == "Intermedio":
            st.markdown(f"## 🟡 {module['title']}")
            st.warning(f"**Duración estimada:** {module['duration']}")
        else:
            st.markdown(f"## 🔴 {module['title']}")
            st.error(f"**Duración estimada:** {module['duration']}")
        
        # Topics covered
        st.markdown("### 📋 **Temas que dominarás:**")
        for topic in module["topics"]:
            st.markdown(f"• {topic}")
        
        # Resources section
        st.markdown("### 📚 **Recursos de Estudio Recomendados:**")
        for resource in module["resources"]:
            with st.expander(f"🔗 {resource['title']} ({resource['type'].title()})"):
                st.markdown(f"**Descripción:** {resource['description']}")
                st.markdown(f"**Enlace:** [{resource['title']}]({resource['url']})")
                if st.button(f"Abrir {resource['title']}", key=f"resource_{i}_{resource['title']}", help="Se abrirá en nueva pestaña"):
                    st.markdown(f"🌐 **Dirígete a:** {resource['url']}")
        
        # Examples for this module with difficulty indicators
        st.markdown("### 💡 **Ejemplos Prácticos:**")
        
        for j, example in enumerate(module["examples"]):
            with st.expander(f"Ejemplo {j+1}: {example['function']} {example['difficulty']}"):
                st.markdown(f"**Función:** `{example['function']}`")
                st.markdown(f"**Límites:** [{example['bounds'][0]}, {example['bounds'][1]}]")
                st.markdown(f"**Dificultad:** {example['difficulty']}")
                st.info(example['explanation'])
                
                col1, col2 = st.columns([1, 1])
                with col1:
                    if st.button(f"🎯 Practicar Ahora", key=f"enhanced_study_{i}_{j}"):
                        # Store in session state with proper keys
                        st.session_state["input_value_integral_function"] = example['function']
                        st.session_state.function_str = example['function']
                        st.session_state.lower_bound = str(example['bounds'][0])
                        st.session_state.upper_bound = str(example['bounds'][1])
                        st.session_state["integral_lower_bound"] = str(example['bounds'][0])
                        st.session_state["integral_upper_bound"] = str(example['bounds'][1])
                        st.success("¡Ejemplo cargado! Ve a la pestaña 'Calculadora' para resolverlo.")
                        st.balloons()
                with col2:
                    if st.button(f"📖 Ver Teoría", key=f"theory_{i}_{j}"):
                        st.info("💡 **Tip:** Revisa los recursos de estudio arriba para entender mejor este tipo de integral.")
        
        st.markdown("---")
    
    # Assessment section
    st.markdown("## 📝 **Plan de Evaluación**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🧪 **Evaluaciones**")
        for quiz in enhanced_definite_integrals_plan["assessment"]["quizzes"]:
            st.markdown(f"• {quiz}")
    
    with col2:
        st.markdown("### 🚀 **Proyectos**")
        for project in enhanced_definite_integrals_plan["assessment"]["projects"]:
            st.markdown(f"• {project}")
    
    st.markdown("---")
    st.success("💪 **¡Sigue este plan y dominarás las integrales definidas completamente!**")
