import streamlit as st
import numpy as np
from utils.calculator import solve_integral
from utils.plotting import plot_integral
from components.solution_display import display_solution
from assets.simple_examples import engineering_scenarios
from assets.translations import get_text

def show():
    """Display software engineering scenarios related to integrals."""
    
    st.title("⚙️ " + get_text("engineering_scenarios"))
    st.markdown(get_text("engineering_scenarios_description"))
    
    # Navigation tabs
    tab1, tab2, tab3 = st.tabs([
        get_text("random_scenario"),
        get_text("scenario_gallery"), 
        get_text("custom_scenario")
    ])
    
    with tab1:
        show_random_scenario()
    
    with tab2:
        show_scenario_gallery()
        
    with tab3:
        show_custom_scenario()

def show_random_scenario():
    """Show a single random engineering scenario."""
    
    import random
    
    # Button to generate scenario
    col1, col2 = st.columns([1, 3])
    
    with col1:
        if st.button("🎲 Generar Escenario Aleatorio", type="primary"):
            # Select random scenario from simple examples
            scenario_key = random.choice(list(engineering_scenarios.keys()))
            scenario = engineering_scenarios[scenario_key].copy()
            scenario['title'] = scenario_key
            st.session_state.current_scenario = scenario
            st.rerun()
    
    with col2:
        st.info("Haz clic para generar un escenario de ingeniería aleatorio con problemas reales.")
    
    # Initialize scenario if none exists
    if "current_scenario" not in st.session_state:
        scenario_key = list(engineering_scenarios.keys())[0]
        scenario = engineering_scenarios[scenario_key].copy()
        scenario['title'] = scenario_key
        st.session_state.current_scenario = scenario
    
    scenario = st.session_state.current_scenario
    
    # Display the current scenario
    display_engineering_scenario(scenario)

def show_scenario_gallery():
    """Show multiple scenarios for selection."""
    
    st.subheader("🏛️ Galería de Escenarios de Ingeniería")
    st.markdown("Explora múltiples escenarios de ingeniería de software generados automáticamente.")
    
    # Convert engineering scenarios to list format
    scenario_list = []
    for title, scenario_data in engineering_scenarios.items():
        scenario = scenario_data.copy()
        scenario['title'] = title
        scenario_list.append(scenario)
    
    if scenario_list:
        # Display scenarios in a grid
        cols = st.columns(2)
        
        for i, scenario in enumerate(scenario_list):
            with cols[i % 2]:
                with st.container():
                    st.markdown(f"### {scenario['title']}")
                    st.markdown(f"**Función:** `{scenario['function']}`")
                    st.markdown(f"**Límites:** [{scenario['lower_bound']}, {scenario['upper_bound']}]")
                    st.markdown(f"**Variable:** {scenario['variable']}")
                    
                    if st.button(f"Seleccionar Escenario {i+1}", 
                               key=f"select_scenario_{i}"):
                        st.session_state.selected_gallery_scenario = scenario
                        st.rerun()
                    
                    st.markdown("---")
        
        # Display selected scenario
        if "selected_gallery_scenario" in st.session_state:
            st.subheader("📋 Escenario Seleccionado")
            display_engineering_scenario(st.session_state.selected_gallery_scenario)
    else:
        st.warning("No se pudieron generar escenarios válidos.")

