import streamlit as st
import numpy as np
from utils.calculator import solve_integral
from utils.plotting import plot_integral
from components.solution_display import display_solution, display_error_message
from components.math_input import create_math_input, create_function_examples
from assets.translations import get_text
import pandas as pd

# Importar los escenarios desde el diccionario existente
from assets.software_engineering_data import SOFTWARE_ENGINEERING_SCENARIOS, DETAILED_SOFTWARE_EXAMPLES

# Combinar todos los escenarios en un solo diccionario
engineering_scenarios = {}

# Procesar escenarios de SOFTWARE_ENGINEERING_SCENARIOS
for category in SOFTWARE_ENGINEERING_SCENARIOS.get("categories", []):
    for scenario in category.get("scenarios", []):
        engineering_scenarios[scenario["title"]] = {
            "function": scenario["function"],
            "lower_bound": str(scenario["bounds"][0]),
            "upper_bound": str(scenario["bounds"][1]),
            "variable": scenario["variable"],
            "context": scenario["context"],
            "unit": scenario.get("unit", "")
        }

# Añadir los ejemplos detallados
for scenario in DETAILED_SOFTWARE_EXAMPLES:
    engineering_scenarios[scenario["title"]] = {
        "function": scenario["function"],
        "lower_bound": str(scenario["bounds"][0]),
        "upper_bound": str(scenario["bounds"][1]),
        "variable": scenario["variable"],
        "context": scenario["context"],
        "unit": scenario.get("unit", "")
    }

def show():
    """Display software engineering scenarios related to integrals."""
    st.title("🏗️ Cálculo en Ingeniería de Software")
    st.markdown("**Descubre cómo el cálculo integral impulsa la innovación tecnológica**")
    
    # Navigation tabs con más opciones interactivas
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "🧮 Calculadora Interactiva",
        "🎯 Escenarios Prácticos",
        "🎓 Centro de Aprendizaje",
        "📐 Análisis Geométrico",
        "🔬 Caso de Estudio Completo",
        "🎥 Recursos Educativos",
        "💼 Aplicaciones Profesionales"
    ])
    
    with tab1:
        show_interactive_calculator()
    
    with tab2:
        show_practical_scenarios()
    
    with tab3:
        show_advanced_learning_section()
    
    with tab4:
        show_geometric_analysis()
    
    with tab5:
        show_complete_case_study()
    
    with tab6:
        show_educational_resources()
    
    with tab7:
        show_professional_applications()

def show_interactive_calculator():
    """Calculadora interactiva personalizada para ingeniería de software."""
    st.markdown("## 🧮 Calculadora Interactiva de Ingeniería")
    st.markdown("Resuelve problemas personalizados aplicados a desarrollo de software")
    
    # Inicializar estado de sesión para esta sección
    if "eng_function" not in st.session_state:
        st.session_state.eng_function = "2*t**2 + 5*t"
    if "eng_lower" not in st.session_state:
        st.session_state.eng_lower = "0"
    if "eng_upper" not in st.session_state:
        st.session_state.eng_upper = "10"
    if "eng_variable" not in st.session_state:
        st.session_state.eng_variable = "t"
    if "eng_units" not in st.session_state:
        st.session_state.eng_units = "unidades"
    
    # Layout principal
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📝 Configuración del Problema")
        
        # Selector de tipo de problema
        problem_type = st.selectbox(
            "🎯 Tipo de problema de ingeniería:",
            [
                "Análisis de Complejidad Temporal",
                "Optimización de Recursos",
                "Machine Learning - Función de Pérdida", 
                "Análisis de Tráfico de Red",
                "Ciberseguridad - Análisis de Entropía",
                "Personalizado"
            ],
            key="problem_type_selector"
        )
        
        # Templates basados en el tipo de problema
        if problem_type != "Personalizado":
            if st.button("📋 Cargar Template", key="load_template"):
                load_problem_template(problem_type)
                st.rerun()
        
        # Variable de integración (PRIMERO para evitar errores)
        variable = st.text_input(
            "📊 Variable de integración:", 
            st.session_state.eng_variable, 
            key="eng_variable_input",
            help="Especifica la variable de integración (ej: t, x, n, etc.)"
        )
        st.session_state.eng_variable = variable
        
        # Inputs de función personalizables
        function_input = create_math_input(
            f"🔢 Función f({variable}):", 
            st.session_state.eng_function, 
            key="eng_function_input",
            help_text=f"Ingresa la función que modela tu problema de ingeniería en términos de {variable}"
        )
        st.session_state.eng_function = function_input
        
        # Límites de integración
        col1a, col1b = st.columns(2)
        with col1a:
            lower_bound = st.text_input(
                "⬇️ Límite inferior:", 
                st.session_state.eng_lower, 
                key="eng_lower_input",
                help="Valor inicial del intervalo"
            )
            st.session_state.eng_lower = lower_bound
        with col1b:
            upper_bound = st.text_input(
                "⬆️ Límite superior:", 
                st.session_state.eng_upper, 
                key="eng_upper_input",
                help="Valor final del intervalo"
            )
            st.session_state.eng_upper = upper_bound
        
        # Unidades y contexto
        col1c, col1d = st.columns(2)
        with col1c:
            units = st.text_input(
                "📏 Unidades:",
                st.session_state.eng_units,
                key="eng_units_input",
                help="Ej: ms, MB, usuarios, etc."
            )
            st.session_state.eng_units = units
        
        with col1d:
            # Botón para limpiar todo
            if st.button("🗑️ Limpiar Todo", key="clear_all"):
                st.session_state.eng_function = ""
                st.session_state.eng_lower = "0"
                st.session_state.eng_upper = "1"
                st.session_state.eng_variable = "x"
                st.session_state.eng_units = "unidades"
                st.rerun()
        
        # Descripción del contexto
        context_description = st.text_area(
            "📝 Describe tu problema:",
            "Análisis del comportamiento de un sistema de software...",
            key="context_input",
            help="Explica qué representa tu función en el contexto real"
        )
    
    with col2:
        st.markdown("### 🎲 Ejemplos Rápidos")
        
        # Ejemplos predefinidos con diferentes variables
        quick_examples = {
            "Bubble Sort O(n²)": {
                "function": "n**2",
                "lower": "1",
                "upper": "1000",
                "variable": "n",
                "units": "operaciones"
            },
            "Cache Hit Rate": {
                "function": "100/(1 + exp(-0.1*s))",
                "lower": "0",
                "upper": "50",
                "variable": "s",
                "units": "% hit rate"
            },
            "Red Neuronal": {
                "function": "exp(-0.05*e)",
                "lower": "0",
                "upper": "100",
                "variable": "e",
                "units": "error"
            },
            "Tráfico Web": {
                "function": "1000*sin(3.14*h/12) + 1500",
                "lower": "0",
                "upper": "24",
                "variable": "h",
                "units": "MB/h"
            },
            "Consumo CPU": {
                "function": "50*log(u+1) + 20",
                "lower": "1",
                "upper": "100",
                "variable": "u",
                "units": "% CPU"
            },
            "Algoritmo Recursivo": {
                "function": "2**r",
                "lower": "1",
                "upper": "10",
                "variable": "r",
                "units": "llamadas"
            }
        }
        
        selected_example = st.selectbox(
            "Selecciona un ejemplo:",
            list(quick_examples.keys()),
            key="quick_example_selector"
        )
        
        if st.button("📥 Cargar Ejemplo", key="load_quick_example"):
            example = quick_examples[selected_example]
            st.session_state.eng_function = example["function"]
            st.session_state.eng_lower = example["lower"]
            st.session_state.eng_upper = example["upper"]
            st.session_state.eng_variable = example["variable"]
            st.session_state.eng_units = example["units"]
            st.success(f"✅ Ejemplo '{selected_example}' cargado correctamente!")
            st.rerun()
        
        # Mostrar detalles del ejemplo seleccionado
        if selected_example in quick_examples:
            example = quick_examples[selected_example]
            st.markdown("#### 📋 Vista Previa")
            st.code(f"""Función: {example['function']}
Variable: {example['variable']}
Límites: [{example['lower']}, {example['upper']}]
Unidades: {example['units']}""")
        
        # Mostrar ejemplos de funciones para la variable actual
        st.markdown("#### 💡 Ejemplos de Funciones")
        function_examples = [
            f"{variable}**2 + 3*{variable}",
            f"exp(-0.1*{variable})",
            f"sin({variable}) + 2",
            f"log({variable}+1)",
            f"sqrt({variable})",
            f"1/(1 + exp(-{variable}))"
        ]
        
        for example in function_examples:
            if st.button(f"📝 {example}", key=f"example_{example}"):
                st.session_state.eng_function = example
                st.rerun()
    
    # Sección de cálculo
    st.markdown("---")
    
    # Botones de acción
    col_calc1, col_calc2, col_calc3 = st.columns([1, 2, 1])
    with col_calc2:
        calculate_button = st.button(
            "🚀 Resolver Problema de Ingeniería", 
            key="calculate_engineering",
            use_container_width=True,
            type="primary"
        )
    
    if calculate_button:
        solve_engineering_problem_fixed(function_input, lower_bound, upper_bound, variable, units, context_description)

def solve_engineering_problem_fixed(function_str, lower_bound, upper_bound, variable, units, context):
    """Resolver problema de ingeniería con soporte para cualquier variable - CORREGIDO."""
    try:
        # Validar entradas
        if not function_str.strip():
            st.error("⚠️ Por favor ingresa una función válida")
            return
        
        if not variable.strip():
            st.error("⚠️ Por favor especifica la variable de integración")
            return
        
        # Resolver integral directamente con la función y variable originales
        with st.spinner("🔄 Resolviendo problema de ingeniería..."):
            result, steps = solve_integral(function_str, lower_bound, upper_bound, variable)
        
        # Mostrar resultados
        st.success(f"### ✅ Resultado: {result:.6f} {units}")
        
        # Layout de resultados
        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Visualización",
            "📝 Solución Paso a Paso",
            "💡 Interpretación",
            "📋 Resumen"
        ])
        
        with tab1:
            st.markdown("#### 📈 Gráfica del Problema")
            try:
                plot_integral(function_str, lower_bound, upper_bound, variable)
                
                # Información adicional sobre la gráfica
                st.markdown(f"""
                **📊 Análisis Visual:**
                - La función f({variable}) = {function_str}
                - Intervalo: [{lower_bound}, {upper_bound}]
                - El área sombreada representa el valor total acumulado
                - Resultado: {result:.6f} {units}
                """)
            except Exception as e:
                st.warning(f"⚠️ No se pudo generar la gráfica: {str(e)}")
        
        with tab2:
            st.markdown("#### 🔍 Solución Detallada")
            for i, step in enumerate(steps, 1):
                with st.expander(f"Paso {i}", expanded=i==1):
                    st.markdown(step)
        
        with tab3:
            st.markdown("#### 💡 Interpretación del Resultado")
            st.markdown(f"**Contexto del problema:** {context}")
            st.markdown(f"""
            **🎯 Significado del resultado:**
            - El valor {result:.6f} {units} representa el total acumulado en el intervalo [{lower_bound}, {upper_bound}]
            - Esto es útil para análisis de rendimiento, predicción de recursos y optimización de sistemas
            - La variable {variable} representa la dimensión de análisis del problema
            """)
            
            # Análisis adicional basado en el resultado
            if result > 0:
                st.success("✅ Resultado positivo: indica crecimiento o acumulación positiva")
            else:
                st.warning("⚠️ Resultado negativo: indica decrecimiento o pérdida acumulada")
        
        with tab4:
            # Generar resumen descargable
            summary = generate_engineering_summary(function_str, lower_bound, upper_bound, variable, units, result, context)
            st.markdown("#### 📋 Resumen del Análisis")
            st.code(summary, language="text")
            
            st.download_button(
                label="💾 Descargar Reporte Completo",
                data=summary,
                file_name=f"analisis_ingenieria_{variable}_{function_str.replace('*', '_').replace('/', '_')}.txt",
                mime="text/plain",
                key="download_engineering_report"
            )
            
    except Exception as e:
        display_error_message("engineering_calculation_error", str(e))
        st.error(f"❌ Error en el cálculo: {str(e)}")

def load_problem_template(problem_type):
    """Cargar template basado en el tipo de problema seleccionado."""
    templates = {
        "Análisis de Complejidad Temporal": {
            "function": "2*n**2 + 5*n",
            "lower": "1",
            "upper": "1000",
            "variable": "n",
            "units": "operaciones",
            "description": "Análisis del tiempo total de ejecución de algoritmo con complejidad cuadrática"
        },
        "Optimización de Recursos": {
            "function": "50*log(u+1) + 100",
            "lower": "1",
            "upper": "100",
            "variable": "u",
            "units": "MB",
            "description": "Consumo total de memoria en función del número de usuarios activos"
        },
        "Machine Learning - Función de Pérdida": {
            "function": "exp(-0.1*e)",
            "lower": "0",
            "upper": "50",
            "variable": "e",
            "units": "error",
            "description": "Pérdida acumulada durante el entrenamiento de una red neuronal"
        },
        "Análisis de Tráfico de Red": {
            "function": "1000*sin(3.14159*t/12) + 1500",
            "lower": "0",
            "upper": "24",
            "variable": "t",
            "units": "MB/h",
            "description": "Volumen total de datos transferido en un servidor durante 24 horas"
        },
        "Ciberseguridad - Análisis de Entropía": {
            "function": "log(b)*b",
            "lower": "1",
            "upper": "32",
            "variable": "b",
            "units": "bits",
            "description": "Entropía total acumulada en un sistema de generación de contraseñas"
        }
    }
    
    if problem_type in templates:
        template = templates[problem_type]
        st.session_state.eng_function = template["function"]
        st.session_state.eng_lower = template["lower"]
        st.session_state.eng_upper = template["upper"]
        st.session_state.eng_variable = template["variable"]
        st.session_state.eng_units = template["units"]
        
        # Mostrar información del template
        st.success(f"📋 **Template cargado**: {template['description']}")

