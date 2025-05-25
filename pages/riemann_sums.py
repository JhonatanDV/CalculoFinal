import streamlit as st
import sympy as sp
import numpy as np
from utils.riemann_sum import calculate_riemann_sum, get_riemann_sum_steps, compare_riemann_methods
from utils.plotting import plot_riemann_sum
from components.math_input import create_math_input, create_function_examples
from components.solution_display import display_riemann_sum_solution, display_error_message, create_solution_summary
from assets.simple_examples import riemann_sum_examples
from assets.translations import get_text

def show():
    st.title("📊 " + get_text("riemann_sums_calculator"))
    
    # Initialize page-specific session state
    if "input_value_riemann_function" not in st.session_state:
        st.session_state["input_value_riemann_function"] = "x^2"
    if "riemann_lower" not in st.session_state:
        st.session_state.riemann_lower = "0"
    if "riemann_upper" not in st.session_state:
        st.session_state.riemann_upper = "1"
    if "riemann_n" not in st.session_state:
        st.session_state.riemann_n = 10
    
    st.markdown(get_text("riemann_sums_description"))
    
    # Main input section
    st.header(get_text("function_and_interval"))
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Function input
        function_input = create_math_input(
            get_text("function_fx"), 
            st.session_state.get("input_value_riemann_function", "x^2"), 
            key="riemann_function",
            help_text=get_text("function_input_help")
        )
        
        # Save the function input to session state
        st.session_state["input_value_riemann_function"] = function_input
        
        # Bounds input
        col1a, col1b = st.columns(2)
        with col1a:
            lower_bound = st.text_input(
                get_text("lower_limit_a"), 
                st.session_state.get("riemann_lower", "0"), 
                key="riemann_lower_input"
            )
            st.session_state.riemann_lower = lower_bound
        with col1b:
            upper_bound = st.text_input(
                get_text("upper_limit_b"), 
                st.session_state.get("riemann_upper", "1"), 
                key="riemann_upper_input"
            )
            st.session_state.riemann_upper = upper_bound
        
        # Number of subdivisions and method
        col1c, col1d = st.columns(2)
        with col1c:
            n_subdivisions = st.number_input(
                get_text("number_subdivisions_n"), 
                min_value=1, 
                max_value=1000, 
                value=st.session_state.get("riemann_n", 10), 
                key="riemann_n_input"
            )
            st.session_state.riemann_n = n_subdivisions
        
        with col1d:
            method = st.selectbox(
                get_text("sampling_method"),
                ["left", "right", "midpoint"],
                index=0,
                format_func=lambda x: get_text(f"method_{x}"),
                key="riemann_method_input"
            )
    
    with col2:
        st.markdown("### " + get_text("example_problems"))
        selected_example = st.selectbox(
            get_text("select_example"),
            list(riemann_sum_examples.keys()),
            key="riemann_example"
        )
        
        if st.button(get_text("load_example"), key="load_riemann_example"):
            example = riemann_sum_examples[selected_example]
            # Update session state values
            st.session_state["input_value_riemann_function"] = example["function"]
            st.session_state.riemann_lower = str(example["lower_bound"])
            st.session_state.riemann_upper = str(example["upper_bound"])
            st.session_state.riemann_n = example["subdivisions"]
            st.rerun()
        
        # Show function examples
        create_function_examples("x")
    
    # Calculate button
    st.markdown("---")
    
    col_calc1, col_calc2, col_calc3 = st.columns([1, 2, 1])
    with col_calc2:
        calculate_button = st.button(
            f"🧮 {get_text('calculate_riemann_sum')}", 
            key="calculate_riemann",
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
            a = float(lower_bound)
            b = float(upper_bound)
            n = int(n_subdivisions)
            
            if a >= b:
                st.error(get_text("invalid_interval"))
                return
            
            if n <= 0:
                st.error(get_text("invalid_subdivisions"))
                return
            
            # Calculate Riemann sum
            with st.spinner(get_text("calculating")):
                riemann_sum, rectangle_areas = calculate_riemann_sum(func_str, a, b, n, method, "x")
                steps = get_riemann_sum_steps(func_str, a, b, n, method, "x")
            
            # Create summary
            inputs = {
                "function": func_str,
                "lower_bound": str(a),
                "upper_bound": str(b),
                "subdivisions": str(n),
                "method": get_text(f"method_{method}")
            }
            create_solution_summary("riemann_sum", inputs, riemann_sum)
            
            # Display the plot
            st.markdown("### " + get_text("visualization"))
            plot_riemann_sum(func_str, a, b, n, method, "x")
            
            # Display the solution
            display_riemann_sum_solution(func_str, a, b, n, method, riemann_sum, steps, diagram_provided=True, variable="x")
            
        except ValueError as e:
            display_error_message("calculation_error", str(e))
        except Exception as e:
            display_error_message("unexpected_error", str(e))
    
    # Method comparison
    st.markdown("---")
    st.subheader(get_text("method_comparison"))
    
    if st.button(get_text("compare_methods"), key="compare_riemann_methods"):
        try:
            if not function_input.strip() or not lower_bound.strip() or not upper_bound.strip():
                st.warning(get_text("fill_all_fields"))
                return
            
            func_str = function_input
            a = float(lower_bound)
            b = float(upper_bound)
            n = int(n_subdivisions)
            
            with st.spinner(get_text("comparing_methods")):
                comparison = compare_riemann_methods(func_str, a, b, n, "x")
            
            if "error" in comparison:
                st.error(f"{get_text('comparison_error')}: {comparison['error']}")
                return
            
            # Display comparison results
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    label=get_text("method_left"),
                    value=f"{comparison['left']:.6f}"
                )
                if "left_error" in comparison:
                    st.caption(f"{get_text('error')}: {comparison['left_error']:.6f}")
            
            with col2:
                st.metric(
                    label=get_text("method_right"),
                    value=f"{comparison['right']:.6f}"
                )
                if "right_error" in comparison:
                    st.caption(f"{get_text('error')}: {comparison['right_error']:.6f}")
            
            with col3:
                st.metric(
                    label=get_text("method_midpoint"),
                    value=f"{comparison['midpoint']:.6f}"
                )
                if "midpoint_error" in comparison:
                    st.caption(f"{get_text('error')}: {comparison['midpoint_error']:.6f}")
            
            if "exact" in comparison and comparison["exact"] is not None:
                st.info(f"{get_text('exact_value')}: {comparison['exact']:.6f}")
                
                # Show which method is most accurate
                errors = {
                    get_text("method_left"): comparison.get('left_error', float('inf')),
                    get_text("method_right"): comparison.get('right_error', float('inf')),
                    get_text("method_midpoint"): comparison.get('midpoint_error', float('inf'))
                }
                
                best_method = min(errors, key=errors.get)
                st.success(f"{get_text('most_accurate_method')}: {best_method}")
                
        except Exception as e:
            display_error_message("comparison_error", str(e))
    
    # Theory section
    with st.expander(get_text("learn_about_riemann_sums"), expanded=False):
        st.markdown("### " + get_text("what_is_riemann_sum"))
        
        st.markdown(get_text("riemann_sum_explanation"))
        
        st.markdown("### " + get_text("types_riemann_sums"))
        
        st.markdown(f"1. **{get_text('method_left')}**: {get_text('left_method_explanation')}")
        st.markdown(f"2. **{get_text('method_right')}**: {get_text('right_method_explanation')}")
        st.markdown(f"3. **{get_text('method_midpoint')}**: {get_text('midpoint_method_explanation')}")
        
        st.markdown("### " + get_text("the_formula"))
        
        st.markdown(get_text("riemann_formula_explanation"))
        
        st.latex(r"R_n = \Delta x \sum_{i=1}^{n} f(x_i^*)")
        
        st.markdown(get_text("where_explanation"))
        
        st.markdown("### " + get_text("connection_definite_integrals"))
        
        st.markdown(get_text("convergence_explanation"))
        
        st.latex(r"\lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x = \int_{a}^{b} f(x) \, dx")
        
        st.markdown(get_text("fundamental_connection"))
