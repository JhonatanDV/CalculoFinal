import streamlit as st
import sympy as sp
import numpy as np
from utils.area_between_curves import calculate_area_between_curves, find_intersection_points, get_area_steps_with_intersections
from utils.plotting import plot_area_between_curves
from components.math_input import create_math_input, create_function_examples
from components.solution_display import display_area_between_curves_solution, display_error_message, create_solution_summary
from assets.simple_examples import area_between_curves_examples
from assets.translations import get_text

def show():
    st.title("📏 " + get_text("area_between_curves_calculator"))
    
    # Initialize page-specific session state
    if "input_value_area_function1" not in st.session_state:
        st.session_state["input_value_area_function1"] = "x^2"
    if "input_value_area_function2" not in st.session_state:
        st.session_state["input_value_area_function2"] = "x"
    if "area_lower" not in st.session_state:
        st.session_state.area_lower = "0"
    if "area_upper" not in st.session_state:
        st.session_state.area_upper = "1"
    
    st.markdown(get_text("area_between_curves_description"))
    
    # Main input section
    st.header(get_text("functions_and_interval"))
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Function inputs
        function1_input = create_math_input(
            get_text("first_function_f1"), 
            st.session_state.get("input_value_area_function1", "x^2"), 
            key="area_function1",
            help_text=get_text("function_input_help")
        )
        st.session_state["input_value_area_function1"] = function1_input
        
        function2_input = create_math_input(
            get_text("second_function_f2"), 
            st.session_state.get("input_value_area_function2", "x"), 
            key="area_function2",
            help_text=get_text("function_input_help")
        )
        st.session_state["input_value_area_function2"] = function2_input
        
        # Bounds input
        col1a, col1b = st.columns(2)
        with col1a:
            lower_bound = st.text_input(
                get_text("lower_limit"), 
                st.session_state.get("area_lower", "0"), 
                key="area_lower_input"
            )
            st.session_state.area_lower = lower_bound
        with col1b:
            upper_bound = st.text_input(
                get_text("upper_limit"), 
                st.session_state.get("area_upper", "1"), 
                key="area_upper_input"
            )
            st.session_state.area_upper = upper_bound
        
        # Variable input
        variable = st.text_input(
            get_text("variable"), 
            "x", 
            key="area_variable",
            help=get_text("variable_help")
        )
    
    with col2:
        st.markdown("### " + get_text("example_problems"))
        selected_example = st.selectbox(
            get_text("select_example"),
            list(area_between_curves_examples.keys()),
            key="area_example"
        )
        
        if st.button(get_text("load_example"), key="load_area_example"):
            example = area_between_curves_examples[selected_example]
            # Update session state values
            st.session_state["input_value_area_function1"] = example["function1"]
            st.session_state["input_value_area_function2"] = example["function2"]
            st.session_state.area_lower = str(example["lower_bound"])
            st.session_state.area_upper = str(example["upper_bound"])
            st.rerun()
        
        # Show function examples
        create_function_examples(variable)
    
    # Intersection finder tool
    st.markdown("---")
    st.subheader(get_text("intersection_analysis"))
    
    col_int1, col_int2 = st.columns(2)
    
    with col_int1:
        if st.button(get_text("find_intersections_automatically"), key="find_intersections"):
            if function1_input.strip() and function2_input.strip():
                with st.spinner(get_text("finding_intersections")):
                    try:
                        intersections = find_intersection_points(function1_input, function2_input, variable)
                        
                        if intersections:
                            st.success(f"{get_text('found_intersections')}: {len(intersections)}")
                            
                            # Display intersection points
                            st.markdown(f"**{get_text('intersection_points')}:**")
                            for i, point in enumerate(intersections):
                                st.write(f"{i+1}. {variable} = {point:.6f}")
                            
                            # Suggest bounds based on intersections
                            if len(intersections) >= 2:
                                st.markdown(f"**{get_text('suggested_bounds')}:**")
                                for i in range(len(intersections) - 1):
                                    lower_suggest = intersections[i]
                                    upper_suggest = intersections[i + 1]
                                    st.write(f"{get_text('from')} {lower_suggest:.6f} {get_text('to')} {upper_suggest:.6f}")
                                    
                                    if st.button(f"{get_text('use_first_interval')}", 
                                               key=f"use_interval_{i}"):
                                        st.session_state.area_lower = str(lower_suggest)
                                        st.session_state.area_upper = str(upper_suggest)
                                        st.rerun()
                        else:
                            st.warning(get_text("no_intersections_found"))
                            
                    except Exception as e:
                        st.error(f"{get_text('error')}: {str(e)}")
            else:
                st.warning(get_text("enter_both_functions"))
    
    # Calculate button
    st.markdown("---")
    
    col_calc1, col_calc2, col_calc3 = st.columns([1, 2, 1])
    with col_calc2:
        calculate_button = st.button(
            f"🧮 {get_text('calculate_area_between_curves')}", 
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
            a = lower_bound
            b = upper_bound
            var = variable if variable else "x"
            
            # Calculate area
            with st.spinner(get_text("calculating")):
                area, steps = calculate_area_between_curves(func1_str, func2_str, a, b, var)
            
            # Create summary
            inputs = {
                "function1": func1_str,
                "function2": func2_str,
                "lower_bound": a,
                "upper_bound": b,
                "variable": var
            }
            create_solution_summary("area_between_curves", inputs, area)
            
            # Display the plot
            st.markdown("### " + get_text("visualization"))
            plot_area_between_curves(func1_str, func2_str, a, b, var)
            
            # Display the solution
            display_area_between_curves_solution(func1_str, func2_str, float(a), float(b), area, steps, True, var)
            
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
            temp = st.session_state.get("input_value_area_function1", "")
            st.session_state["input_value_area_function1"] = st.session_state.get("input_value_area_function2", "")
            st.session_state["input_value_area_function2"] = temp
            st.rerun()
    
    with col_tool2:
        if st.button(get_text("clear_functions"), key="clear_functions"):
            # Clear both functions
            st.session_state["input_value_area_function1"] = ""
            st.session_state["input_value_area_function2"] = ""
            st.rerun()
    
    # Theory section
    with st.expander(get_text("learn_about_area_between_curves"), expanded=False):
        st.markdown("### " + get_text("what_is_area_between_curves"))
        
        st.markdown(get_text("area_between_curves_explanation"))
        
        st.latex(r"\text{Area} = \int_{a}^{b} |f(x) - g(x)| \, dx")
        
        st.markdown("### " + get_text("when_functions_intersect"))
        
        st.markdown(get_text("intersection_handling_explanation"))
        
        st.latex(r"\text{Area} = \int_{a}^{c} |f(x) - g(x)| \, dx + \int_{c}^{b} |f(x) - g(x)| \, dx")
        
        st.markdown("### " + get_text("applications"))
        
        applications = [
            get_text("physics_applications"),
            get_text("economics_applications"), 
            get_text("engineering_applications"),
            get_text("probability_applications"),
            get_text("optimization_applications")
        ]
        
        for app in applications:
            st.markdown(f"- {app}")
        
        st.markdown("### " + get_text("tips_for_success"))
        
        tips = [
            get_text("identify_intersection_points"),
            get_text("determine_which_function_top"),
            get_text("split_intervals_if_needed"),
            get_text("always_positive_area"),
            get_text("check_work_with_graph")
        ]
        
        for tip in tips:
            st.markdown(f"- {tip}")
