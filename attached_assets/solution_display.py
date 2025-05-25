import streamlit as st
import sympy as sp
from assets.translations import get_text

def display_solution(func_str: str, lower_bound: str, upper_bound: str, 
                    result: float, steps: list, variable: str = "x"):
    """
    Display the solution to an integral calculation with step-by-step workings.
    
    Args:
        func_str (str): String representation of the function
        lower_bound (str): Lower bound of integration
        upper_bound (str): Upper bound of integration
        result (float): Result of the integration
        steps (list): List of solution steps
        variable (str): Integration variable
    """
    st.markdown("## " + get_text("solution"))
    
    # Display the problem statement
    st.markdown(f"### {get_text('evaluating')} $\\int_{{{lower_bound}}}^{{{upper_bound}}} {func_str} \\, d{variable}$")
    
    # Display the result prominently
    st.success(f"### {get_text('result')}: {result:.6f}")
    
    # Display step-by-step solution
    st.markdown("### " + get_text("step_by_step_solution"))
    
    with st.expander(get_text("show_solution_steps"), expanded=True):
        for i, step in enumerate(steps):
            st.markdown(step)
            if i < len(steps) - 1:
                st.markdown("---")
    
    # Additional information
    with st.expander(get_text("additional_info"), expanded=False):
        st.markdown(f"**{get_text('interpretation')}:**")
        st.markdown(f"{get_text('integral_interpretation')}")
        
        if result >= 0:
            st.markdown(f"✅ {get_text('positive_result_meaning')}")
        else:
            st.markdown(f"⚠️ {get_text('negative_result_meaning')}")
    
    # Download button for the solution
    solution_text = f"""
{get_text('integral_calculation')}: ∫[{lower_bound}, {upper_bound}] {func_str} d{variable}

{get_text('result')}: {result:.6f}

{get_text('step_by_step_solution')}:
"""
    for i, step in enumerate(steps):
        # Remove LaTeX formatting for plain text
        clean_step = step.replace("$", "").replace("\\", "")
        solution_text += f"\n{i+1}. {clean_step}"
    
    st.download_button(
        label=get_text("download_solution"),
        data=solution_text,
        file_name=f"integral_solution_{func_str.replace('*', '_').replace('^', '_')}.txt",
        mime="text/plain",
        key="download_integral_solution"
    )

def display_riemann_sum_solution(func_str: str, lower_bound: float, upper_bound: float, 
                                n: int, method: str, result: float, steps: list, 
                                diagram_provided: bool = True, variable: str = "x"):
    """
    Display the solution to a Riemann sum calculation with step-by-step workings.
    """
    st.markdown("## " + get_text("riemann_sum_solution"))
    
    # Display the problem statement
    method_text = get_text(f"method_{method}")
    st.markdown(f"### {get_text('calculating_riemann_sum')} {method_text} {get_text('for')} $f({variable}) = {func_str}$ {get_text('on')} $[{lower_bound}, {upper_bound}]$ {get_text('with')} $n = {n}$")
    
    # Display the result prominently
    st.success(f"### {get_text('result')}: {result:.6f}")
    
    # Display step-by-step solution
    st.markdown("### " + get_text("step_by_step_solution"))
    
    with st.expander(get_text("show_solution_steps"), expanded=True):
        for i, step in enumerate(steps):
            st.markdown(step)
            if i < len(steps) - 1:
                st.markdown("---")
    
    # Explanation of what the Riemann sum represents
    with st.expander(get_text("what_riemann_represents"), expanded=False):
        st.markdown(f"**{get_text('riemann_explanation')}:**")
        
        explanation = f"""
        {get_text('riemann_approximates')} $f({variable}) = {func_str}$ {get_text('from')} ${variable} = {lower_bound}$ {get_text('to')} ${variable} = {upper_bound}$
        {get_text('by_dividing_into')} {n} {get_text('equal_subintervals')}.
        
        {get_text('method_explanation', method=method_text)}
        """
        
        if method == 'left':
            explanation += f"\n- {get_text('left_endpoint_explanation')}"
        elif method == 'right':
            explanation += f"\n- {get_text('right_endpoint_explanation')}"
        elif method == 'midpoint':
            explanation += f"\n- {get_text('midpoint_explanation')}"
        
        explanation += f"""
        
        {get_text('convergence_explanation')}:
        
        $\\lim_{{n \\to \\infty}} \\sum_{{i=1}}^{{n}} f({variable}_i^*) \\Delta {variable} = \\int_{{{lower_bound}}}^{{{upper_bound}}} f({variable}) \\, d{variable}$
        """
        
        st.markdown(explanation)
    
    # Download button for the solution
    solution_text = f"""
{get_text('riemann_sum_calculation')} f({variable}) = {func_str} {get_text('on')} [{lower_bound}, {upper_bound}] {get_text('with')} n = {n}

{get_text('method')}: {method_text}
{get_text('result')}: {result:.6f}

{get_text('step_by_step_solution')}:
"""
    for i, step in enumerate(steps):
        clean_step = step.replace("$", "").replace("\\", "")
        solution_text += f"\n{i+1}. {clean_step}"
    
    st.download_button(
        label=get_text("download_solution"),
        data=solution_text,
        file_name=f"riemann_sum_{method}_n{n}.txt",
        mime="text/plain",
        key="download_riemann_solution"
    )