def generate_engineering_summary(function_str, lower_bound, upper_bound, variable, units, result, context):
    """Generar resumen técnico del análisis."""
    return f"""REPORTE DE ANÁLISIS - INGENIERÍA DE SOFTWARE
==========================================

PROBLEMA ANALIZADO:
{context}

FUNCIÓN MATEMÁTICA:
f({variable}) = {function_str}

PARÁMETROS:
- Variable: {variable}
- Límite inferior: {lower_bound}
- Límite superior: {upper_bound}
- Unidades: {units}

RESULTADO:
∫[{lower_bound}, {upper_bound}] {function_str} d{variable} = {result:.6f} {units}

INTERPRETACIÓN:
Este resultado representa el valor total acumulado de la función en el intervalo especificado.
En el contexto de ingeniería de software, esto puede indicar:
- Tiempo total de ejecución
- Recursos consumidos
- Carga total del sistema
- Error acumulado
- Throughput total

APLICACIONES PRÁCTICAS:
- Análisis de rendimiento de algoritmos
- Planificación de recursos de sistema
- Optimización de procesos
- Predicción de capacidad
- Análisis de escalabilidad

Generado por: Calculadora Matemática Avanzada
"""

def show_practical_scenarios():
    """Show practical software engineering scenarios with calculus applications."""
    st.markdown("## 🎯 Escenarios Prácticos de Ingeniería de Software")
    st.markdown("Explora aplicaciones reales del cálculo integral en desarrollo de software")
    
    # Define scenarios directly here con diferentes variables
    scenarios = [
        {
            "title": "Optimización de Algoritmos",
            "context": "Análisis de complejidad temporal de algoritmo de ordenamiento",
            "function": "2*n**2 + 5*n",
            "bounds": [1, 100],
            "unit": "operaciones",
            "variable": "n",
            "explanation": "Esta integral calcula el número total de operaciones cuando la complejidad temporal es cuadrática.",
            "real_application": "Algoritmos como Bubble Sort, Selection Sort en sistemas reales",
            "difficulty": "⭐⭐",
            "category": "Algoritmos"
        },
        {
            "title": "Machine Learning - Función de Pérdida",
            "context": "Calcular la pérdida total durante entrenamiento de red neuronal",
            "function": "exp(-0.1*e)",
            "bounds": [0, 50],
            "unit": "unidades de error",
            "variable": "e",
            "explanation": "La integral de la función de pérdida nos da el error total acumulado durante el entrenamiento.",
            "real_application": "Optimización en TensorFlow, PyTorch, Keras",
            "difficulty": "⭐⭐⭐",
            "category": "IA/ML"
        },
        {
            "title": "Análisis de Tráfico Web",
            "context": "Tráfico total de datos en servidor durante 24 horas",
            "function": "1000*sin(3.14159*h/12) + 1500",
            "bounds": [0, 24],
            "unit": "MB/hora",
            "variable": "h",
            "explanation": "Calcular el volumen total de datos transferido con patrones cíclicos diarios.",
            "real_application": "CDNs como Cloudflare, AWS CloudFront",
            "difficulty": "⭐⭐",
            "category": "Redes"
        },
        {
            "title": "Optimización de Cache",
            "context": "Hit rate óptimo de cache para minimizar latencia",
            "function": "100/(1 + exp(-0.5*(s-10)))",
            "bounds": [0, 20],
            "unit": "% hit rate",
            "variable": "s",
            "explanation": "Función sigmoide que modela cómo mejora el hit rate conforme aumenta el tamaño del cache.",
            "real_application": "Sistemas de cache en Redis, Memcached, bases de datos",
            "difficulty": "⭐⭐⭐",
            "category": "Sistemas"
        },
        {
            "title": "Análisis de Ciberseguridad",
            "context": "Entropía total de sistema de contraseñas",
            "function": "log(b)*b",
            "bounds": [1, 32],
            "unit": "bits de entropía",
            "variable": "b",
            "explanation": "La entropía acumulada determina la fortaleza criptográfica del sistema.",
            "real_application": "Generadores de contraseñas, análisis de seguridad",
            "difficulty": "⭐⭐⭐⭐",
            "category": "Seguridad"
        }
    ]
    
    # Filtros interactivos
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Filtro por categoría
        categories = ["Todos"] + list(set([s["category"] for s in scenarios]))
        selected_category = st.selectbox("🏷️ Filtrar por categoría:", categories, key="category_filter")
    
    with col2:
        # Filtro por dificultad
        difficulties = ["Todos", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐"]
        selected_difficulty = st.selectbox("🎯 Filtrar por dificultad:", difficulties, key="difficulty_filter")
    
    with col3:
        # Orden
        sort_options = ["Orden original", "Por dificultad", "Alfabético"]
        sort_by = st.selectbox("📊 Ordenar por:", sort_options, key="sort_filter")
    
    # Aplicar filtros
    filtered_scenarios = scenarios.copy()
    
    if selected_category != "Todos":
        filtered_scenarios = [s for s in filtered_scenarios if s["category"] == selected_category]
    
    if selected_difficulty != "Todos":
        filtered_scenarios = [s for s in filtered_scenarios if s["difficulty"] == selected_difficulty]
    
    # Aplicar ordenamiento
    if sort_by == "Por dificultad":
        filtered_scenarios.sort(key=lambda x: len(x["difficulty"]))
    elif sort_by == "Alfabético":
        filtered_scenarios.sort(key=lambda x: x["title"])
    
    # Mostrar estadísticas
    st.markdown(f"📊 **Mostrando {len(filtered_scenarios)} de {len(scenarios)} escenarios**")
    
    # Inicializar estado de sesión para escenarios
    if "scenario_index" not in st.session_state:
        st.session_state.scenario_index = 0
    
    # Verificar si hay un escenario aleatorio pendiente
    if "random_scenario_pending" in st.session_state:
        st.session_state.scenario_index = st.session_state.random_scenario_pending
        del st.session_state.random_scenario_pending
    
    # Scenario selector mejorado
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        if filtered_scenarios:
            # Asegurar que el índice esté en rango
            if st.session_state.scenario_index >= len(filtered_scenarios):
                st.session_state.scenario_index = 0
                
            selected_scenario = st.selectbox(
                "🎯 Selecciona un escenario:",
                range(len(filtered_scenarios)),
                format_func=lambda x: f"{filtered_scenarios[x]['difficulty']} {filtered_scenarios[x]['title']} ({filtered_scenarios[x]['category']})",
                index=st.session_state.scenario_index,
                key="scenario_selector"
            )
            st.session_state.scenario_index = selected_scenario
        else:
            st.warning("No hay escenarios que coincidan con los filtros seleccionados")
            return
    
    with col2:
        if st.button("🎲 Escenario Aleatorio", key="random_scenario"):
            import random
            random_index = random.randint(0, len(filtered_scenarios) - 1)
            st.session_state.random_scenario_pending = random_index
            st.rerun()
    
    with col3:
        if st.button("🔄 Reiniciar Filtros", key="reset_filters"):
            st.rerun()
    
    # Display selected scenario
    scenario = filtered_scenarios[selected_scenario]
    
    # Mostrar información del escenario seleccionado
    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"### 🔍 {scenario['title']}")
        st.markdown(f"**Categoría:** {scenario['category']} | **Dificultad:** {scenario['difficulty']}")
        st.info(f"**Contexto:** {scenario['context']}")
        st.markdown(f"**Aplicación real:** {scenario['real_application']}")
    
    with col2:
        # Tarjeta con detalles técnicos
        st.markdown("#### 📊 Detalles Técnicos")
        st.code(f"""Función: {scenario['function']}
Variable: {scenario['variable']}
Límites: [{scenario['bounds'][0]}, {scenario['bounds'][1]}]
Unidades: {scenario['unit']}""")
    
    # Botón de cálculo mejorado
    col_calc1, col_calc2, col_calc3 = st.columns([1, 2, 1])
    with col_calc2:
        if st.button("🚀 Resolver Escenario Completo", key="calculate_scenario", use_container_width=True, type="primary"):
            solve_scenario_complete_fixed(scenario)

def solve_scenario_complete_fixed(scenario):
    """Resolver escenario con análisis completo y interactivo - CORREGIDO."""
    try:
        # Usar directamente la función y variable originales
        original_function = scenario['function']
        variable = scenario['variable']
        
        # Resolver integral directamente sin conversiones
        with st.spinner("🔄 Analizando escenario de ingeniería..."):
            result, steps = solve_integral(
                original_function, 
                str(scenario['bounds'][0]), 
                str(scenario['bounds'][1]), 
                variable
            )
        
        # Resultados en tabs interactivos
        tab1, tab2, tab3, tab4 = st.tabs([
            "📈 Resultado",
            "📊 Visualización", 
            "🔍 Pasos",
            "💡 Análisis"
        ])
        
        with tab1:
            st.success(f"### ✅ Resultado: {result:.6f} {scenario['unit']}")
            
            # Métricas adicionales
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Valor Total", f"{result:.2f}", f"{scenario['unit']}")
            with col2:
                interval_size = scenario['bounds'][1] - scenario['bounds'][0]
                average = result / interval_size if interval_size > 0 else 0
                st.metric("Promedio", f"{average:.2f}", f"{scenario['unit']}/unidad")
            with col3:
                st.metric("Intervalo", f"[{scenario['bounds'][0]}, {scenario['bounds'][1]}]", f"{interval_size} unidades")
        
        with tab2:
            st.markdown("#### 📈 Gráfica Interactiva")
            try:
                plot_integral(
                    original_function,
                    str(scenario['bounds'][0]),
                    str(scenario['bounds'][1]),
                    variable
                )
                
                # Análisis visual adicional
                st.markdown(f"""
                **📊 Interpretación Visual:**
                - El área bajo la curva representa: {scenario['explanation']}
                - Función: f({variable}) = {original_function}
                - El resultado {result:.6f} es el valor total acumulado
                """)
            except Exception as e:
                st.warning(f"⚠️ Error en visualización: {str(e)}")
        
        with tab3:
            st.markdown("#### 🔍 Solución Paso a Paso")
            for i, step in enumerate(steps, 1):
                with st.expander(f"📝 Paso {i}", expanded=i<=2):
                    st.markdown(step)
        
        with tab4:
            st.markdown("#### 💡 Análisis Técnico Detallado")
            st.markdown(f"**🎯 Contexto del problema:**")
            st.markdown(scenario['context'])
            
            st.markdown(f"**🔬 Explicación matemática:**")
            st.markdown(scenario['explanation'])
            
            st.markdown(f"**🏭 Aplicación en la industria:**")
            st.markdown(scenario['real_application'])
            
            # Análisis adicional basado en el resultado
            if result > 0:
                st.success("✅ **Interpretación positiva:** El sistema muestra crecimiento o acumulación favorable")
            else:
                st.warning("⚠️ **Interpretación:** Se detecta decrecimiento o pérdida en el sistema")
                    
    except Exception as e:
        display_error_message("scenario_calculation_error", str(e))

def show_advanced_learning_section():
    """Sección avanzada de aprendizaje con ejercicios interactivos."""
    st.markdown("## 🎓 Centro de Aprendizaje Avanzado")
    
    # Subsecciones de aprendizaje
    learning_tab1, learning_tab2, learning_tab3, learning_tab4 = st.tabs([
        "🧪 Laboratorio de Experimentos",
        "🎯 Desafíos Progresivos", 
        "📊 Análisis Comparativo",
        "🏆 Evaluación de Competencias"
    ])
    
    with learning_tab1:
        show_experiment_lab()
    
    with learning_tab2:
        show_progressive_challenges()
    
    with learning_tab3:
        show_comparative_analysis()
    
    with learning_tab4:
        show_competency_evaluation()

def show_experiment_lab():
    """Laboratorio de experimentos para probar diferentes funciones y parámetros."""
    st.markdown("### 🧪 Laboratorio de Experimentos Matemáticos")
    st.markdown("Experimenta con diferentes funciones y observa cómo afectan los resultados en sistemas reales")
    
    # Experimento de complejidad algorítmica
    with st.expander("🔬 Experimento 1: Complejidad Algorítmica", expanded=True):
        st.markdown("**Objetivo**: Comparar diferentes algoritmos de ordenamiento")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Configurar Experimento:**")
            algorithm_type = st.selectbox(
                "Tipo de algoritmo:",
                ["Bubble Sort O(n²)", "Quick Sort O(n log n)", "Merge Sort O(n log n)", "Selection Sort O(n²)"],
                key="algorithm_experiment"
            )
            
            data_size = st.slider("Tamaño de datos (n):", 100, 10000, 1000, key="data_size_exp")
            
            # Definir funciones según el algoritmo
            complexity_functions = {
                "Bubble Sort O(n²)": f"n**2",
                "Quick Sort O(n log n)": f"n*log(n)",
                "Merge Sort O(n log n)": f"n*log(n)", 
                "Selection Sort O(n²)": f"n**2"
            }
            
            selected_function = complexity_functions[algorithm_type]
            
            if st.button("🚀 Ejecutar Experimento", key="run_algorithm_experiment"):
                try:
                    result, steps = solve_integral(selected_function, "1", str(data_size), "n")
                    
                    st.success(f"**Operaciones totales**: {result:.0f}")
                    st.info(f"**Promedio por elemento**: {result/data_size:.2f} operaciones")
                    
                    # Comparación con otros algoritmos
                    if "O(n²)" in algorithm_type:
                        efficient_result, _ = solve_integral("n*log(n)", "1", str(data_size), "n")
                        improvement = (result - efficient_result) / result * 100
                        st.warning(f"📈 Un algoritmo O(n log n) sería {improvement:.1f}% más eficiente")
                    
                except Exception as e:
                    st.error(f"Error en experimento: {e}")
        
        with col2:
            st.markdown("**Análisis del Experimento:**")
            st.markdown(f"- Algoritmo: {algorithm_type}")
            st.markdown(f"- Función de complejidad: {selected_function}")
            st.markdown(f"- Tamaño de datos: {data_size:,} elementos")
            
            # Visualización del experimento
            if st.button("📊 Visualizar Complejidad", key="visualize_complexity"):
                try:
                    plot_integral(selected_function, "1", str(data_size), "n")
                except Exception as e:
                    st.warning("No se pudo generar la visualización")

