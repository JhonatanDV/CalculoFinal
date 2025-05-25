import streamlit as st
import numpy as np
from utils.calculator import solve_integral
from utils.plotting import plot_integral
from components.solution_display import display_solution
from utils.random_generator import generate_engineering_scenario
from assets.translations import get_text

def show():
    """Mostrar escenarios de ingeniería de software relacionados con integrales."""
    
    st.header(get_text("engineering_scenarios"))
    st.markdown(get_text("engineering_scenarios_description"))
    
    # Botón para generar escenario aleatorio
    col1, col2 = st.columns([1, 3])
    
    with col1:
        if st.button("🎲 Generar Escenario Aleatorio", type="primary"):
            if "current_scenario" not in st.session_state:
                st.session_state.current_scenario = generate_engineering_scenario()
            else:
                st.session_state.current_scenario = generate_engineering_scenario()
            st.rerun()
    
    with col2:
        st.info("Genera un escenario de ingeniería completamente aleatorio con función y límites únicos")
    
    # Inicializar escenario si no existe
    if "current_scenario" not in st.session_state:
        st.session_state.current_scenario = generate_engineering_scenario()
    
    scenario = st.session_state.current_scenario
    
    # Mostrar el escenario actual
    st.subheader(f"📊 {scenario['title']}")
    st.write(scenario['description'])
    
    # Información del escenario en tarjetas
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"""
        **Función matemática:**  
        `{scenario['function']}`
        
        **Contexto:** {scenario['context']}  
        **Complejidad:** {scenario['complexity']}
        """)
    
    with col2:
        st.success(f"""
        **Límites de integración:**  
        Inferior: `{scenario['lower_bound']}`  
        Superior: `{scenario['upper_bound']}`
        
        **Unidad de medida:** {scenario['unit']}
        """)
    
    # Botón para calcular
    if st.button("🧮 Calcular Integral", type="secondary"):
        with st.spinner("Calculando..."):
            try:
                result, steps = solve_integral(
                    scenario['function'], 
                    scenario['lower_bound'], 
                    scenario['upper_bound']
                )
                
                # Mostrar gráfica
                st.subheader("📈 Visualización")
                plot_integral(scenario['function'], scenario['lower_bound'], scenario['upper_bound'])
                
                # Mostrar solución
                st.subheader("📝 Solución paso a paso")
                display_solution(
                    scenario['function'], 
                    scenario['lower_bound'], 
                    scenario['upper_bound'], 
                    result, 
                    steps
                )
                
                # Interpretación del resultado
                st.subheader("🎯 Interpretación del Resultado")
                st.success(f"""
                **Resultado:** {result:.4f} {scenario['unit']}
                
                **Interpretación:** El área bajo la curva representa {scenario['description'].lower()}.
                Este valor indica la cantidad total acumulada durante el período analizado.
                """)
                
            except Exception as e:
                st.error(f"❌ Error al calcular: {str(e)}")
                st.info("💡 Intenta generar un nuevo escenario si persiste el error.")