def show_custom_scenario():
    """Allow users to create custom engineering scenarios."""
    
    st.subheader(get_text("create_custom_scenario"))
    st.markdown(get_text("custom_scenario_description"))
    
    # Input fields for custom scenario
    col1, col2 = st.columns(2)
    
    with col1:
        title = st.text_input(
            get_text("scenario_title"),
            value="Análisis de Rendimiento Personalizado",
            key="custom_title"
        )
        
        function = st.text_input(
            get_text("mathematical_function"),
            value="t^2 + 5*t",
            key="custom_function",
            help=get_text("function_input_help")
        )
        
        context = st.text_input(
            get_text("engineering_context"),
            value="uso de memoria del sistema",
            key="custom_context"
        )
    
    with col2:
        lower_bound = st.text_input(
            get_text("lower_bound"),
            value="0",
            key="custom_lower"
        )
        
        upper_bound = st.text_input(
            get_text("upper_bound"),
            value="10",
            key="custom_upper"
        )
        
        unit = st.text_input(
            get_text("measurement_unit"),
            value="MB/min",
            key="custom_unit"
        )
    
    # Description text area
    description = st.text_area(
        get_text("scenario_description"),
        value=f"El sistema experimenta {context} modelado por la función f(t) = {function}. Calcula el valor acumulado total en el intervalo dado.",
        key="custom_description",
        height=100
    )
    
    # Create custom scenario button
    if st.button("🛠️ " + get_text("create_custom_scenario"), key="create_custom"):
        # Create scenario dictionary
        custom_scenario = {
            "title": title,
            "description": description,
            "function": function,
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
            "variable": "t",
            "context": context,
            "unit": unit,
            "complexity": "personalizada",
            "function_type": "custom"
        }
        
        # Validate the custom scenario
        is_valid, error_msg = validate_scenario(custom_scenario)
        
        if is_valid:
            st.session_state.custom_scenario = custom_scenario
            st.success(get_text("custom_scenario_created"))
            st.rerun()
        else:
            st.error(f"{get_text('validation_error')}: {error_msg}")
    
    # Display custom scenario if created
    if "custom_scenario" in st.session_state:
        st.markdown("---")
        st.subheader(get_text("your_custom_scenario"))
        display_engineering_scenario(st.session_state.custom_scenario)

def display_engineering_scenario(scenario):
    """Display a complete engineering scenario with calculation capabilities."""
    
    # Display scenario header
    st.subheader(f"📊 {scenario['title']}")
    st.write(scenario['description'])
    
    # Information cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"""
        **{get_text('mathematical_function')}:**  
        `{scenario['function']}`
        
        **Contexto:** {scenario.get('context', 'Análisis de rendimiento del sistema')}  
        **Complejidad:** {scenario.get('complexity', 'Media')}
        """)
    
    with col2:
        st.success(f"""
        **{get_text('integration_bounds')}:**  
        {get_text('lower')}: `{scenario['lower_bound']}`  
        {get_text('upper')}: `{scenario['upper_bound']}`
        
        **{get_text('measurement_unit')}:** {scenario['unit']}
        """)
    
    # Calculation button
    if st.button("🧮 " + get_text("calculate_integral"), key=f"calc_{hash(str(scenario))}", type="secondary"):
        with st.spinner(get_text("calculating")):
            try:
                result, steps = solve_integral(
                    scenario['function'], 
                    scenario['lower_bound'], 
                    scenario['upper_bound'],
                    scenario.get('variable', 't')
                )
                
                # Display visualization
                st.subheader("📈 " + get_text("visualization"))
                plot_integral(
                    scenario['function'], 
                    scenario['lower_bound'], 
                    scenario['upper_bound'],
                    scenario.get('variable', 't')
                )
                
                # Display solution
                st.subheader("📝 " + get_text("step_by_step_solution"))
                display_solution(
                    scenario['function'], 
                    scenario['lower_bound'], 
                    scenario['upper_bound'], 
                    result, 
                    steps,
                    scenario.get('variable', 't')
                )
                
                # Interpretation of result
                st.subheader("🎯 " + get_text("result_interpretation"))
                st.success(f"""
                **{get_text('result')}:** {result:.4f} {scenario['unit']}
                
                **{get_text('interpretation')}:** {get_text('area_under_curve_represents')} {scenario['context'].lower()}.
                {get_text('total_accumulated_value')}.
                """)
                
                # Additional insights
                with st.expander(get_text("engineering_insights"), expanded=False):
                    st.markdown(f"**{get_text('practical_meaning')}:**")
                    
                    if result > 0:
                        st.markdown(f"- {get_text('positive_accumulated_value')}")
                    else:
                        st.markdown(f"- {get_text('negative_accumulated_value')}")
                    
                    # Provide context-specific insights
                    if "memoria" in scenario['context'].lower():
                        st.markdown(f"- {get_text('memory_usage_insight')}")
                    elif "cpu" in scenario['context'].lower():
                        st.markdown(f"- {get_text('cpu_usage_insight')}")
                    elif "usuarios" in scenario['context'].lower():
                        st.markdown(f"- {get_text('user_load_insight')}")
                    else:
                        st.markdown(f"- {get_text('general_performance_insight')}")
                
            except Exception as e:
                st.error(f"❌ {get_text('calculation_error')}: {str(e)}")
                st.info(f"💡 {get_text('try_different_scenario')}")