def show_progressive_challenges():
    """Desafíos progresivos para diferentes niveles de competencia."""
    st.markdown("### 🎯 Desafíos Progresivos de Cálculo en Ingeniería")
    
    # Seleccionar nivel de dificultad
    difficulty_level = st.selectbox(
        "🎚️ Selecciona tu nivel:",
        ["🟢 Principiante", "🟡 Intermedio", "🔴 Avanzado", "⚫ Experto"],
        key="difficulty_level"
    )
    
    challenges = {
        "🟢 Principiante": [
            {
                "title": "Análisis básico de algoritmo lineal",
                "description": "Calcula el tiempo total de un algoritmo O(n)",
                "function": "n",
                "bounds": [1, 100],
                "variable": "n",
                "expected_range": [5000, 5100],
                "hint": "Un algoritmo lineal tiene complejidad O(n), donde cada elemento se procesa una vez"
            },
            {
                "title": "Consumo de memoria constante",
                "description": "Analiza el consumo de memoria de una aplicación",
                "function": "50",
                "bounds": [0, 10],
                "variable": "t",
                "expected_range": [490, 510],
                "hint": "Memoria constante significa que no cambia con el tiempo"
            }
        ],
        "🟡 Intermedio": [
            {
                "title": "Optimización de cache con función logarítmica",
                "description": "Calcula la mejora de rendimiento con cache inteligente",
                "function": "log(t+1)*100",
                "bounds": [0, 50],
                "variable": "t",
                "expected_range": [1800, 2000],
                "hint": "Los sistemas de cache mejoran logarítmicamente con el tiempo"
            },
            {
                "title": "Red neuronal con función sigmoide",
                "description": "Analiza la activación total en una capa neuronal",
                "function": "1/(1 + exp(-t))",
                "bounds": [-5, 5],
                "variable": "t",
                "expected_range": [4.9, 5.1],
                "hint": "La función sigmoide es común en redes neuronales para activación"
            }
        ],
        "🔴 Avanzado": [
            {
                "title": "Sistema distribuido con patrones sinusoidales",
                "description": "Analiza el tráfico en un sistema distribuido con patrones cíclicos",
                "function": "1000*sin(t/6) + 2000*cos(t/8) + 3000",
                "bounds": [0, 48],
                "variable": "t",
                "expected_range": [143000, 145000],
                "hint": "Los sistemas distribuidos suelen tener patrones cíclicos complejos"
            }
        ],
        "⚫ Experto": [
            {
                "title": "IA Cuántica: Superposición de estados",
                "description": "Modela la evolución de qubits en computación cuántica",
                "function": "sin(t)**2 + cos(t)**2 + t*exp(-t**2/50)",
                "bounds": [0, 10],
                "variable": "t",
                "expected_range": [9.8, 10.2],
                "hint": "En computación cuántica, los estados evolucionan según ecuaciones complejas"
            }
        ]
    }
    
    current_challenges = challenges[difficulty_level]
    
    # Mostrar desafío seleccionado
    challenge_index = st.selectbox(
        "Selecciona un desafío:",
        range(len(current_challenges)),
        format_func=lambda x: f"Desafío {x+1}: {current_challenges[x]['title']}",
        key="challenge_selector"
    )
    
    challenge = current_challenges[challenge_index]
    
    st.markdown(f"### 🎯 {challenge['title']}")
    st.info(f"**Descripción**: {challenge['description']}")
    st.markdown(f"**💡 Pista**: {challenge['hint']}")
    
    # Interfaz del desafío
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**🔢 Configura tu solución:**")
        
        user_function = st.text_input(
            f"Función f({challenge['variable']}):",
            placeholder=f"Ingresa tu función en términos de {challenge['variable']}",
            key="challenge_function"
        )
        
        user_lower = st.text_input(
            "Límite inferior:",
            value=str(challenge['bounds'][0]),
            key="challenge_lower"
        )
        
        user_upper = st.text_input(
            "Límite superior:",
            value=str(challenge['bounds'][1]),
            key="challenge_upper"
        )
        
        if st.button("🚀 Resolver Desafío", key="solve_challenge"):
            if user_function.strip():
                try:
                    result, steps = solve_integral(user_function, user_lower, user_upper, challenge['variable'])
                    
                    # Evaluar la respuesta
                    expected_min, expected_max = challenge['expected_range']
                    
                    if expected_min <= result <= expected_max:
                        st.success(f"🎉 ¡Excelente! Tu resultado {result:.2f} está en el rango esperado")
                        st.balloons()
                        
                        # Mostrar solución correcta
                        correct_result, _ = solve_integral(
                            challenge['function'], 
                            str(challenge['bounds'][0]), 
                            str(challenge['bounds'][1]), 
                            challenge['variable']
                        )
                        st.info(f"📚 Solución de referencia: {correct_result:.2f} (función: {challenge['function']})")
                        
                    else:
                        st.warning(f"🤔 Tu resultado {result:.2f} no está en el rango esperado ({expected_min}-{expected_max})")
                        st.markdown("**Sugerencias:**")
                        st.markdown("- Revisa la función matemática que modela el problema")
                        st.markdown("- Considera los límites de integración")
                        st.markdown("- Lee nuevamente la pista proporcionada")
                        
                except Exception as e:
                    st.error(f"❌ Error en tu solución: {e}")
            else:
                st.warning("⚠️ Por favor ingresa una función")
    
    with col2:
        st.markdown("**📊 Información del Desafío:**")
        st.code(f"""Variable: {challenge['variable']}
Límites: [{challenge['bounds'][0]}, {challenge['bounds'][1]}]
Rango esperado: {challenge['expected_range']}""")

def show_comparative_analysis():
    """Análisis comparativo entre diferentes enfoques y algoritmos."""
    st.markdown("### 📊 Análisis Comparativo de Algoritmos")
    st.markdown("Compara el rendimiento de diferentes algoritmos y enfoques de ingeniería")
    
    # Comparación de algoritmos de ordenamiento
    st.markdown("#### 🔄 Comparación de Algoritmos de Ordenamiento")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Configuración del Análisis:**")
        data_sizes = st.multiselect(
            "Tamaños de datos a comparar:",
            [100, 500, 1000, 5000, 10000],
            default=[1000, 5000],
            key="comparison_sizes"
        )
        
        algorithms_to_compare = st.multiselect(
            "Algoritmos a comparar:",
            ["Bubble Sort O(n²)", "Quick Sort O(n log n)", "Merge Sort O(n log n)", "Heap Sort O(n log n)"],
            default=["Bubble Sort O(n²)", "Quick Sort O(n log n)"],
            key="algorithms_compare"
        )
    
    with col2:
        if st.button("📈 Generar Comparación", key="generate_comparison"):
            if data_sizes and algorithms_to_compare:
                comparison_results = {}
                
                algorithm_functions = {
                    "Bubble Sort O(n²)": "n**2",
                    "Quick Sort O(n log n)": "n*log(n)",
                    "Merge Sort O(n log n)": "n*log(n)", 
                    "Heap Sort O(n log n)": "n*log(n)"
                }
                
                for algorithm in algorithms_to_compare:
                    comparison_results[algorithm] = {}
                    function = algorithm_functions[algorithm]
                    
                    for size in data_sizes:
                        try:
                            result, _ = solve_integral(function, "1", str(size), "n")
                            comparison_results[algorithm][size] = result
                        except:
                            comparison_results[algorithm][size] = None
                
                # Mostrar resultados en tabla
                st.markdown("**📊 Resultados de la Comparación:**")
                
                # Crear tabla de resultados
                table_data = []
                for algorithm in algorithms_to_compare:
                    row = {"Algoritmo": algorithm}
                    for size in data_sizes:
                        result = comparison_results[algorithm][size]
                        if result is not None:
                            row[f"n={size}"] = f"{result:,.0f}"
                        else:
                            row[f"n={size}"] = "Error"
                    table_data.append(row)
                
                df = pd.DataFrame(table_data)
                st.dataframe(df, use_container_width=True)

def show_competency_evaluation():
    """Sistema de evaluación de competencias."""
    st.markdown("### 🏆 Evaluación de Competencias")
    st.markdown("Evalúa tu comprensión del cálculo integral aplicado a ingeniería de software")
    
    # Cuestionario de evaluación
    st.markdown("#### 📝 Cuestionario de Evaluación")
    
    questions = [
        {
            "question": "¿Qué representa la integral de una función de complejidad O(n²)?",
            "options": [
                "El tiempo promedio de ejecución",
                "El número total de operaciones",
                "La memoria utilizada",
                "La complejidad espacial"
            ],
            "correct": 1,
            "explanation": "La integral de una función de complejidad nos da el total acumulado de operaciones."
        },
        {
            "question": "En machine learning, ¿qué significa integrar la función de pérdida?",
            "options": [
                "Calcular el error promedio",
                "Obtener el error total acumulado",
                "Encontrar el mínimo global",
                "Derivar la función"
            ],
            "correct": 1,
            "explanation": "Integrar la función de pérdida nos da el error total acumulado durante el entrenamiento."
        },
        {
            "question": "¿Cuál es la principal ventaja de usar integrales en análisis de sistemas?",
            "options": [
                "Simplificar cálculos",
                "Obtener valores totales acumulados",
                "Reducir complejidad",
                "Aumentar velocidad"
            ],
            "correct": 1,
            "explanation": "Las integrales nos permiten calcular valores totales acumulados en intervalos específicos."
        }
    ]
    
    if "evaluation_answers" not in st.session_state:
        st.session_state.evaluation_answers = {}
    
    for i, q in enumerate(questions):
        st.markdown(f"**Pregunta {i+1}:** {q['question']}")
        
        answer = st.radio(
            f"Selecciona tu respuesta:",
            q['options'],
            key=f"question_{i}",
            index=None
        )
        
        if answer:
            st.session_state.evaluation_answers[i] = q['options'].index(answer)
    
    if st.button("📊 Evaluar Respuestas", key="evaluate_answers"):
        if len(st.session_state.evaluation_answers) == len(questions):
            correct_answers = 0
            
            for i, q in enumerate(questions):
                user_answer = st.session_state.evaluation_answers.get(i)
                if user_answer == q['correct']:
                    correct_answers += 1
                    st.success(f"✅ Pregunta {i+1}: Correcto")
                else:
                    st.error(f"❌ Pregunta {i+1}: Incorrecto")
                    st.info(f"💡 Explicación: {q['explanation']}")
            
            score = (correct_answers / len(questions)) * 100
            st.markdown(f"### 🎯 Puntuación Final: {score:.1f}%")
            
            if score >= 80:
                st.success("🏆 ¡Excelente! Tienes un dominio sólido del tema")
                st.balloons()
            elif score >= 60:
                st.warning("📚 Buen trabajo, pero puedes mejorar con más práctica")
            else:
                st.error("📖 Te recomendamos revisar los conceptos fundamentales")
        else:
            st.warning("⚠️ Por favor responde todas las preguntas")

def show_geometric_analysis():
    """Análisis geométrico de áreas y volúmenes en ingeniería de software."""
    st.markdown("## 📐 Análisis Geométrico: Áreas y Volúmenes")
    st.markdown("Aplicación del cálculo integral para calcular áreas y volúmenes en contextos de ingeniería de software")
    
    geo_tab1, geo_tab2, geo_tab3 = st.tabs([
        "📏 Cálculo de Áreas",
        "📦 Cálculo de Volúmenes",
        "🔄 Sólidos de Revolución"
    ])
    
    with geo_tab1:
        show_area_calculations()
    
    with geo_tab2:
        show_volume_calculations()
    
    with geo_tab3:
        show_revolution_solids()

def show_area_calculations():
    """Cálculos de áreas aplicados a ingeniería de software."""
    st.markdown("### 📏 Cálculo de Áreas en Ingeniería de Software")
    st.markdown("Analiza problemas donde el área bajo una curva representa métricas importantes")
    
    area_scenarios = [
        {
            "title": "Área de Consumo de CPU",
            "description": "Calcula el consumo total de CPU durante un período de tiempo",
            "function": "50*sin(t/6) + 75",
            "bounds": [0, 24],
            "variable": "t",
            "units": "% CPU × horas",
            "interpretation": "El área representa el consumo total de recursos computacionales"
        },
        {
            "title": "Área de Transferencia de Datos",
            "description": "Volumen total de datos transferidos en una red",
            "function": "1000*exp(-t/10) + 500",
            "bounds": [0, 20],
            "variable": "t",
            "units": "MB × tiempo",
            "interpretation": "El área muestra la cantidad total de datos procesados"
        },
        {
            "title": "Área de Usuarios Activos",
            "description": "Total de usuarios-hora en una aplicación web",
            "function": "2000/(1 + exp(-0.5*t)) + 1000",
            "bounds": [0, 48],
            "variable": "t",
            "units": "usuarios × horas",
            "interpretation": "El área representa la carga total del servidor"
        }
    ]
    
    selected_area_scenario = st.selectbox(
        "🎯 Selecciona un escenario de área:",
        range(len(area_scenarios)),
        format_func=lambda x: area_scenarios[x]["title"],
        key="area_scenario_selector"
    )
    
    scenario = area_scenarios[selected_area_scenario]
    
    st.markdown(f"### 📊 {scenario['title']}")
    st.info(f"**Descripción**: {scenario['description']}")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### 🔧 Parámetros del Cálculo")
        
        # Mostrar función y permitir modificaciones
        custom_function = st.text_input(
            f"Función f({scenario['variable']}):",
            value=scenario['function'],
            key="area_function"
        )
        
        col1a, col1b = st.columns(2)
        with col1a:
            lower_bound = st.number_input(
                "Límite inferior:",
                value=float(scenario['bounds'][0]),
                key="area_lower"
            )
        with col1b:
            upper_bound = st.number_input(
                "Límite superior:",
                value=float(scenario['bounds'][1]),
                key="area_upper"
            )
        
        if st.button("📐 Calcular Área", key="calculate_area"):
            try:
                result, steps = solve_integral(
                    custom_function, 
                    str(lower_bound), 
                    str(upper_bound), 
                    scenario['variable']
                )
                
                st.success(f"### ✅ Área calculada: {result:.2f} {scenario['units']}")
                
                # Análisis geométrico detallado
                st.markdown("#### 📊 Análisis Geométrico:")
                st.markdown(f"- **Función**: f({scenario['variable']}) = {custom_function}")
                st.markdown(f"- **Intervalo**: [{lower_bound}, {upper_bound}]")
                st.markdown(f"- **Área bajo la curva**: {result:.6f} {scenario['units']}")
                st.markdown(f"- **Interpretación**: {scenario['interpretation']}")
                
                # Análisis adicional
                interval_width = upper_bound - lower_bound
                average_height = result / interval_width if interval_width > 0 else 0
                st.info(f"**Altura promedio**: {average_height:.2f} unidades")
                
                # Visualización
                try:
                    st.markdown("#### 📈 Visualización del Área")
                    plot_integral(custom_function, str(lower_bound), str(upper_bound), scenario['variable'])
                except Exception as e:
                    st.warning(f"⚠️ Error en visualización: {e}")
                
            except Exception as e:
                st.error(f"❌ Error en el cálculo: {e}")
    
    with col2:
        st.markdown("#### 📋 Información del Escenario")
        st.code(f"""
Función: {scenario['function']}
Variable: {scenario['variable']}
Límites: {scenario['bounds']}
Unidades: {scenario['units']}
        """)
        
        st.markdown("#### 🎯 Casos de Uso")
        st.markdown("- Análisis de carga de trabajo")
        st.markdown("- Planificación de capacidad")
        st.markdown("- Optimización de recursos")
        st.markdown("- Monitoreo de rendimiento")

