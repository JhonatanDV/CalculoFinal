import streamlit as st
import sympy as sp
import numpy as np
from utils.area_calculator import calculate_area_between_curves, find_intersection_points
from utils.plotting import plot_area_between_curves
from components.math_input import create_math_input, create_function_examples
from components.solution_display import display_area_between_curves_solution, display_error_message, create_solution_summary
from assets.examples import area_between_curves_examples
from assets.translations import get_text

def show():
    st.title("📏 " + get_text("area_between_curves_calculator"))
    
    # Initialize page-specific session state for functions
    if "input_value_function1" not in st.session_state:
        st.session_state["input_value_function1"] = "x^2"
    if "input_value_function2" not in st.session_state:
        st.session_state["input_value_function2"] = "x"
    if "abc_lower" not in st.session_state:
        st.session_state.abc_lower = "0"
    if "abc_upper" not in st.session_state:
        st.session_state.abc_upper = "1"
    
    st.markdown(get_text("area_between_curves_description"))
    
    # Main input section
    st.header(get_text("functions_and_interval"))
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Function inputs
        function1_input = create_math_input(
            get_text("first_function_f1"), 
            st.session_state.get("input_value_function1", "x^2"), 
            key="function1",
            help_text=get_text("function_input_help")
        )
        function2_input = create_math_input(
            get_text("second_function_f2"), 
            st.session_state.get("input_value_function2", "x"), 
            key="function2",
            help_text=get_text("function_input_help")
        )
        
        # Save functions to session state
        st.session_state["input_value_function1"] = function1_input
        st.session_state["input_value_function2"] = function2_input
        
        # Bounds input
        col1a, col1b = st.columns(2)
        with col1a:
            lower_bound = st.text_input(
                get_text("lower_bound_a"), 
                st.session_state.abc_lower, 
                key="abc_lower_input"
            )
            st.session_state.abc_lower = lower_bound
        with col1b:
            upper_bound = st.text_input(
                get_text("upper_bound_b"), 
                st.session_state.abc_upper, 
                key="abc_upper_input"
            )
            st.session_state.abc_upper = upper_bound
        
        # Options
        find_intersections = st.checkbox(
            get_text("find_intersections_automatically"), 
            value=True,
            help=get_text("intersection_help")
        )
    
    with col2:
        st.markdown("### " + get_text("example_problems"))
        selected_example = st.selectbox(
            get_text("select_example"),
            list(area_between_curves_examples.keys()),
            key="abc_example"
        )
        
        if st.button(get_text("load_example"), key="load_abc_example"):
            example = area_between_curves_examples[selected_example]
            st.session_state["input_value_function1"] = example["function1"]
            st.session_state["input_value_function2"] = example["function2"]
            st.session_state.abc_lower = str(example["lower_bound"])
            st.session_state.abc_upper = str(example["upper_bound"])
            st.rerun()
        
        # Show function examples
        create_function_examples("x")
    
    # Find intersections if requested
    if find_intersections:
        col_int1, col_int2, col_int3 = st.columns([1, 2, 1])
        with col_int2:
            find_button = st.button(
                f"🔍 {get_text('find_intersection_points')}", 
                key="find_intersections",
                use_container_width=True
            )
        
        if find_button:
            try:
                if not function1_input.strip() or not function2_input.strip():
                    st.warning(get_text("enter_both_functions"))
                    return
                
                with st.spinner(get_text("finding_intersections")):
                    intersections = find_intersection_points(function1_input, function2_input, "x")
                
                if intersections:
                    st.success(f"{get_text('found_intersections')}: {len(intersections)}")
                    
                    intersection_text = ", ".join([f"x = {x:.6f}" for x in intersections])
                    st.markdown(f"**{get_text('intersection_points')}:** {intersection_text}")
                    
                    # Suggest bounds
                    if len(intersections) >= 2:
                        st.markdown(f"**{get_text('suggested_bounds')}:**")
                        for i in range(len(intersections) - 1):
                            st.markdown(f"• {get_text('from')} x = {intersections[i]:.6f} {get_text('to')} x = {intersections[i+1]:.6f}")
                        
                        # Auto-fill bounds with first interval
                        if st.button(get_text("use_first_interval"), key="use_first_interval"):
                            st.session_state.abc_lower = str(round(intersections[0], 6))
                            st.session_state.abc_upper = str(round(intersections[1], 6))
                            st.rerun()
                else:
                    st.warning(get_text("no_intersections_found"))
            
            except Exception as e:
                display_error_message("intersection_error", str(e))
    
    # Calculate button
    st.markdown("---")
    
    col_calc1, col_calc2, col_calc3 = st.columns([1, 2, 1])
    with col_calc2:
        calculate_button = st.button(
            f"🧮 {get_text('calculate_area')}", 
            key="calculate_area",
            use_container_width=True,
            type="primary"
        )
    
    if calculate_button:
        try:
            # Validate inputs
            if not function1_input.strip() or not function2_input.strip():
                st.error(get_text("enter_both_functions"))
                return
            
            if not lower_bound.strip() or not upper_bound.strip():
                st.error(get_text("empty_bounds"))
                return
            
            # Parse inputs
            func1_str = function1_input
            func2_str = function2_input
            a = float(lower_bound)
            b = float(upper_bound)
            
            if a >= b:
                st.error(get_text("invalid_interval"))
                return
            
            # Calculate area
            with st.spinner(get_text("calculating")):
                area, steps = calculate_area_between_curves(func1_str, func2_str, a, b, "x")
            
            # Create summary
            inputs = {
                "function1": func1_str,
                "function2": func2_str,
                "lower_bound": str(a),
                "upper_bound": str(b)
            }
            create_solution_summary("area_between_curves", inputs, area)
            
            # Display the plot
            st.markdown("### " + get_text("visualization"))
            plot_area_between_curves(func1_str, func2_str, a, b, "x")
            
            # Display the solution
            display_area_between_curves_solution(func1_str, func2_str, a, b, area, steps)
            
        except ValueError as e:
            display_error_message("calculation_error", str(e))
        except Exception as e:
            display_error_message("unexpected_error", str(e))
    
    # Additional tools
    st.markdown("---")
    st.subheader(get_text("additional_tools"))
    
    col_tool1, col_tool2 = st.columns(2)
    
    with col_tool1:
        if st.button(get_text("swap_functions"), key="swap_functions"):
            # Swap the functions
            temp = st.session_state["input_value_function1"]
            st.session_state["input_value_function1"] = st.session_state["input_value_function2"]
            st.session_state["input_value_function2"] = temp
            st.rerun()
    
    with col_tool2:
        if st.button(get_text("clear_functions"), key="clear_functions"):
            st.session_state["input_value_function1"] = ""
            st.session_state["input_value_function2"] = ""
            st.session_state.abc_lower = "0"
            st.session_state.abc_upper = "1"
            st.rerun()
    
    # Theory section
    with st.expander(get_text("learn_about_area_between_curves"), expanded=False):
        st.markdown("### " + get_text("area_between_curves_calculation"))
        
        st.markdown(get_text("area_between_curves_theory"))
        
        st.latex(r"\text{Area} = \int_{a}^{b} |f(x) - g(x)| \, dx")
        
        st.markdown(get_text("practice_determination"))
        
        st.latex(r"\text{Area} = \int_{a}^{b} [f(x) - g(x)] \, dx")
        
        st.markdown("### " + get_text("when_curves_intersect"))
        
        st.markdown(get_text("intersection_procedure"))
        
        st.markdown("### " + get_text("important_considerations"))
        
        considerations = [
            get_text("area_always_positive"),
            get_text("y_axis_integration"),
            get_text("complex_regions_advice")
        ]
        
        for consideration in considerations:
            st.markdown(f"- {consideration}")
        
        st.markdown("### " + get_text("practical_applications"))
        
        applications = [
            get_text("physics_applications"),
            get_text("economics_applications"),
            get_text("engineering_applications_detailed"),
            get_text("geometry_applications")
        ]
        
        for app in applications:
            st.markdown(f"- {app}")