def display_area_between_curves_solution(func1_str: str, func2_str: str, 
                                       lower_bound: float, upper_bound: float, 
                                       result: float, steps: list, 
                                       diagram_provided: bool = True, variable: str = "x"):
    """
    Display the solution to an area between curves calculation with step-by-step workings.
    """
    st.markdown("## " + get_text("area_between_curves_solution"))
    
    # Display the problem statement
    st.markdown(f"### {get_text('calculating_area_between')} $y = {func1_str}$ {get_text('and')} $y = {func2_str}$ {get_text('from')} ${variable} = {lower_bound}$ {get_text('to')} ${variable} = {upper_bound}$")
    
    # Display the result prominently
    st.success(f"### {get_text('result')}: {result:.6f} {get_text('square_units')}")
    
    # Display step-by-step solution
    st.markdown("### " + get_text("step_by_step_solution"))
    
    with st.expander(get_text("show_solution_steps"), expanded=True):
        for i, step in enumerate(steps):
            st.markdown(step)
            if i < len(steps) - 1:
                st.markdown("---")
    
    # Explanation of what the area represents
    with st.expander(get_text("what_area_represents"), expanded=False):
        st.markdown(f"**{get_text('area_explanation')}:**")
        
        explanation = f"""
        {get_text('area_between_explanation')} $y = {func1_str}$ {get_text('and')} $y = {func2_str}$
        {get_text('from')} ${variable} = {lower_bound}$ {get_text('to')} ${variable} = {upper_bound}$.
        
        {get_text('area_formula')}:
        
        $\\text{{{get_text('area')}}} = \\int_{{{lower_bound}}}^{{{upper_bound}}} |f_1({variable}) - f_2({variable})| \\, d{variable}$
        
        {get_text('area_practice')}:
        
        $\\text{{{get_text('area')}}} = \\int_{{{lower_bound}}}^{{{upper_bound}}} [\\text{{{get_text('upper_function')}}} - \\text{{{get_text('lower_function')}}}] \\, d{variable}$
        """
        
        st.markdown(explanation)
        
        # Applications
        st.markdown(f"**{get_text('applications')}:**")
        st.markdown(f"- {get_text('physical_applications')}")
        st.markdown(f"- {get_text('economic_applications')}")
        st.markdown(f"- {get_text('engineering_applications')}")
    
    # Download button for the solution
    solution_text = f"""
{get_text('area_between_curves_calculation')} y = {func1_str} {get_text('and')} y = {func2_str} {get_text('on')} [{lower_bound}, {upper_bound}]

{get_text('result')}: {result:.6f} {get_text('square_units')}

{get_text('step_by_step_solution')}:
"""
    for i, step in enumerate(steps):
        clean_step = step.replace("$", "").replace("\\", "")
        solution_text += f"\n{i+1}. {clean_step}"
    
    st.download_button(
        label=get_text("download_solution"),
        data=solution_text,
        file_name=f"area_between_curves.txt",
        mime="text/plain",
        key="download_area_solution"
    )

def display_error_message(error_type: str, error_details: str):
    """
    Display a formatted error message with helpful suggestions.
    """
    st.error(f"❌ {get_text('error')}: {get_text(error_type)}")
    
    with st.expander(get_text("error_details"), expanded=True):
        st.code(error_details)
        
        # Provide helpful suggestions based on error type
        if "parsing" in error_type.lower():
            st.markdown(f"**{get_text('suggestions')}:**")
            st.markdown(f"- {get_text('check_syntax')}")
            st.markdown(f"- {get_text('use_star_multiplication')}")
            st.markdown(f"- {get_text('check_parentheses')}")
            st.markdown(f"- {get_text('use_valid_functions')}")
        
        elif "conversion" in error_type.lower():
            st.markdown(f"**{get_text('suggestions')}:**")
            st.markdown(f"- {get_text('check_bounds_numeric')}")
            st.markdown(f"- {get_text('use_pi_for_pi')}")
            st.markdown(f"- {get_text('use_e_for_e')}")
        
        elif "evaluation" in error_type.lower():
            st.markdown(f"**{get_text('suggestions')}:**")
            st.markdown(f"- {get_text('check_domain')}")
            st.markdown(f"- {get_text('avoid_division_zero')}")
            st.markdown(f"- {get_text('check_complex_results')}")

def create_solution_summary(calculation_type: str, inputs: dict, result: float):
    """
    Create a summary card for the solution.
    """
    with st.container():
        st.markdown("### " + get_text("calculation_summary"))
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**{get_text('calculation_type')}:** {get_text(calculation_type)}")
            for key, value in inputs.items():
                st.markdown(f"**{get_text(key)}:** {value}")
        
        with col2:
            st.metric(
                label=get_text("final_result"),
                value=f"{result:.6f}"
            )
            
            # Add interpretation based on result
            if abs(result) < 1e-10:
                st.info(get_text("result_near_zero"))
            elif result > 0:
                st.success(get_text("result_positive"))
            else:
                st.warning(get_text("result_negative"))