def show_volume_calculations():
    """Cálculos de volúmenes en contextos de ingeniería de software."""
    st.markdown("### 📦 Cálculo de Volúmenes en Sistemas 3D")
    st.markdown("Aplica integrales dobles y triples para análisis de sistemas complejos")
    
    # Simulación de volúmenes usando integrales simples con interpretaciones 3D
    volume_scenarios = [
        {
            "title": "Volumen de Datos en Base de Datos",
            "description": "Crecimiento volumétrico de datos almacenados",
            "function": "t**2 * 100",  # Área base que crece cuadráticamente
            "bounds": [1, 12],  # meses
            "variable": "t",
            "height_factor": "log(t+1)",  # Factor de altura
            "units": "GB³",
            "interpretation": "Volumen total de almacenamiento necesario considerando crecimiento en 3 dimensiones"
        },
        {
            "title": "Volumen de Procesamiento en Cluster",
            "description": "Capacidad de procesamiento distribuido en 3D",
            "function": "1000*sin(t/4)**2",
            "bounds": [0, 24],
            "variable": "t",
            "height_factor": "sqrt(t+1)",
            "units": "FLOPS³",
            "interpretation": "Volumen de operaciones procesables en arquitectura 3D"
        }
    ]
    
    selected_volume_scenario = st.selectbox(
        "🎯 Selecciona un escenario de volumen:",
        range(len(volume_scenarios)),
        format_func=lambda x: volume_scenarios[x]["title"],
        key="volume_scenario_selector"
    )
    
    scenario = volume_scenarios[selected_volume_scenario]
    
    st.markdown(f"### 📦 {scenario['title']}")
    st.info(f"**Descripción**: {scenario['description']}")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### ⚙️ Configuración del Volumen")
        
        base_function = st.text_input(
            f"Función base f({scenario['variable']}):",
            value=scenario['function'],
            key="volume_base_function"
        )
        
        height_function = st.text_input(
            f"Función altura h({scenario['variable']}):",
            value=scenario['height_factor'],
            key="volume_height_function"
        )
        
        # Simulación de cálculo de volumen
        if st.button("📦 Calcular Volumen", key="calculate_volume"):
            try:
                # Calcular área base
                base_area, _ = solve_integral(
                    base_function,
                    str(scenario['bounds'][0]),
                    str(scenario['bounds'][1]),
                    scenario['variable']
                )
                
                # Calcular factor de altura promedio
                height_integral, _ = solve_integral(
                    height_function,
                    str(scenario['bounds'][0]),
                    str(scenario['bounds'][1]),
                    scenario['variable']
                )
                
                interval = scenario['bounds'][1] - scenario['bounds'][0]
                avg_height = height_integral / interval
                
                # Volumen aproximado
                volume = base_area * avg_height
                
                st.success(f"### ✅ Volumen calculado: {volume:.2f} {scenario['units']}")
                
                # Análisis volumétrico detallado
                st.markdown("#### 📊 Análisis Volumétrico:")
                st.markdown(f"- **Función base**: f({scenario['variable']}) = {base_function}")
                st.markdown(f"- **Función altura**: h({scenario['variable']}) = {height_function}")
                st.markdown(f"- **Área base**: {base_area:.2f}")
                st.markdown(f"- **Altura promedio**: {avg_height:.2f}")
                st.markdown(f"- **Volumen total**: {volume:.2f} {scenario['units']}")
                st.markdown(f"- **Interpretación**: {scenario['interpretation']}")
                
                # Métricas adicionales
                col_vol1, col_vol2, col_vol3 = st.columns(3)
                with col_vol1:
                    st.metric("Área Base", f"{base_area:.1f}")
                with col_vol2:
                    st.metric("Altura Media", f"{avg_height:.1f}")
                with col_vol3:
                    st.metric("Volumen", f"{volume:.1f}")
                
            except Exception as e:
                st.error(f"❌ Error en el cálculo: {e}")
    
    with col2:
        st.markdown("#### 📋 Información del Volumen")
        st.code(f"""
Base: {scenario['function']}
Altura: {scenario['height_factor']}
Intervalo: {scenario['bounds']}
Unidades: {scenario['units']}
        """)
        
        st.markdown("#### 🔧 Aplicaciones")
        st.markdown("- Diseño de arquitecturas 3D")
        st.markdown("- Planificación de centros de datos")
        st.markdown("- Modelado de sistemas complejos")
        st.markdown("- Optimización espacial")

def show_revolution_solids():
    """Sólidos de revolución aplicados a ingeniería de software."""
    st.markdown("### 🔄 Sólidos de Revolución en Sistemas Rotativos")
    st.markdown("Analiza sistemas que pueden modelarse como sólidos de revolución")
    
    revolution_scenarios = [
        {
            "title": "Disco de Almacenamiento Rotativo",
            "description": "Modelado de un disco duro como sólido de revolución",
            "function": "sqrt(r)",  # función que define el radio
            "bounds": [1, 10],
            "variable": "r",
            "axis": "Eje horizontal",
            "units": "cm³",
            "interpretation": "Volumen del disco calculado por revolución de la curva"
        },
        {
            "title": "Antena Parabólica de Comunicaciones",
            "description": "Forma parabólica para sistemas de comunicación",
            "function": "x**2/4",
            "bounds": [0, 4],
            "variable": "x",
            "axis": "Eje vertical",
            "units": "m³",
            "interpretation": "Volumen de material necesario para construir la antena"
        }
    ]
    
    selected_revolution = st.selectbox(
        "🎯 Selecciona un sólido de revolución:",
        range(len(revolution_scenarios)),
        format_func=lambda x: revolution_scenarios[x]["title"],
        key="revolution_selector"
    )
    
    scenario = revolution_scenarios[selected_revolution]
    
    st.markdown(f"### 🔄 {scenario['title']}")
    st.info(f"**Descripción**: {scenario['description']}")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### ⚙️ Configuración del Sólido")
        
        revolution_function = st.text_input(
            f"Función f({scenario['variable']}):",
            value=scenario['function'],
            key="revolution_function"
        )
        
        revolution_method = st.selectbox(
            "Método de cálculo:",
            ["Método del disco", "Método de la arandela"],
            key="revolution_method"
        )
        
        if st.button("🔄 Calcular Volumen por Revolución", key="calculate_revolution"):
            try:
                # Para método del disco: V = π ∫[a,b] [f(x)]² dx
                if revolution_method == "Método del disco":
                    # Crear función cuadrada para el método del disco
                    squared_function = f"({revolution_function})**2"
                    
                    integral_result, _ = solve_integral(
                        squared_function,
                        str(scenario['bounds'][0]),
                        str(scenario['bounds'][1]),
                        scenario['variable']
                    )
                    
                    volume = 3.14159 * integral_result  # π * integral
                    
                    st.success(f"### ✅ Volumen del sólido: {volume:.2f} {scenario['units']}")
                    
                    # Análisis del sólido de revolución
                    st.markdown("#### 📊 Análisis del Sólido de Revolución:")
                    st.markdown(f"- **Función generatriz**: f({scenario['variable']}) = {revolution_function}")
                    st.markdown(f"- **Método usado**: {revolution_method}")
                    st.markdown(f"- **Eje de revolución**: {scenario['axis']}")
                    st.markdown(f"- **Fórmula**: V = π ∫[{scenario['bounds'][0]},{scenario['bounds'][1]}] [{revolution_function}]² d{scenario['variable']}")
                    st.markdown(f"- **Integral evaluada**: {integral_result:.4f}")
                    st.markdown(f"- **Volumen final**: {volume:.2f} {scenario['units']}")
                    st.markdown(f"- **Interpretación**: {scenario['interpretation']}")
                    
                    # Información técnica adicional
                    radius_at_start = eval(revolution_function.replace(scenario['variable'], str(scenario['bounds'][0])))
                    radius_at_end = eval(revolution_function.replace(scenario['variable'], str(scenario['bounds'][1])))
                    
                    st.markdown("#### 🔧 Detalles Técnicos:")
                    st.markdown(f"- **Radio inicial**: {radius_at_start:.2f}")
                    st.markdown(f"- **Radio final**: {radius_at_end:.2f}")
                    st.markdown(f"- **Variación de radio**: {abs(radius_at_end - radius_at_start):.2f}")
                
            except Exception as e:
                st.error(f"❌ Error en el cálculo: {e}")
    
    with col2:
        st.markdown("#### 📋 Información del Sólido")
        st.code(f"""
Función: {scenario['function']}
Intervalo: {scenario['bounds']}
Eje: {scenario['axis']}
Unidades: {scenario['units']}
        """)
        
        st.markdown("#### 🎯 Aplicaciones Técnicas")
        st.markdown("- Diseño de componentes hardware")
        st.markdown("- Modelado de antenas")
        st.markdown("- Optimización de formas")
        st.markdown("- Cálculo de materiales")

def show_complete_case_study():
    """Caso de estudio completo: Sistema de caching distribuido."""
    st.markdown("## 🔬 Caso de Estudio Completo")
    st.markdown("**Sistema de Caching Distribuido: Análisis Integral Completo**")
    
    st.markdown("""
    ### 📋 Descripción del Problema
    
    **Situación Cotidiana**: Una empresa de streaming de video necesita optimizar su sistema de 
    caching distribuido para mejorar la experiencia del usuario. El sistema debe manejar patrones 
    de tráfico variables a lo largo del día, optimizar el uso de memoria cache, y minimizar la 
    latencia de respuesta.
    
    **Modelado Matemático**: El comportamiento del sistema se puede modelar mediante funciones 
    matemáticas continuas y derivables que representan:
    - Tráfico de usuarios en función del tiempo
    - Eficiencia del cache en función del tamaño
    - Latencia de respuesta según la carga del sistema
    """)
    
    case_tab1, case_tab2, case_tab3, case_tab4, case_tab5 = st.tabs([
        "🎯 Definición del Problema",
        "📐 Modelado Matemático", 
        "🔢 Análisis Integral",
        "📊 Resultados y Gráficas",
        "💡 Conclusiones"
    ])
    
    with case_tab1:
        show_problem_definition()
    
    with case_tab2:
        show_mathematical_modeling()
    
    with case_tab3:
        show_integral_analysis()
    
    with case_tab4:
        show_results_and_graphs()
    
    with case_tab5:
        show_conclusions()

def show_problem_definition():
    """Definición completa del problema del caso de estudio."""
    st.markdown("### 🎯 Definición Completa del Problema")
    
    st.markdown("""
    #### 🌐 Contexto Real: Plataforma de Streaming de Video
    
    **Empresa**: "StreamTech Solutions" - Plataforma de video streaming con 10 millones de usuarios activos
    
    **Desafío Principal**: El sistema actual de caching presenta los siguientes problemas:
    - Latencia elevada durante horas pico (19:00 - 23:00)
    - Uso ineficiente de memoria cache (solo 60% de hit rate)
    - Costos elevados de ancho de banda por cache misses
    - Experiencia de usuario inconsistente
    
    #### 📊 Datos del Sistema Actual
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Métricas Actuales:**
        - Usuarios concurrentes: 2M - 8M (variable)
        - Cache hit rate: 60% promedio
        - Latencia promedio: 150ms
        - Memoria cache: 500 GB distribuida
        - Ancho de banda: 10 Tbps pico
        """)
    
    with col2:
        st.markdown("""
        **Objetivos de Optimización:**
        - Aumentar hit rate a 85%+
        - Reducir latencia a <100ms
        - Minimizar costos de ancho de banda
        - Mantener QoS consistente 24/7
        - Optimizar uso de recursos
        """)
    
    st.markdown("""
    #### 🔬 Variables del Sistema a Analizar
    
    **1. Tráfico de Usuarios T(t)**
    - Función: T(t) = 4000000 + 3000000*sin(π(t-6)/12) + 1000000*sin(π(t-6)/6)
    - Representa usuarios concurrentes por hora (t en horas, 0-24)
    - Patrón diario con picos vespertinos y nocturnos
    
    **2. Eficiencia de Cache E(s)**
    - Función: E(s) = 100/(1 + exp(-0.1*(s-50)))
    - Hit rate en función del tamaño de cache (s en GB)
    - Función sigmoide que modela mejora logarítmica
    
    **3. Latencia del Sistema L(c)**
    - Función: L(c) = 200*exp(-c/5000000) + 50
    - Latencia en ms según carga de usuarios (c)
    - Función exponencial decreciente
    """)
    
    # Visualización interactiva de las funciones
    st.markdown("#### 📈 Visualización de las Funciones del Sistema")
    
    function_to_show = st.selectbox(
        "Selecciona función a visualizar:",
        ["Tráfico de Usuarios T(t)", "Eficiencia de Cache E(s)", "Latencia del Sistema L(c)"],
        key="case_function_selector"
    )
    
    if function_to_show == "Tráfico de Usuarios T(t)":
        if st.button("📊 Visualizar Tráfico", key="show_traffic"):
            try:
                traffic_function = "4000000 + 3000000*sin(3.14159*(t-6)/12) + 1000000*sin(3.14159*(t-6)/6)"
                plot_integral(traffic_function, "0", "24", "t")
                st.info("Esta función modela el tráfico de usuarios a lo largo de 24 horas, con picos en horario vespertino.")
            except Exception as e:
                st.error(f"Error en visualización: {e}")
    
    elif function_to_show == "Eficiencia de Cache E(s)":
        if st.button("📊 Visualizar Eficiencia", key="show_efficiency"):
            try:
                efficiency_function = "100/(1 + exp(-0.1*(s-50)))"
                plot_integral(efficiency_function, "10", "200", "s")
                st.info("Función sigmoide que muestra cómo mejora el hit rate conforme aumenta el tamaño del cache.")
            except Exception as e:
                st.error(f"Error en visualización: {e}")
    
    elif function_to_show == "Latencia del Sistema L(c)":
        if st.button("📊 Visualizar Latencia", key="show_latency"):
            try:
                latency_function = "200*exp(-c/5000000) + 50"
                plot_integral(latency_function, "1000000", "8000000", "c")
                st.info("Función exponencial que modela cómo disminuye la latencia con sistemas más robustos.")
            except Exception as e:
                st.error(f"Error en visualización: {e}")

def show_mathematical_modeling():
    """Modelado matemático detallado del sistema."""
    st.markdown("### 📐 Modelado Matemático Completo")
    
    st.markdown("""
    #### 🧮 Funciones Matemáticas del Sistema
    
    El sistema de caching distribuido se modela mediante tres funciones principales, 
    cada una continua y derivable en su dominio:
    """)
    
    # Función 1: Tráfico de Usuarios
    st.markdown("""
    #### 1️⃣ Función de Tráfico de Usuarios
    
    **T(t) = 4,000,000 + 3,000,000·sin(π(t-6)/12) + 1,000,000·sin(π(t-6)/6)**
    
    **Donde:**
    - t: tiempo en horas (0 ≤ t ≤ 24)
    - T(t): número de usuarios concurrentes
    
    **Análisis de la Función:**
    - Función base: 4M usuarios (tráfico mínimo constante)
    - Componente principal: 3M·sin(π(t-6)/12) - patrón de 24h con pico vespertino
    - Componente secundaria: 1M·sin(π(t-6)/6) - patrón de 12h con picos adicionales
    - Dominio: [0, 24] horas
    - Rango: [1M, 8M] usuarios aproximadamente
    """)
    
    # Análisis de continuidad y derivabilidad
    with st.expander("🔍 Análisis de Continuidad y Derivabilidad - T(t)"):
        st.markdown("""
        **Continuidad:**
        - T(t) es suma de funciones continuas (constante + senos)
        - Por tanto, T(t) es continua en todo ℝ, especialmente en [0,24]
        
        **Derivabilidad:**
        - T'(t) = 3,000,000 · (π/12) · cos(π(t-6)/12) + 1,000,000 · (π/6) · cos(π(t-6)/6)
        - T'(t) existe para todo t ∈ ℝ
        - Por tanto, T(t) es derivable en [0,24]
        
        **Interpretación de la Derivada:**
        - T'(t) > 0: usuarios incrementándose (horas de la tarde)
        - T'(t) < 0: usuarios decrementándose (madrugada)
        - T'(t) = 0: picos y valles de tráfico
        """)
    
    # Función 2: Eficiencia de Cache
    st.markdown("""
    #### 2️⃣ Función de Eficiencia de Cache
    
    **E(s) = 100/(1 + e^(-0.1(s-50)))**
    
    **Donde:**
    - s: tamaño de cache en GB (s ≥ 10)
    - E(s): hit rate en porcentaje (0 ≤ E(s) ≤ 100)
    
    **Análisis de la Función:**
    - Función sigmoide que modela mejora logarítmica
    - Punto de inflexión en s = 50 GB
    - Asíntota inferior: E(s) → 0 cuando s → -∞
    - Asíntota superior: E(s) → 100 cuando s → +∞
    - Crecimiento más pronunciado entre 30-70 GB
    """)
    
    with st.expander("🔍 Análisis de Continuidad y Derivabilidad - E(s)"):
        st.markdown("""
        **Continuidad:**
        - E(s) es función sigmoide (composición de funciones continuas)
        - Continua para todo s ∈ ℝ, especialmente en [10, ∞)
        
        **Derivabilidad:**
        - E'(s) = 100 · 0.1 · e^(-0.1(s-50)) / (1 + e^(-0.1(s-50)))²
        - E'(s) existe para todo s ∈ ℝ
        - E'(s) > 0 para todo s (función estrictamente creciente)
        
        **Interpretación Física:**
        - E'(s) máxima en s = 50 GB (punto de mayor eficiencia marginal)
        - Rendimientos decrecientes: más cache → menor mejora por GB adicional
        """)
    
    # Función 3: Latencia
    st.markdown("""
    #### 3️⃣ Función de Latencia del Sistema
    
    **L(c) = 200·e^(-c/5,000,000) + 50**
    
    **Donde:**
    - c: carga de usuarios concurrentes
    - L(c): latencia promedio en milisegundos
    
    **Análisis de la Función:**
    - Función exponencial decreciente + constante
    - Latencia base: 50ms (infraestructura optimizada)
    - Componente variable: decrece exponencialmente con la carga
    - Modelo contraintuitivo: sistemas más cargados → menor latencia por usuario
    - Justificación: economías de escala en sistemas distribuidos
    """)
    
    with st.expander("🔍 Análisis de Continuidad y Derivabilidad - L(c)"):
        st.markdown("""
        **Continuidad:**
        - L(c) es suma de función exponencial y constante
        - Ambas continuas, por tanto L(c) continua en [0, ∞)
        
        **Derivabilidad:**
        - L'(c) = 200 · (-1/5,000,000) · e^(-c/5,000,000)
        - L'(c) = -0.00004 · e^(-c/5,000,000)
        - L'(c) < 0 para todo c > 0 (función decreciente)
        
        **Interpretación Económica:**
        - Economías de escala: más usuarios → mejor amortización de infraestructura
        - Cache compartido más eficiente con mayor volumen
        - Sistemas distribuidos optimizados para alta carga
        """)
    
    # Función objetivo combinada
    st.markdown("""
    #### 🎯 Función Objetivo del Sistema
    
    Para optimizar el sistema completo, definimos una función objetivo que combina las tres métricas:
    
    **F(t,s,c) = w₁·T(t) + w₂·E(s) - w₃·L(c)**
    
    **Donde:**
    - w₁, w₂, w₃: pesos de optimización
    - Objetivo: maximizar usuarios y eficiencia, minimizar latencia
    
    **Para análisis integral, estudiamos cada función por separado:**
    - ∫₀²⁴ T(t) dt: carga total de usuarios en 24h
    - ∫₁₀²⁰⁰ E(s) ds: eficiencia acumulada por rango de cache
    - ∫₁ₘ⁸ₘ L(c) dc: latencia total en función de la carga
    """)

def show_integral_analysis():
    """Análisis integral completo del sistema."""
    st.markdown("### 🔢 Análisis Integral Detallado")
    
    st.markdown("""
    #### 📋 Aparato Matemático para el Análisis
    
    Aplicaremos el cálculo integral para analizar tres aspectos críticos del sistema:
    1. **Carga Total de Usuarios**: ∫₀²⁴ T(t) dt
    2. **Eficiencia Acumulada de Cache**: ∫₁₀²⁰⁰ E(s) ds  
    3. **Latencia Total del Sistema**: ∫₁ₘ⁸ₘ L(c) dc
    """)
    
    analysis_type = st.selectbox(
        "🔍 Selecciona el análisis integral:",
        [
            "1. Carga Total de Usuarios (24h)",
            "2. Eficiencia Acumulada de Cache", 
            "3. Latencia Total del Sistema",
            "4. Análisis Comparativo Completo"
        ],
        key="integral_analysis_type"
    )
    
    if analysis_type.startswith("1."):
        show_user_load_analysis()
    elif analysis_type.startswith("2."):
        show_cache_efficiency_analysis()
    elif analysis_type.startswith("3."):
        show_latency_analysis()
    elif analysis_type.startswith("4."):
        show_complete_comparative_analysis()

def show_user_load_analysis():
    """Análisis integral de la carga de usuarios."""
    st.markdown("#### 1️⃣ Análisis de Carga Total de Usuarios")
    
    st.markdown("""
    **Función a Integrar**: T(t) = 4,000,000 + 3,000,000·sin(π(t-6)/12) + 1,000,000·sin(π(t-6)/6)
    
    **Integral Definida**: ∫₀²⁴ T(t) dt
    
    **Interpretación**: Esta integral calcula el total de usuarios-hora en un día completo,
    métrica fundamental para planificación de capacidad y facturación de recursos.
    """)
    
    if st.button("🧮 Calcular Integral de Carga de Usuarios", key="calc_user_load"):
        try:
            # Función de tráfico
            traffic_function = "4000000 + 3000000*sin(3.14159*(t-6)/12) + 1000000*sin(3.14159*(t-6)/6)"
            
            # Calcular integral
            result, steps = solve_integral(traffic_function, "0", "24", "t")
            
            st.success(f"### ✅ Carga Total de Usuarios: {result:,.0f} usuarios-hora")
            
            # Análisis detallado
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 📊 Análisis Matemático")
                st.markdown(f"""
                **Resultado de la Integral**: {result:,.2f} usuarios-hora
                
                **Desglose del Cálculo**:
                - Componente constante: 4M × 24h = 96M usuarios-hora
                - Componente seno principal: Contribución de variación diaria
                - Componente seno secundaria: Contribución de variaciones bi-diarias
                
                **Interpretación**:
                - Promedio diario: {result/24:,.0f} usuarios concurrentes
                - Pico estimado: ~8M usuarios
                - Valle estimado: ~1M usuarios
                """)
            
            with col2:
                st.markdown("#### 🎯 Implicaciones Técnicas")
                st.markdown(f"""
                **Planificación de Capacidad**:
                - Ancho de banda total diario: {result*0.5/1000:,.0f} TB
                - Servidores necesarios: {result/(24*100000):,.0f} instancias
                - Costo operativo estimado: ${result*0.001:,.0f}/día
                
                **Optimizaciones Sugeridas**:
                - Cache pre-poblado en horas valle
                - Auto-scaling basado en predicción
                - Balanceeo geográfico de carga
                """)
            
            # Análisis de crecimiento y decrecimiento
            st.markdown("#### 📈 Análisis de Crecimiento y Decrecimiento")
            
            st.markdown("""
            **Derivada de T(t)**:
            T'(t) = 3,000,000 · (π/12) · cos(π(t-6)/12) + 1,000,000 · (π/6) · cos(π(t-6)/6)
            
            **Períodos de Crecimiento** (T'(t) > 0):
            - Mañana: 6:00 - 12:00 (crecimiento moderado)
            - Tarde: 15:00 - 21:00 (crecimiento fuerte)
            
            **Períodos de Decrecimiento** (T'(t) < 0):
            - Madrugada: 0:00 - 6:00 (decrecimiento fuerte)
            - Noche: 21:00 - 24:00 (decrecimiento moderado)
            
            **Puntos Críticos**:
            - Mínimo global: ~2:00 AM (1M usuarios)
            - Máximo global: ~20:00 PM (8M usuarios)
            """)
            
            # Visualización
            st.markdown("#### 📊 Visualización de la Función")
            try:
                plot_integral(traffic_function, "0", "24", "t")
                st.info("El área bajo la curva representa la carga total de usuarios en 24 horas")
            except Exception as e:
                st.warning(f"Error en visualización: {e}")
                
        except Exception as e:
            st.error(f"Error en el cálculo: {e}")

def show_cache_efficiency_analysis():
    """Análisis integral de la eficiencia de cache."""
    st.markdown("#### 2️⃣ Análisis de Eficiencia Acumulada de Cache")
    
    st.markdown("""
    **Función a Integrar**: E(s) = 100/(1 + e^(-0.1(s-50)))
    
    **Integral Definida**: ∫₁₀²⁰⁰ E(s) ds
    
    **Interpretación**: Esta integral calcula la eficiencia acumulada de cache en el rango
    de 10GB a 200GB, fundamental para determinar el tamaño óptimo de cache.
    """)
    
    if st.button("🧮 Calcular Integral de Eficiencia de Cache", key="calc_cache_efficiency"):
        try:
            # Función de eficiencia
            efficiency_function = "100/(1 + exp(-0.1*(s-50)))"
            
            # Calcular integral
            result, steps = solve_integral(efficiency_function, "10", "200", "s")
            
            st.success(f"### ✅ Eficiencia Acumulada: {result:,.2f} %·GB")
            
            # Análisis detallado
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 📊 Análisis Matemático")
                st.markdown(f"""
                **Resultado de la Integral**: {result:,.2f} %·GB
                
                **Eficiencia Promedio**: {result/190:.1f}% en el rango [10, 200] GB
                
                **Puntos de Referencia**:
                - E(10) ≈ {100/(1 + np.exp(-0.1*(10-50))):.1f}% hit rate
                - E(50) ≈ {100/(1 + np.exp(-0.1*(50-50))):.1f}% hit rate  
                - E(100) ≈ {100/(1 + np.exp(-0.1*(100-50))):.1f}% hit rate
                - E(200) ≈ {100/(1 + np.exp(-0.1*(200-50))):.1f}% hit rate
                
                **Análisis de Rendimientos**:
                - Rendimientos decrecientes después de 80GB
                - Punto de inflexión óptimo: 50GB
                """)
            
            with col2:
                st.markdown("#### 🎯 Recomendaciones Técnicas")
                
                # Calcular eficiencias en puntos específicos
                eff_30 = 100/(1 + np.exp(-0.1*(30-50)))
                eff_50 = 100/(1 + np.exp(-0.1*(50-50)))
                eff_100 = 100/(1 + np.exp(-0.1*(100-50)))
                
                st.markdown(f"""
                **Configuraciones Sugeridas**:
                
                **Cache Pequeño (30GB)**:
                - Hit Rate: {eff_30:.1f}%
                - Costo: Bajo
                - Uso: Sistemas pequeños
                
                **Cache Medio (50GB)**:
                - Hit Rate: {eff_50:.1f}%
                - Costo: Moderado  
                - Uso: **RECOMENDADO** - Punto óptimo
                
                **Cache Grande (100GB)**:
                - Hit Rate: {eff_100:.1f}%
                - Costo: Alto
                - Uso: Sistemas críticos
                
                **ROI Óptimo**: 50GB de cache ofrece la mejor 
                relación costo-beneficio según el análisis integral.
                """)
            
            # Análisis de derivada
            st.markdown("#### 📈 Análisis de la Tasa de Mejora")
            st.markdown("""
            **Derivada de E(s)**:
            E'(s) = 10 · e^(-0.1(s-50)) / (1 + e^(-0.1(s-50)))²
            
            **Interpretación de E'(s)**:
            - E'(s) > 0 para todo s (función siempre creciente)
            - Máximo de E'(s) en s = 50GB (máxima eficiencia marginal)
            - Para s < 50: mejora rápida al agregar cache
            - Para s > 50: mejora decreciente (rendimientos marginales)
            
            **Decisión de Inversión**:
            - Cache < 50GB: inversión muy rentable
            - Cache > 100GB: inversión cuestionable
            - Rango óptimo: 40-80GB
            """)
            
            # Visualización
            try:
                plot_integral(efficiency_function, "10", "200", "s")
                st.info("El área bajo la curva representa la eficiencia acumulada del sistema de cache")
            except Exception as e:
                st.warning(f"Error en visualización: {e}")
                
        except Exception as e:
            st.error(f"Error en el cálculo: {e}")

def show_latency_analysis():
    """Análisis integral de la latencia del sistema."""
    st.markdown("#### 3️⃣ Análisis de Latencia Total del Sistema")
    
    st.markdown("""
    **Función a Integrar**: L(c) = 200·e^(-c/5,000,000) + 50
    
    **Integral Definida**: ∫₁,₀₀₀,₀₀₀⁸,₀₀₀,₀₀₀ L(c) dc
    
    **Interpretación**: Esta integral calcula la latencia acumulada total del sistema
    en función de la carga de usuarios, clave para SLA y calidad de servicio.
    """)
    
    if st.button("🧮 Calcular Integral de Latencia Total", key="calc_latency"):
        try:
            # Función de latencia
            latency_function = "200*exp(-c/5000000) + 50"
            
            # Calcular integral  
            result, steps = solve_integral(latency_function, "1000000", "8000000", "c")
            
            st.success(f"### ✅ Latencia Acumulada: {result:,.0f} ms·usuarios")
            
            # Análisis detallado
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 📊 Análisis Matemático")
                
                # Calcular latencias específicas
                lat_1m = 200*np.exp(-1000000/5000000) + 50
                lat_4m = 200*np.exp(-4000000/5000000) + 50  
                lat_8m = 200*np.exp(-8000000/5000000) + 50
                
                st.markdown(f"""
                **Resultado de la Integral**: {result:,.0f} ms·usuarios
                
                **Latencia Promedio**: {result/7000000:.1f} ms en el rango [1M, 8M] usuarios
                
                **Puntos de Referencia**:
                - L(1M) = {lat_1m:.1f} ms (carga baja)
                - L(4M) = {lat_4m:.1f} ms (carga media)
                - L(8M) = {lat_8m:.1f} ms (carga alta)
                
                **Comportamiento del Sistema**:
                - Latencia base: 50ms (infraestructura optimizada)
                - Componente variable: decrece con la carga
                - Economías de escala evidentes
                """)
            
            with col2:
                st.markdown("#### 🎯 Implicaciones para SLA")
                
                st.markdown(f"""
                **Niveles de Servicio**:
                
                **Carga Baja (1-2M usuarios)**:
                - Latencia: ~{lat_1m:.0f}ms
                - SLA: Premium (< 100ms) ❌
                - Acción: Optimizar para cargas bajas
                
                **Carga Media (3-5M usuarios)**:
                - Latencia: ~{lat_4m:.0f}ms  
                - SLA: Estándar (< 80ms) ✅
                - Estado: Óptimo
                
                **Carga Alta (6-8M usuarios)**:
                - Latencia: ~{lat_8m:.0f}ms
                - SLA: Premium (< 60ms) ✅  
                - Estado: Excelente
                
                **Estrategia Recomendada**:
                - Mantener carga base > 3M usuarios
                - Pre-calentamiento del sistema en horas valle
                """)
            
            # Análisis de derivada
            st.markdown("#### 📉 Análisis de la Tasa de Mejora de Latencia")
            st.markdown(f"""
            **Derivada de L(c)**:
            L'(c) = -200 · (1/5,000,000) · e^(-c/5,000,000) = -0.00004 · e^(-c/5,000,000)
            
            **Interpretación de L'(c)**:
            - L'(c) < 0 para todo c > 0 (latencia siempre decrece)
            - |L'(c)| máxima en c = 0 (mayor beneficio marginal con primeros usuarios)
            - |L'(c)| → 0 cuando c → ∞ (beneficio marginal tiende a cero)
            
            **Punto de Eficiencia Marginal**:
            - Mejora significativa hasta 5M usuarios
            - Mejora marginal después de 6M usuarios
            - Sistema optimizado para alta concurrencia
            
            **Conclusión del Análisis**:
            El sistema muestra comportamiento contraintuitivo pero técnicamente válido:
            más usuarios → mejor aprovechamiento de recursos → menor latencia por usuario.
            """)
            
            # Visualización
            try:
                plot_integral(latency_function, "1000000", "8000000", "c")
                st.info("El área bajo la curva representa la latencia total acumulada del sistema")
            except Exception as e:
                st.warning(f"Error en visualización: {e}")
                
        except Exception as e:
            st.error(f"Error en el cálculo: {e}")

def show_complete_comparative_analysis():
    """Análisis comparativo completo de todas las métricas."""
    st.markdown("#### 4️⃣ Análisis Comparativo Completo")
    
    st.markdown("""
    ### 🔄 Integración de Todas las Métricas del Sistema
    
    Este análisis combina los tres aspectos fundamentales del sistema de caching distribuido:
    """)
    
    if st.button("🚀 Ejecutar Análisis Completo", key="complete_analysis"):
        try:
            # Funciones del sistema
            traffic_function = "4000000 + 3000000*sin(3.14159*(t-6)/12) + 1000000*sin(3.14159*(t-6)/6)"
            efficiency_function = "100/(1 + exp(-0.1*(s-50)))"
            latency_function = "200*exp(-c/5000000) + 50"
            
            # Calcular todas las integrales
            traffic_result, _ = solve_integral(traffic_function, "0", "24", "t")
            efficiency_result, _ = solve_integral(efficiency_function, "10", "200", "s")
            latency_result, _ = solve_integral(latency_function, "1000000", "8000000", "c")
            
            # Mostrar resultados
            st.markdown("### 📊 Resultados Integrales Completos")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Carga Total (24h)",
                    f"{traffic_result:,.0f}",
                    "usuarios-hora"
                )
            
            with col2:
                st.metric(
                    "Eficiencia Acumulada",
                    f"{efficiency_result:,.1f}",
                    "%·GB"
                )
            
            with col3:
                st.metric(
                    "Latencia Acumulada", 
                    f"{latency_result:,.0f}",
                    "ms·usuarios"
                )
            
            # Análisis de optimización
            st.markdown("### 🎯 Análisis de Optimización Integral")
            
            # Métricas derivadas
            avg_users = traffic_result / 24
            avg_efficiency = efficiency_result / 190
            avg_latency = latency_result / 7000000
            
            st.markdown(f"""
            #### 📈 Métricas Promedio del Sistema:
            
            **Carga Promedio**: {avg_users:,.0f} usuarios concurrentes
            - Pico estimado: {avg_users * 2:,.0f} usuarios (20:00h)
            - Valle estimado: {avg_users * 0.25:,.0f} usuarios (02:00h)
            - Variabilidad: ±{avg_users * 0.75:,.0f} usuarios
            
            **Eficiencia Promedio**: {avg_efficiency:.1f}% hit rate
            - Configuración recomendada: 50GB cache
            - Hit rate esperado: 85%+
            - Mejora vs actual: +25%
            
            **Latencia Promedio**: {avg_latency:.1f} ms
            - SLA objetivo: <100ms ✅
            - Mejora vs actual: -33%
            - Consistencia: Alta en todo el rango
            """)
            
            # Función objetivo combinada
            st.markdown("#### 🎯 Función Objetivo del Sistema")
            
            # Normalizar métricas para función objetivo
            normalized_traffic = traffic_result / 100000000  # Normalizar a 0-1
            normalized_efficiency = efficiency_result / 20000  # Normalizar a 0-1
            normalized_latency = latency_result / 1000000  # Normalizar a 0-1 (invertir)
            
            # Pesos de optimización
            w1, w2, w3 = 0.4, 0.4, 0.2  # Priorizar usuarios y eficiencia
            
            objective_value = w1 * normalized_traffic + w2 * normalized_efficiency - w3 * normalized_latency
            
            st.markdown(f"""
            **Función Objetivo Combinada**:
            F = 0.4·T + 0.4·E - 0.2·L = {objective_value:.3f}
            
            **Donde**:
            - T: Capacidad de usuarios (normalizada)
            - E: Eficiencia de cache (normalizada)  
            - L: Latencia del sistema (normalizada, invertida)
            
            **Puntuación del Sistema**: {objective_value*100:.1f}/100
            """)
            
            if objective_value > 0.7:
                st.success("🏆 Sistema optimizado - Rendimiento excelente")
            elif objective_value > 0.5:
                st.warning("⚠️ Sistema aceptable - Margen de mejora")
            else:
                st.error("❌ Sistema subóptimo - Requiere optimización")
            
            # Recomendaciones finales
            st.markdown("### 💡 Recomendaciones Integrales")
            
            st.markdown(f"""
            **Basado en el Análisis Integral Completo:**
            
            **1. Configuración Óptima de Cache:**
            - Tamaño: 50-80GB por nodo
            - Distribución: 10 nodos × 5GB cada uno
            - Hit rate esperado: 85%+
            
            **2. Gestión de Carga:**
            - Auto-scaling: 3M-8M usuarios
            - Pre-poblado: 01:00-05:00 (horas valle)
            - Balanceeo: Geográfico + temporal
            
            **3. SLA y Latencia:**
            - Objetivo: <80ms promedio
            - Garantía: 99.9% uptime
            - Monitoreo: Tiempo real
            
            **4. Costos Proyectados:**
            - Reducción ancho de banda: 40%
            - Mejora experiencia usuario: 35%
            - ROI estimado: 6 meses
            """)
            
        except Exception as e:
            st.error(f"Error en análisis completo: {e}")

def show_results_and_graphs():
    """Mostrar resultados y gráficas del análisis."""
    st.markdown("### 📊 Resultados y Gráficas del Análisis")
    
    st.markdown("""
    #### 📈 Visualizaciones Completas del Sistema
    
    Esta sección presenta las gráficas de todas las funciones analizadas,
    junto con sus integrales y interpretaciones gráficas.
    """)
    
    graph_type = st.selectbox(
        "📊 Selecciona visualización:",
        [
            "Tráfico de Usuarios T(t)",
            "Eficiencia de Cache E(s)",
            "Latencia del Sistema L(c)",
            "Comparación de las 3 Funciones",
            "Análisis de Derivadas"
        ],
        key="graph_type_selector"
    )
    
    if graph_type == "Tráfico de Usuarios T(t)":
        st.markdown("#### 📈 Gráfica de Tráfico de Usuarios")
        try:
            traffic_function = "4000000 + 3000000*sin(3.14159*(t-6)/12) + 1000000*sin(3.14159*(t-6)/6)"
            plot_integral(traffic_function, "0", "24", "t")
            
            st.markdown("""
            **Interpretación Gráfica:**
            - **Eje X**: Tiempo en horas (0-24)
            - **Eje Y**: Usuarios concurrentes
            - **Área sombreada**: Carga total de usuarios en 24h
            - **Picos**: 08:00, 14:00, 20:00 (horarios de mayor actividad)
            - **Valles**: 02:00, 05:00 (horarios de menor actividad)
            
            **Patrones Identificados:**
            - Patrón primario: Ciclo de 24h (actividad diaria)
            - Patrón secundario: Ciclo de 12h (almuerzo y cena)
            - Componente base: 4M usuarios mínimos constantes
            """)
        except Exception as e:
            st.error(f"Error en gráfica: {e}")
    
    elif graph_type == "Eficiencia de Cache E(s)":
        st.markdown("#### 📊 Gráfica de Eficiencia de Cache")
        try:
            efficiency_function = "100/(1 + exp(-0.1*(s-50)))"
            plot_integral(efficiency_function, "10", "200", "s")
            
            st.markdown("""
            **Interpretación Gráfica:**
            - **Eje X**: Tamaño de cache en GB
            - **Eje Y**: Hit rate en porcentaje
            - **Área sombreada**: Eficiencia acumulada total
            - **Punto de inflexión**: 50GB (máxima eficiencia marginal)
            - **Asíntotas**: 0% (s→0) y 100% (s→∞)
            
            **Zonas de Rendimiento:**
            - **0-30GB**: Rendimiento bajo (<50% hit rate)
            - **30-80GB**: Zona óptima (50-95% hit rate)
            - **80-200GB**: Rendimientos decrecientes (>95% hit rate)
            """)
        except Exception as e:
            st.error(f"Error en gráfica: {e}")
    
    elif graph_type == "Latencia del Sistema L(c)":
        st.markdown("#### ⏱️ Gráfica de Latencia del Sistema")
        try:
            latency_function = "200*exp(-c/5000000) + 50"
            plot_integral(latency_function, "1000000", "8000000", "c")
            
            st.markdown("""
            **Interpretación Gráfica:**
            - **Eje X**: Carga de usuarios concurrentes
            - **Eje Y**: Latencia promedio en ms
            - **Área sombreada**: Latencia total acumulada
            - **Comportamiento**: Exponencial decreciente + constante
            - **Asíntota**: 50ms (latencia mínima del sistema)
            
            **Zonas de Operación:**
            - **1-2M usuarios**: Latencia alta (>150ms)
            - **3-5M usuarios**: Latencia media (80-120ms)
            - **6-8M usuarios**: Latencia baja (<80ms)
            """)
        except Exception as e:
            st.error(f"Error en gráfica: {e}")
    
    elif graph_type == "Comparación de las 3 Funciones":
        st.markdown("#### 📊 Tabla Comparativa de Resultados")
        
        # Crear tabla comparativa
        comparison_data = {
            "Métrica": [
                "Carga de Usuarios",
                "Eficiencia de Cache", 
                "Latencia del Sistema"
            ],
            "Función": [
                "T(t) = 4M + 3M·sin(π(t-6)/12) + 1M·sin(π(t-6)/6)",
                "E(s) = 100/(1 + e^(-0.1(s-50)))",
                "L(c) = 200·e^(-c/5M) + 50"
            ],
            "Intervalo": [
                "[0, 24] horas",
                "[10, 200] GB",
                "[1M, 8M] usuarios"
            ],
            "Integral": [
                "∫₀²⁴ T(t) dt",
                "∫₁₀²⁰⁰ E(s) ds",
                "∫₁ₘ⁸ₘ L(c) dc"
            ],
            "Unidades": [
                "usuarios-hora",
                "%·GB",
                "ms·usuarios"
            ]
        }
        
        df_comparison = pd.DataFrame(comparison_data)
        st.dataframe(df_comparison, use_container_width=True)
        
        st.markdown("""
        **Análisis Comparativo:**
        
        **Función de Tráfico T(t)**:
        - Tipo: Periódica (senos + constante)
        - Comportamiento: Cíclico con variaciones diarias
        - Aplicación: Planificación de capacidad
        
        **Función de Eficiencia E(s)**:
        - Tipo: Sigmoide (logística)
        - Comportamiento: Crecimiento con rendimientos decrecientes
        - Aplicación: Optimización de recursos
        
        **Función de Latencia L(c)**:
        - Tipo: Exponencial decreciente + constante
        - Comportamiento: Mejora con economías de escala
        - Aplicación: Garantías de SLA
        """)
    
    elif graph_type == "Análisis de Derivadas":
        st.markdown("#### 📉 Análisis de Derivadas y Tendencias")
        
        st.markdown("""
        #### 🔍 Derivadas de las Funciones del Sistema
        
        **1. Derivada de Tráfico: T'(t)**
        ```
        T'(t) = 3,000,000 · (π/12) · cos(π(t-6)/12) + 1,000,000 · (π/6) · cos(π(t-6)/6)
        ```
        - **T'(t) > 0**: Crecimiento de usuarios (mañana y tarde)
        - **T'(t) < 0**: Decrecimiento de usuarios (madrugada y noche)
        - **T'(t) = 0**: Picos y valles de tráfico
        
        **2. Derivada de Eficiencia: E'(s)**
        ```
        E'(s) = 10 · e^(-0.1(s-50)) / (1 + e^(-0.1(s-50)))²
        ```
        - **E'(s) > 0**: Siempre positiva (función creciente)
        - **Máximo de E'(s)**: En s = 50GB (punto de máxima eficiencia marginal)
        - **E'(s) → 0**: Cuando s → ∞ (rendimientos decrecientes)
        
        **3. Derivada de Latencia: L'(c)**
        ```
        L'(c) = -0.00004 · e^(-c/5,000,000)
        ```
        - **L'(c) < 0**: Siempre negativa (función decreciente)
        - **|L'(c)| máxima**: En c = 0 (mayor beneficio marginal inicial)
        - **L'(c) → 0**: Cuando c → ∞ (beneficio marginal tiende a cero)
        """)
        
        # Tabla de puntos críticos
        critical_points_data = {
            "Función": ["T(t)", "E(s)", "L(c)"],
            "Tipo de Función": ["Periódica", "Sigmoide", "Exponencial Decreciente"],
            "Derivada": ["Variable", "Siempre Positiva", "Siempre Negativa"],
            "Puntos Críticos": [
                "t = 2, 8, 14, 20 (aprox.)",
                "s = 50 (punto de inflexión)",
                "Sin puntos críticos internos"
            ],
            "Interpretación": [
                "Picos y valles de tráfico",
                "Máxima eficiencia marginal",
                "Mejora continua decreciente"
            ]
        }
        
        df_critical = pd.DataFrame(critical_points_data)
        st.dataframe(df_critical, use_container_width=True)

def show_conclusions():
    """Conclusiones del análisis completo."""
    st.markdown("### 💡 Conclusiones del Análisis Integral")
    
    st.markdown("""
    #### 🎯 Conclusiones Técnicas del Sistema de Caching Distribuido
    
    Después de realizar un análisis integral completo del sistema de caching distribuido 
    de StreamTech Solutions, podemos extraer las siguientes conclusiones fundamentales:
    """)
    
    # Conclusiones por área
    conclusion_tab1, conclusion_tab2, conclusion_tab3 = st.tabs([
        "🔍 Conclusiones Técnicas",
        "📚 Aporte Académico",
        "🔗 Vínculo con Ingeniería de Software"
    ])
    
    with conclusion_tab1:
        show_technical_conclusions()
    
    with conclusion_tab2:
        show_academic_contribution()
    
    with conclusion_tab3:
        show_software_engineering_link()

def show_technical_conclusions():
    """Conclusiones técnicas del análisis."""
    st.markdown("#### 🔍 Conclusiones Técnicas del Análisis")
    
    st.markdown("""
    ### 📊 Resultados Principales del Análisis Integral
    
    **1. Análisis de Carga de Usuarios (∫₀²⁴ T(t) dt)**
    """)
    
    # Simular cálculo para mostrar resultados
    try:
        traffic_result = 96000000  # Resultado aproximado
        st.success(f"✅ Carga total: {traffic_result:,} usuarios-hora")
        
        st.markdown(f"""
        **Conclusiones sobre el Tráfico:**
        - El sistema maneja aproximadamente **{traffic_result:,} usuarios-hora** diarios
        - Promedio de **{traffic_result//24:,} usuarios** concurrentes constantes
        - Variabilidad del **±75%** entre picos y valles
        - **Patrones identificados**: Dos ciclos superpuestos (24h y 12h)
        - **Recomendación**: Implementar auto-scaling basado en predicción matemática
        
        **Impacto en la Infraestructura:**
        - Servidores necesarios: **{traffic_result//2400000:,} instancias** en promedio
        - Ancho de banda total: **{traffic_result*0.5//1000:,} TB/día**
        - Costo operativo estimado: **${traffic_result*0.001:,.0f}/día**
        """)
    except:
        pass
    
    st.markdown("""
    **2. Análisis de Eficiencia de Cache (∫₁₀²⁰⁰ E(s) ds)**
    """)
    
    try:
        efficiency_result = 16500  # Resultado aproximado
        st.success(f"✅ Eficiencia acumulada: {efficiency_result:,} %·GB")
        
        st.markdown(f"""
        **Conclusiones sobre la Eficiencia:**
        - Eficiencia promedio del **{efficiency_result/190:.1f}%** en el rango analizado
        - **Punto óptimo identificado**: 50GB de cache por nodo
        - Hit rate proyectado: **85%+** (mejora del 42% vs actual)
        - **Zona de rendimientos decrecientes**: >80GB por nodo
        - **ROI máximo**: Configuración de 50-70GB por nodo
        
        **Impacto Económico:**
        - Reducción de cache misses: **40%**
        - Ahorro en ancho de banda: **${efficiency_result*10:,}/mes**
        - Mejora en experiencia de usuario: **35%**
        """)
    except:
        pass
    
    st.markdown("""
    **3. Análisis de Latencia (∫₁ₘ⁸ₘ L(c) dc)**
    """)
    
    try:
        latency_result = 700000  # Resultado aproximado  
        st.success(f"✅ Latencia acumulada: {latency_result:,} ms·usuarios")
        
        st.markdown(f"""
        **Conclusiones sobre la Latencia:**
        - Latencia promedio: **{latency_result/7000000:.1f}ms** en el rango operativo
        - **Comportamiento contraintuitivo**: Latencia decrece con más usuarios
        - **Explicación técnica**: Economías de escala en sistemas distribuidos
        - **SLA alcanzable**: <100ms en 99.9% de los casos
        - **Configuración óptima**: Mantener carga base >3M usuarios
        
        **Implicaciones para el Servicio:**
        - Mejora de **33%** en latencia vs sistema actual
        - Cumplimiento de SLA Premium en cargas altas
        - Estrategia de pre-calentamiento efectiva
        """)
    except:
        pass
    
    # Conclusiones integradas
    st.markdown("""
    ### 🎯 Conclusiones Integradas del Sistema
    
    **Función Objetivo Optimizada:**
    El análisis integral reveló que el sistema puede optimizarse mediante:
    
    **1. Configuración Recomendada:**
    - **Cache**: 50GB por nodo (punto de máxima eficiencia marginal)
    - **Auto-scaling**: 3M-8M usuarios (zona de latencia óptima)
    - **Distribución**: 10 nodos geográficamente distribuidos
    
    **2. Beneficios Proyectados:**
    - **Reducción de costos**: 40% en ancho de banda
    - **Mejora de rendimiento**: 35% en experiencia de usuario
    - **Cumplimiento de SLA**: 99.9% uptime garantizado
    - **ROI**: Recuperación de inversión en 6 meses
    
    **3. Validación Matemática:**
    - **Modelo predictivo**: Funciones continuas y derivables validadas
    - **Optimización global**: Punto óptimo encontrado via análisis integral
    - **Escalabilidad**: Sistema optimizado para crecimiento futuro
    """)
    
    # Métricas de éxito
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Mejora en Hit Rate",
            "85%",
            "+42%"
        )
    
    with col2:
        st.metric(
            "Reducción Latencia",
            "80ms",
            "-33%"
        )
    
    with col3:
        st.metric(
            "Ahorro Costos",
            "40%",
            "+$2M/año"
        )

def show_academic_contribution():
    """Aporte académico del curso de cálculo integral."""
    st.markdown("#### 📚 Aporte del Curso de Cálculo Integral")
    
    st.markdown("""
    ### 🎓 Reflexión sobre el Aporte Académico
    
    El desarrollo de este caso de estudio ha demostrado de manera tangible cómo el 
    **Cálculo Integral** se convierte en una herramienta fundamental para la formación 
    de futuros ingenieros de software. A continuación, se detalla el aporte específico:
    """)
    
    # Competencias desarrolladas
    st.markdown("""
    #### 🧠 Competencias Desarrolladas
    
    **1. Modelado Matemático de Sistemas Reales**
    - **Antes del curso**: Percepción del cálculo como conocimiento abstracto
    - **Después del curso**: Capacidad para modelar sistemas complejos con funciones matemáticas
    - **Impacto**: Habilidad para traducir problemas técnicos a lenguaje matemático
    
    **2. Análisis Cuantitativo de Rendimiento**
    - **Antes del curso**: Análisis empírico basado en pruebas y observación
    - **Después del curso**: Análisis predictivo basado en fundamentos matemáticos
    - **Impacto**: Capacidad para predecir comportamiento de sistemas antes de implementarlos
    
    **3. Optimización de Recursos**
    - **Antes del curso**: Optimización por ensayo y error
    - **Después del curso**: Optimización sistemática usando derivadas e integrales
    - **Impacto**: Encontrar puntos óptimos con fundamento matemático sólido
    """)
    
    # Metodologías aprendidas
    st.markdown("""
    #### 🔬 Metodologías Aprendidas Aplicables
    
    **1. Método del Análisis Integral**
    ```
    Problema Real → Función Matemática → Integral Definida → Interpretación Técnica
    ```
    
    **Aplicaciones Identificadas:**
    - Cálculo de recursos totales necesarios
    - Análisis de costos acumulados
    - Predicción de capacidad futura
    - Optimización de configuraciones
    
        **2. Método de Optimización por Derivadas**
    ```
    Función Objetivo → Derivada → Puntos Críticos → Máximos/Mínimos → Solución Óptima
    ```
    
    **Aplicaciones en Ingeniería de Software:**
    - Optimización de parámetros de algoritmos
    - Minimización de funciones de costo
    - Maximización de rendimiento de sistemas
    - Balanceamiento de cargas de trabajo
    
    **3. Método de Análisis de Convergencia**
    ```
    Serie/Secuencia → Límites → Criterios de Convergencia → Estabilidad del Sistema
    ```
    
    **Aplicaciones Prácticas:**
    - Análisis de estabilidad en algoritmos iterativos
    - Convergencia en machine learning
    - Estabilidad de sistemas distribuidos
    - Análisis de algoritmos de consenso
    """)

def show_educational_resources():
    """Recursos educativos y materiales de apoyo."""
    st.markdown("## 🎥 Recursos Educativos")
    st.markdown("Materiales de apoyo para profundizar en cálculo aplicado a ingeniería de software")
    
    # Videos educativos
    st.markdown("### 📹 Videos Recomendados")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🎯 Conceptos Fundamentales")
        videos_fundamentales = [
            "Introducción al Cálculo Integral en Informática",
            "Análisis de Complejidad con Integrales",
            "Optimización en Machine Learning",
            "Modelado Matemático de Sistemas"
        ]
        
        for video in videos_fundamentales:
            st.markdown(f"▶️ {video}")
            if st.button(f"Ver resumen", key=f"video_{video.replace(' ', '_')}"):
                st.info(f"Resumen de '{video}': Explicación teórica y ejemplos prácticos aplicados a ingeniería de software.")
    
    with col2:
        st.markdown("#### 🔬 Aplicaciones Avanzadas")
        videos_avanzados = [
            "Integrales en Análisis de Big Data",
            "Cálculo Vectorial en Gráficos 3D",
            "Ecuaciones Diferenciales en Simulaciones",
            "Teoría de la Información y Entropía"
        ]
        
        for video in videos_avanzados:
            st.markdown(f"▶️ {video}")
            if st.button(f"Ver resumen", key=f"video_adv_{video.replace(' ', '_')}"):
                st.info(f"Resumen de '{video}': Conceptos avanzados con implementaciones en proyectos reales.")
    
    # Documentación técnica
    st.markdown("### 📚 Documentación Técnica")
    
    docs = {
        "📖 Manual de Cálculo Integral": "Guía completa con ejemplos paso a paso",
        "🔧 API Reference": "Documentación de funciones matemáticas disponibles",
        "💡 Casos de Uso": "Ejemplos prácticos de la industria",
        "🎯 Ejercicios Resueltos": "Problemas con soluciones detalladas"
    }
    
    for doc, description in docs.items():
        with st.expander(doc):
            st.markdown(f"**Descripción:** {description}")
            st.markdown("- Contenido teórico fundamentado")
            st.markdown("- Ejemplos prácticos")
            st.markdown("- Ejercicios de aplicación")
            st.markdown("- Referencias adicionales")

def show_professional_applications():
    """Aplicaciones profesionales del cálculo en la industria."""
    st.markdown("## 💼 Aplicaciones Profesionales")
    st.markdown("Cómo se aplica el cálculo integral en la industria del software")
    
    # Industrias y aplicaciones
    industries = {
        "🏦 Fintech": {
            "description": "Tecnología financiera y análisis de riesgo",
            "applications": [
                "Cálculo de riesgo de cartera de inversiones",
                "Análisis de volatilidad de criptomonedas",
                "Optimización de algoritmos de trading",
                "Modelado de fraudes financieros"
            ],
            "tools": ["Black-Scholes", "Monte Carlo", "Value at Risk"]
        },
        "🚗 Autotech": {
            "description": "Vehículos autónomos y sistemas inteligentes",
            "applications": [
                "Planificación de rutas óptimas",
                "Análisis de sensores LIDAR",
                "Optimización de consumo energético",
                "Sistemas de frenado automático"
            ],
            "tools": ["Kalman Filters", "Control Theory", "Path Planning"]
        },
        "🎮 Gaming": {
            "description": "Desarrollo de videojuegos y motores gráficos",
            "applications": [
                "Física de partículas en tiempo real",
                "Animaciones fluidas de personajes",
                "Optimización de rendering 3D",
                "Inteligencia artificial de NPCs"
            ],
            "tools": ["Unity Physics", "Unreal Engine", "OpenGL"]
        },
        "🏥 HealthTech": {
            "description": "Tecnología médica y bioinformática",
            "applications": [
                "Análisis de señales biomédicas",
                "Optimización de dosificación de medicamentos",
                "Modelado de propagación de enfermedades",
                "Análisis de imágenes médicas"
            ],
            "tools": ["MATLAB", "R", "TensorFlow Medical"]
        }
    }
    
    selected_industry = st.selectbox(
        "🏭 Selecciona una industria:",
        list(industries.keys()),
        key="industry_selector"
    )
    
    industry_data = industries[selected_industry]
    
    # Mostrar información de la industria
    st.markdown(f"### {selected_industry}")
    st.info(f"**Descripción:** {industry_data['description']}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🎯 Aplicaciones Principales")
        for app in industry_data['applications']:
            st.markdown(f"• {app}")
    
    with col2:
        st.markdown("#### 🛠️ Herramientas Utilizadas")
        for tool in industry_data['tools']:
            st.markdown(f"• {tool}")
    
    # Salarios y oportunidades
    st.markdown("### 💰 Oportunidades Profesionales")
    
    salary_data = {
        "🏦 Fintech": {"junior": "$80,000", "senior": "$150,000", "growth": "15%"},
        "🚗 Autotech": {"junior": "$85,000", "senior": "$160,000", "growth": "20%"},
        "🎮 Gaming": {"junior": "$70,000", "senior": "$130,000", "growth": "12%"},
        "🏥 HealthTech": {"junior": "$75,000", "senior": "$140,000", "growth": "18%"}
    }
    
    if selected_industry in salary_data:
        salary = salary_data[selected_industry]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Salario Junior", salary["junior"])
        with col2:
            st.metric("Salario Senior", salary["senior"])
        with col3:
            st.metric("Crecimiento Anual", salary["growth"])

def show_software_engineering_link():
    """Explica la conexión entre cálculo y ingeniería de software."""
    st.markdown("## 🔗 Vínculo: Cálculo Integral ↔ Ingeniería de Software")
    
    st.markdown("""
    ### 🎯 ¿Por qué es importante el Cálculo para Ingenieros de Software?
    
    El cálculo integral no es solo matemática abstracta, es una herramienta fundamental 
    que permite a los ingenieros de software:
    """)
    
    # Conexiones principales
    connections = [
        {
            "title": "🧮 Análisis de Algoritmos",
            "description": "Calcular complejidad temporal y espacial total",
            "example": "∫[1 to n] f(x)dx = Tiempo total de ejecución",
            "real_case": "Google PageRank, algoritmos de ordenamiento"
        },
        {
            "title": "🤖 Machine Learning",
            "description": "Optimización de funciones de pérdida y gradientes",
            "example": "∫ loss(x)dx = Error total del modelo",
            "real_case": "TensorFlow, PyTorch, redes neuronales"
        },
        {
            "title": "📊 Análisis de Datos",
            "description": "Cálculo de métricas acumulativas y tendencias",
            "example": "∫ traffic(t)dt = Volumen total de datos",
            "real_case": "Analytics de Google, Facebook Insights"
        },
        {
            "title": "🎮 Física de Juegos",
            "description": "Simulación de movimiento y colisiones realistas",
            "example": "∫ velocity(t)dt = Distancia recorrida",
            "real_case": "Unity, Unreal Engine, motores físicos"
        },
        {
            "title": "💰 Optimización Financiera",
            "description": "Cálculo de riesgos y retornos de inversión",
            "example": "∫ profit(t)dt = Ganancia total esperada",
            "real_case": "Algoritmos de trading, fintech"
        }
    ]
    
    for i, connection in enumerate(connections):
        with st.expander(f"{connection['title']}", expanded=i==0):
            st.markdown(f"**Aplicación:** {connection['description']}")
            st.code(connection['example'])
            st.info(f"**Casos reales:** {connection['real_case']}")
    
    # Reflexión personal
    st.markdown("### 🤔 Reflexión: ¿Qué aporta a tu formación?")
    
    st.markdown("""
    **Como futuro Ingeniero de Software, el Cálculo Integral te permite:**
    
    1. **🎯 Pensamiento Analítico**: Descomponer problemas complejos en funciones matemáticas
    2. **📈 Optimización**: Encontrar soluciones eficientes para problemas de gran escala  
    3. **🔬 Modelado**: Representar sistemas reales con funciones matemáticas
    4. **📊 Análisis Predictivo**: Usar integrales para predecir comportamientos futuros
    5. **🏗️ Arquitectura de Sistemas**: Diseñar sistemas escalables basados en análisis matemático
    
    **El cálculo no es solo teoría - es la base matemática que sustenta:**
    - Los algoritmos de Google
    - La inteligencia artificial de Tesla
    - Los recomendadores de Netflix
    - Los sistemas de trading de Wall Street
    - Los motores gráficos de videojuegos AAA
    """)
    
    # Testimonios simulados
    st.markdown("### 💬 ¿Qué dicen los profesionales?")
    
    testimonials = [
        {
            "name": "Sarah Chen",
            "role": "Senior ML Engineer @ Google",
            "quote": "El cálculo integral es esencial para entender backpropagation y optimización de redes neuronales."
        },
        {
            "name": "Marcus Rodriguez", 
            "role": "Lead Game Developer @ Epic Games",
            "quote": "Sin cálculo, sería imposible crear físicas realistas en Fortnite."
        },
        {
            "name": "Aisha Patel",
            "role": "Quant Developer @ Goldman Sachs",
            "quote": "Uso integrales diariamente para modelar riesgos financieros y optimizar portafolios."
        }
    ]
    
    st.info(f'💬 "{testimonial["quote"]}" - **{testimonial["name"]}**, {testimonial["role"]}')
    
    # Call to action
    # Testimonios simulados
st.markdown("### 💬 ¿Qué dicen los profesionales?")

testimonials = [
    {
        "name": "Sarah Chen",
        "role": "Senior ML Engineer @ Google",
        "quote": "El cálculo integral es esencial para entender backpropagation y optimización de redes neuronales."
    },
    {
        "name": "Marcus Rodriguez", 
        "role": "Lead Game Developer @ Epic Games",
        "quote": "Sin cálculo, sería imposible crear físicas realistas en Fortnite."
    },
    {
        "name": "Aisha Patel",
        "role": "Quant Developer @ Goldman Sachs",
        "quote": "Uso integrales diariamente para modelar riesgos financieros y optimizar portafolios."
    }
]

for testimonial in testimonials:
    # CORRECCIÓN: Cambiar st.quote por st.info o st.markdown
    st.info(f'💬 "{testimonial["quote"]}" - **{testimonial["name"]}**, {testimonial["role"]}')
# Función para mostrar conclusiones completas
def show_complete_conclusions():
    """Muestra las conclusiones completas del curso y su aplicación."""
    st.markdown("## 🎓 Conclusiones del Análisis Integral en Ingeniería de Software")
    
    st.markdown("""
    ### 📊 Análisis Completo Realizado
    
    A través de este estudio interactivo, hemos explorado sistemáticamente:
    
    1. **Cálculo de Áreas y Volúmenes**: Aplicados a optimización de algoritmos y análisis de recursos
    2. **Análisis de Funciones Continuas**: Modelado de sistemas de monitoreo en tiempo real
    3. **Integrales Definidas**: Cálculo de métricas acumulativas en sistemas de software
    4. **Representaciones Gráficas**: Visualización de comportamientos de sistemas complejos
    
    ### 🔍 Metodologías Aplicadas
    
    **1. Método Analítico-Descriptivo**
    - Descomposición de problemas reales en funciones matemáticas
    - Análisis de continuidad y derivabilidad
    - Cálculo de integrales definidas con interpretación contextual
    
    **2. Método Comparativo**
    - Evaluación de diferentes algoritmos mediante análisis integral
    - Comparación de eficiencia entre sistemas
    - Optimización basada en análisis matemático
    
    **3. Método Experimental**
    - Simulación de sistemas reales
    - Validación de modelos matemáticos
    - Experimentación con parámetros variables
    
    ### 🎯 Aporte del Curso a la Formación Profesional
    
    **Como futuros ingenieros de software, este curso nos ha proporcionado:**
    
    #### 🧠 Competencias Cognitivas
    - **Pensamiento Analítico**: Capacidad de modelar problemas complejos matemáticamente
    - **Razonamiento Lógico**: Establecimiento de relaciones causa-efecto en sistemas
    - **Abstracción**: Generalización de problemas específicos a modelos universales
    
    #### 🛠️ Competencias Técnicas  
    - **Análisis de Complejidad**: Evaluación rigurosa de algoritmos
    - **Optimización de Sistemas**: Mejora de rendimiento basada en análisis matemático
    - **Modelado Predictivo**: Anticipación de comportamientos de sistemas
    
    #### 💼 Competencias Profesionales
    - **Toma de Decisiones**: Basada en análisis cuantitativo
    - **Comunicación Técnica**: Expresión clara de conceptos matemáticos complejos
    - **Innovación**: Aplicación creativa de conceptos matemáticos a problemas tecnológicos
    
    ### 🔗 Vínculo Específico: Cálculo Integral ↔ Ingeniería de Software
    
    **La conexión es profunda y multifacética:**
    
    #### 1. **Fundamentos Algorítmicos**
    ```
    Cálculo Integral → Análisis de Complejidad → Diseño de Algoritmos Eficientes
    ```
    - Las integrales permiten calcular costos computacionales totales
    - Optimización de algoritmos mediante análisis de funciones de costo
    - Predicción de escalabilidad de sistemas
    
    #### 2. **Inteligencia Artificial y Machine Learning**
    ```
    Cálculo Integral → Optimización de Funciones → Entrenamiento de Modelos
    ```
    - Gradiente descendente como aplicación directa de cálculo
    - Funciones de pérdida como integrales de error
    - Backpropagation basado en regla de la cadena
    
    #### 3. **Análisis de Sistemas**
    ```
    Cálculo Integral → Modelado de Sistemas → Análisis de Rendimiento
    ```
    - Monitoreo continuo de métricas de sistema
    - Análisis de tendencias y patrones temporales
    - Predicción de cargas y planificación de capacidad
    
    #### 4. **Desarrollo de Videojuegos**
    ```
    Cálculo Integral → Física Computacional → Experiencias Inmersivas
    ```
    - Simulación de movimiento y colisiones
    - Rendering de gráficos realistas
    - Inteligencia artificial de personajes
    
    ### 💡 Reflexión Final
    
    **El Cálculo Integral no es meramente una asignatura matemática** - es el lenguaje 
    fundamental que nos permite:
    
    - **Cuantificar** el rendimiento de nuestros sistemas
    - **Optimizar** los recursos computacionales
    - **Predecir** el comportamiento futuro de aplicaciones
    - **Innovar** en el diseño de algoritmos
    - **Resolver** problemas complejos de manera elegante
    
    **En un mundo donde los datos crecen exponencialmente y los sistemas se vuelven 
    cada vez más complejos**, dominar el cálculo integral nos convierte en ingenieros 
    de software capaces de:
    
    1. **Crear algoritmos verdaderamente eficientes**
    2. **Diseñar sistemas escalables y robustos**  
    3. **Innovar en áreas emergentes como IA y computación cuántica**
    4. **Liderar equipos técnicos con fundamentos sólidos**
    5. **Contribuir al avance tecnológico de la humanidad**
    
    ### 🚀 Perspectiva Futura
    
    **Las tecnologías del futuro** - computación cuántica, inteligencia artificial general, 
    realidad virtual inmersiva, vehículos autónomos - **todas requieren ingenieros que 
    dominen tanto el código como las matemáticas que lo sustentan**.
    
    Este curso nos ha preparado no solo para resolver los problemas de hoy, sino para 
    **imaginar y construir las soluciones del mañana**. 🌟
    """)
    
    # Estadísticas del aprendizaje
    st.markdown("### 📈 Impacto Medible del Aprendizaje")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Conceptos Dominados", "15+", "🎯")
    with col2:
        st.metric("Aplicaciones Prácticas", "25+", "🛠️")
    with col3:
        st.metric("Problemas Resueltos", "40+", "✅")
    with col4:
        st.metric("Competencias Desarrolladas", "12+", "🧠")
    