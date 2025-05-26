import streamlit as st
import numpy as np
from utils.calculator import solve_integral
from utils.plotting import plot_integral
from components.solution_display import display_solution, display_error_message
from components.math_input import create_math_input, create_function_examples
from assets.translations import get_text
import pandas as pd

def show():
    """Display software engineering scenarios related to integrals."""
    st.title("🏗️ Cálculo en Ingeniería de Software")
    st.markdown("**Descubre cómo el cálculo integral impulsa la innovación tecnológica**")
    
    # Tabs optimizados
    tab1, tab2, tab3, tab4 = st.tabs([
        "🧮 Calculadora Interactiva",
        "🔬 Caso de Estudio Completo", 
        "🎲 Escenarios Aleatorios",
        "🎥 Recursos Educativos"
    ])
    
    with tab1:
        show_interactive_calculator()
    
    with tab2:
        show_complete_case_study()
    
    with tab3:
        show_random_scenarios()
    
    with tab4:
        show_educational_resources()

def show_interactive_calculator():
    """Mostrar calculadora interactiva."""
    st.markdown("## 🧮 Calculadora Interactiva")
    st.markdown("**Resuelve integrales definidas con visualización**")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        function_input = st.text_input("🔢 Función f(x):", "x**2 + 2*x + 1", key="interactive_func")
        
        col_a, col_b = st.columns(2)
        with col_a:
            lower_input = st.text_input("📉 Límite inferior:", "0", key="interactive_lower")
        with col_b:
            upper_input = st.text_input("📈 Límite superior:", "5", key="interactive_upper")
        
        variable_input = st.selectbox("📊 Variable:", ["x", "t", "u", "s"], key="interactive_var")
        
        if st.button("🚀 Calcular Integral", key="interactive_calc", type="primary"):
            from utils.calculator import calculate_definite_integral_robust
            
            success, result, details = calculate_definite_integral_robust(
                function_input, lower_input, upper_input, variable_input
            )
            
            if success:
                st.success(f"✅ **Resultado:** {result:.6f}")
                st.metric("📈 Valor de la Integral", f"{result:.6f}")
                st.info(f"🔧 Método: {details.get('method_used', 'Numérico')}")
            else:
                st.error(f"❌ Error: {result}")
    
    with col2:
        st.info("""
        **💡 Ejemplos:**
        - `x**2` → Parábola
        - `sin(x)` → Seno
        - `exp(-x)` → Exponencial
        - `log(x+1)` → Logaritmo
        """)
    
    # Visualización
    if st.button("📊 Visualizar", key="interactive_plot"):
        plot_integral(function_input, lower_input, upper_input, variable_input)

def show_random_scenarios():
    """Generador de escenarios aleatorios de cálculo y software."""
    st.markdown("## 🎲 Generador de Escenarios Aleatorios")
    st.markdown("**Problemas dinámicos de cálculo aplicado a ingeniería de software**")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        difficulty = st.selectbox("🎯 Nivel de Dificultad:", 
                                ["🟢 Básico", "🟡 Intermedio", "🔴 Avanzado"])
        
        category = st.selectbox("📂 Categoría:", [
            "🚀 Optimización de Rendimiento",
            "📊 Machine Learning", 
            "🌐 Sistemas Distribuidos",
            "💾 Bases de Datos",
            "🔒 Seguridad"
        ])
        
        if st.button("🎲 Generar Problema Aleatorio", type="primary"):
            scenario = generate_random_scenario(difficulty, category)
            # ✅ GUARDAR ESCENARIO EN SESSION STATE
            st.session_state['current_scenario'] = scenario
            st.rerun()
    
    with col2:
        st.info("""
        **🎯 ¿Qué hace el generador?**
        - Crea problemas únicos cada vez
        - Contextos realistas de empresas tech
        - Funciones matemáticas variables
        - Aplicaciones prácticas del cálculo
        """)
    
    # ✅ MOSTRAR ESCENARIO SI EXISTE
    if 'current_scenario' in st.session_state:
        display_random_scenario(st.session_state['current_scenario'])
def generate_random_scenario(difficulty, category):
    """Generar escenario aleatorio basado en parámetros."""
    import random
    
    # Templates por categoría
    templates = {
        "🚀 Optimización de Rendimiento": [
            {"func": lambda: f"{random.randint(10,100)}*t**2 + {random.randint(1,20)}*t", 
             "context": "Tiempo de procesamiento de algoritmo O(n²)",
             "bounds": [0, random.randint(50, 200)]},
            {"func": lambda: f"{random.randint(20,150)}*exp(-{random.uniform(0.1,0.5):.2f}*t)", 
             "context": "Degradación de cache después de pico",
             "bounds": [0, random.randint(10, 60)]}
        ],
        "📊 Machine Learning": [
            {"func": lambda: f"{random.uniform(0.5,2.0):.2f}*exp(-{random.uniform(0.01,0.2):.3f}*t)", 
             "context": "Función de pérdida durante entrenamiento",
             "bounds": [0, random.randint(100, 1000)]},
            {"func": lambda: f"{random.randint(5,25)}*log(t+1) + {random.randint(1,10)}", 
             "context": "Convergencia de accuracy en epochs",
             "bounds": [1, random.randint(50, 200)]}
        ],
        "🌐 Sistemas Distribuidos": [
            {"func": lambda: f"{random.randint(100,500)}*sin(3.14*t/{random.randint(12,24)}) + {random.randint(200,800)}", 
             "context": "Carga de tráfico distribuido",
             "bounds": [0, random.randint(24, 72)]},
            {"func": lambda: f"{random.randint(50,200)}*exp(-t/{random.randint(10,30)}) + {random.randint(10,50)}", 
             "context": "Latencia en red distribuida",
             "bounds": [0, random.randint(60, 180)]}
        ],
        "💾 Bases de Datos": [
            {"func": lambda: f"{random.randint(1000,5000)}*log(t+1) + {random.randint(100,500)}*t", 
             "context": "Consultas por segundo en base de datos",
             "bounds": [1, random.randint(24, 168)]},
            {"func": lambda: f"{random.randint(50,200)}*sqrt(t) + {random.randint(10,100)}", 
             "context": "Tiempo de respuesta de consultas",
             "bounds": [1, random.randint(100, 500)]}
        ],
        "🔒 Seguridad": [
            {"func": lambda: f"{random.randint(10,100)}*exp(t/{random.randint(50,200)}) + {random.randint(5,50)}", 
             "context": "Intentos de acceso maliciosos",
             "bounds": [0, random.randint(24, 72)]},
            {"func": lambda: f"{random.randint(100,1000)}*sin(3.14*t/{random.randint(6,24)}) + {random.randint(50,500)}", 
             "context": "Eventos de seguridad detectados",
             "bounds": [0, random.randint(24, 168)]}
        ]
    }
    
    template = random.choice(templates.get(category, templates["🚀 Optimización de Rendimiento"]))
    
    return {
        "function": template["func"](),
        "context": template["context"],
        "company": random.choice(["TechCorp", "DataFlow Inc", "CloudScale", "AI Systems", "ByteForce", "NeoStream"]),
        "metric": random.choice(["MB/s", "ms", "requests/s", "% CPU", "GB", "usuarios", "eventos/h"]),
        "lower": "0",
        "upper": str(template["bounds"][1]),
        "variable": "t"
    }
def display_random_scenario(scenario):
    """Mostrar escenario generado con funcionalidad completa."""
    st.success(f"🏢 **{scenario['company']}** - {scenario['context']}")
    
    st.info(f"""
    **📊 Problema Generado:**
    - **Función:** `f(t) = {scenario['function']}`
    - **Intervalo:** [0, {scenario['upper']}] horas
    - **Métrica:** {scenario['metric']}
    - **Variable:** t (tiempo)
    """)
    
    # ✅ CREAR COLUMNAS PARA BOTONES
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🚀 Resolver Escenario", key="solve_random", type="primary"):
            solve_random_scenario(scenario)
    
    with col2:
        if st.button("📊 Ver Gráfica", key="plot_random"):
            plot_random_scenario(scenario)
    
    with col3:
        if st.button("🔄 Generar Nuevo", key="regenerate_random"):
            # ✅ LIMPIAR SESSION STATE Y REGENERAR
            if 'current_scenario' in st.session_state:
                del st.session_state['current_scenario']
            st.rerun()
def solve_random_scenario(scenario):
    """Resolver escenario aleatorio con análisis completo."""
    try:
        from utils.calculator import calculate_definite_integral_robust
        
        st.markdown("### 🚀 Resolviendo Escenario...")
        
        with st.spinner("Calculando integral..."):
            success, result, details = calculate_definite_integral_robust(
                scenario['function'], scenario['lower'], scenario['upper'], scenario['variable']
            )
        
        if success:
            st.success(f"### ✅ Resultado: {result:.2f} {scenario['metric']}")
            
            # ✅ MÉTRICAS EN COLUMNAS
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("📈 Valor Total Acumulado", f"{result:.2f}")
            
            with col2:
                try:
                    average_value = result / float(scenario['upper'])
                    st.metric("📊 Valor Promedio/Hora", f"{average_value:.2f}")
                except:
                    st.metric("📊 Valor Promedio/Hora", "N/A")
            
            with col3:
                st.metric("🔧 Método Usado", details.get('method_used', 'Numérico'))
            
            # ✅ INTERPRETACIÓN CONTEXTUAL
            st.markdown("### 💡 Interpretación del Resultado")
            
            context_lower = scenario['context'].lower()
            
            if "tiempo de procesamiento" in context_lower or "algoritmo" in context_lower:
                st.info(f"""
                **🚀 Optimización de Rendimiento:**
                - **Tiempo total acumulado:** {result:.2f} {scenario['metric']}
                - **Impacto:** Costo computacional total del algoritmo
                - **Recomendación:** Optimizar complejidad algorítmica
                - **Meta:** Reducir área bajo la curva = menor costo total
                """)
                
            elif "cache" in context_lower or "degradación" in context_lower:
                st.info(f"""
                **💾 Gestión de Cache:**
                - **Degradación total:** {result:.2f} {scenario['metric']}
                - **Impacto:** Pérdida de eficiencia acumulada
                - **Recomendación:** Implementar cache warming automático
                - **Meta:** Minimizar área = mejor rendimiento sostenido
                """)
                
            elif "pérdida" in context_lower or "entrenamiento" in context_lower:
                st.info(f"""
                **📊 Machine Learning:**
                - **Pérdida total:** {result:.2f}
                - **Impacto:** Convergencia del modelo durante entrenamiento
                - **Recomendación:** Ajustar learning rate si pérdida alta
                - **Meta:** Área decreciente = modelo mejorando
                """)
                
            elif "tráfico" in context_lower or "carga" in context_lower:
                st.info(f"""
                **🌐 Sistemas Distribuidos:**
                - **Carga total procesada:** {result:.2f} {scenario['metric']}
                - **Impacto:** Capacidad total requerida del sistema
                - **Recomendación:** Dimensionar infraestructura según picos
                - **Meta:** Área = recursos totales necesarios
                """)
                
            elif "consultas" in context_lower or "base de datos" in context_lower:
                st.info(f"""
                **💾 Bases de Datos:**
                - **Consultas totales procesadas:** {result:.2f} {scenario['metric']}
                - **Impacto:** Carga acumulada en el sistema de BD
                - **Recomendación:** Optimizar índices y consultas frecuentes
                - **Meta:** Área estable = rendimiento consistente
                """)
                
            elif "seguridad" in context_lower or "acceso" in context_lower:
                st.info(f"""
                **🔒 Seguridad:**
                - **Eventos totales detectados:** {result:.2f} {scenario['metric']}
                - **Impacto:** Nivel de amenaza acumulado
                - **Recomendación:** Reforzar sistemas de detección
                - **Meta:** Área controlada = seguridad efectiva
                """)
                
            else:
                st.info(f"""
                **📈 Análisis General:**
                - **Valor total acumulado:** {result:.2f} {scenario['metric']}
                - **Contexto:** {scenario['context']}
                - **Empresa:** {scenario['company']}
                - **Período analizado:** {scenario['upper']} horas
                """)
            
            # ✅ BOTÓN PARA VER GRÁFICA DESPUÉS DE RESOLVER
            if st.button("📊 Ver Visualización", key="plot_after_solve"):
                plot_random_scenario(scenario)
                
        else:
            st.error(f"❌ Error al calcular: {result}")
            st.warning("💡 Intenta con un escenario diferente")
    
    except Exception as e:
        st.error(f"❌ Error resolviendo escenario: {str(e)}")
        
        # ✅ DEBUG INFO
        with st.expander("🔍 Información de Debug"):
            st.code(f"""
Función: {scenario['function']}
Límites: [{scenario['lower']}, {scenario['upper']}]
Variable: {scenario['variable']}
Error: {str(e)}
            """)
def plot_random_scenario(scenario):
    """Visualizar escenario aleatorio con análisis completo."""
    try:
        st.markdown(f"### 📊 Visualización: {scenario['context']}")
        st.markdown(f"**Empresa:** {scenario['company']} | **Métrica:** {scenario['metric']}")
        
        # ✅ GRÁFICA PRINCIPAL CON MANEJO DE ERRORES
        try:
            plot_integral(scenario['function'], scenario['lower'], 
                         scenario['upper'], scenario['variable'])
        except Exception as plot_error:
            st.error(f"Error en gráfica principal: {plot_error}")
            st.warning("Intentando con visualización alternativa...")
            
            # ✅ FALLBACK: MOSTRAR FUNCIÓN SIN ÁREA
            try:
                from utils.plotting import plot_riemann_sum
                plot_riemann_sum(
                    scenario['function'],
                    float(scenario['lower']),
                    float(scenario['upper']),
                    20,  # Pocas muestras para evitar errores
                    "midpoint",
                    scenario['variable']
                )
            except Exception as fallback_error:
                st.error(f"Error en visualización alternativa: {fallback_error}")
                return
        
        # ✅ INFORMACIÓN ADICIONAL
        st.markdown("### 📈 Análisis Visual")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info(f"""
            **🎯 Función Matemática:**
            - **Expresión:** f(t) = {scenario['function']}
            - **Dominio:** [0, {scenario['upper']}] horas
            - **Contexto:** {scenario['context']}
            
            **📊 El área bajo la curva representa:**
            - Acumulación total de {scenario['metric']} durante el período
            - Impacto integral en el sistema de {scenario['company']}
            """)
        
        with col2:
            st.markdown("**🔬 Análisis Avanzado**")
            
            # ✅ BOTÓN PARA RIEMANN
            if st.button("📐 Ver Aproximación Discreta", key="riemann_random"):
                try:
                    st.markdown("#### 📐 Aproximación por Sumas de Riemann")
                    from utils.plotting import plot_riemann_sum
                    
                    plot_riemann_sum(
                        scenario['function'],
                        float(scenario['lower']),
                        float(scenario['upper']),
                        50,  # 50 muestras
                        "midpoint",
                        scenario['variable']
                    )
                    
                    st.info("""
                    💡 **Interpretación:**
                    Esta aproximación simula monitoreo cada ~30 minutos,
                    típico en sistemas de observabilidad empresarial.
                    """)
                except Exception as riemann_error:
                    st.error(f"Error en Riemann: {riemann_error}")
            
            # ✅ BOTÓN PARA RESOLVER SI NO SE HA HECHO
            if st.button("🚀 Resolver Ahora", key="solve_from_plot"):
                solve_random_scenario(scenario)
    
    except Exception as e:
        st.error(f"❌ Error en visualización: {str(e)}")
        
        # ✅ DEBUG Y ALTERNATIVA
        with st.expander("🔍 Información de Debug"):
            st.code(f"""
Función: {scenario['function']}
Límites: [{scenario['lower']}, {scenario['upper']}]
Variable: {scenario['variable']}
Error: {str(e)}
            """)
        
        st.info("💡 **Sugerencia:** Intenta generar un nuevo escenario")

def show_complete_case_study():
    """✅ CASO DE ESTUDIO COMPLETO - Con las 4 funcionalidades requeridas."""
    st.markdown("## 🔬 Caso de Estudio: Sistema de Streaming de Video")
    st.markdown("**StreamTech Solutions - Aplicación Práctica del Cálculo Integral**")
    
    # Introducción del problema real
    with st.expander("📖 Contexto del Problema Empresarial", expanded=True):
        st.markdown("""
        ### 🎯 StreamTech Solutions - Plataforma de 10M usuarios
        
        **Desafíos Actuales:**
        - 🔴 Latencia alta en horas pico (19:00-23:00)
        - 🟡 Cache hit rate bajo (60% actual vs 85% objetivo)
        - 🟠 Costos elevados de ancho de banda
        - 🔵 Experiencia inconsistente del usuario
        
        **Métricas del Sistema:**
        - 👥 Usuarios: 2M base + 8M variable
        - 💾 Cache: 500 GB distribuida
        - ⚡ Latencia: 150ms promedio
        - 🌐 Bandwidth: 10 Tbps pico
        
        ### 🧮 Aplicación de los 4 Conceptos de Cálculo Integral:
        
        **1. 📊 CÁLCULO INTEGRAL DEFINIDO** → Consumo total de recursos  
        **2. 📐 SUMAS DE RIEMANN** → Aproximaciones con muestreo discreto  
        **3. 🔵 ÁREA BAJO LA CURVA** → Impacto acumulado geométrico  
        **4. 🔄 VOLUMEN DE SÓLIDOS** → Capacidad tridimensional del sistema  
        """)
    
    # Selector de métricas del sistema
    st.markdown("### 🔧 Seleccionar Métrica del Sistema")
    
    system_metrics = {
        "📈 Tráfico de Usuarios": {
            "function": "2000000 + 8000000*sin(3.14*t/12)",
            "variable": "t", "lower": "0", "upper": "24",
            "units": "usuarios·hora",
            "description": "Patrón diario de carga de usuarios concurrentes"
        },
        "💾 Eficiencia del Cache": {
            "function": "60 + 25*cos(3.14*t/8) + 15*sqrt(t)",
            "variable": "t", "lower": "0", "upper": "24",
            "units": "% hit rate·hora",
            "description": "Rendimiento del sistema de cache distribuido"
        },
        "⚡ Latencia del Sistema": {
            "function": "150 - 50*sin(3.14*t/12) + 20*exp(-t/24)",
            "variable": "t", "lower": "0", "upper": "24",
            "units": "ms·hora",
            "description": "Tiempo de respuesta promedio del sistema"
        },
        "🧠 Consumo de Memoria": {
            "function": "50 + 30*sin(3.14*t/12) + 15*cos(3.14*t/6) + 5*sqrt(t)",
            "variable": "t", "lower": "0", "upper": "24",
            "units": "GB·hora",
            "description": "Uso de memoria del sistema de cache"
        }
    }
    
    selected_metric = st.selectbox(
        "🎯 Métrica a analizar:",
        list(system_metrics.keys()),
        key="metric_selector"
    )
    
    current_metric = system_metrics[selected_metric]
    
    st.info(f"""
    **📊 Métrica:** {selected_metric}  
    **📝 Descripción:** {current_metric['description']}  
    **🔢 Función:** `f(t) = {current_metric['function']}`  
    **⏰ Período:** 24 horas  
    **📏 Unidades:** {current_metric['units']}
    """)
    
    # ✅ TABS CON LAS 4 FUNCIONALIDADES REQUERIDAS
    concept_tabs = st.tabs([
        "📊 1. CÁLCULO INTEGRAL",
        "📐 2. SUMAS DE RIEMANN", 
        "🔵 3. ÁREA BAJO CURVA",
        "🔄 4. VOLUMEN DE SÓLIDOS"
    ])
    
    # ✅ 1. CÁLCULO INTEGRAL DEFINIDO
    with concept_tabs[0]:
        st.markdown("### 📊 Concepto 1: Cálculo Integral Definido")
        
        st.markdown(f"""
        **🎯 Aplicación en {selected_metric}:**
        
        El **cálculo integral definido** calcula el **valor total acumulado** durante 24 horas.
        
        **💡 ¿Por qué es importante?**
        - **Planificación de Capacidad:** Recursos totales necesarios
        - **Estimación de Costos:** Base para presupuestos operativos  
        - **SLA Compliance:** Cumplimiento de acuerdos de servicio
        - **Análisis de Tendencias:** Comportamiento integral del sistema
        """)
        
        # Fórmula matemática
        function_clean = current_metric['function'].replace('*', '\\cdot').replace('**', '^').replace('3.14', '\\pi')
        st.latex(f"\\int_{{0}}^{{24}} [{function_clean}] \\, dt")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🚀 Calcular Integral", key="integral_calc"):
                calculate_integral_definite(current_metric, selected_metric)
        with col2:
            if st.button("📈 Visualizar", key="integral_plot"):
                st.markdown(f"#### 📈 Gráfica de {selected_metric}")
                plot_integral(current_metric['function'], current_metric['lower'], 
                            current_metric['upper'], current_metric['variable'])
    
    # ✅ 2. SUMAS DE RIEMANN
    with concept_tabs[1]:
        st.markdown("### 📐 Concepto 2: Sumas de Riemann")
        
        st.markdown(f"""
        **🎯 Aplicación en Sistemas Digitales:**
        
        Las **Sumas de Riemann** aproximan integrales usando **muestreo discreto**.
        
        **💡 ¿Por qué es crucial en streaming?**
        - **Monitoreo en Tiempo Real:** Servidores miden cada pocos minutos
        - **Aproximación Rápida:** Estimaciones sin datos completos
        - **Decisiones Dinámicas:** Ajustes automáticos del sistema
        - **Eficiencia Computacional:** Cálculos ligeros para alta frecuencia
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            method = st.selectbox("🔧 Método:", ["left", "right", "midpoint", "simpson"], key="riemann_method")
            n_samples = st.slider("📊 Muestras/día:", 10, 500, 96, key="riemann_samples")
            minutes_interval = 24 * 60 / n_samples
            st.info(f"📏 Medición cada {minutes_interval:.1f} minutos")
        
        with col2:
            if st.button("📊 Calcular Riemann", key="riemann_calc"):
                calculate_riemann_sum(current_metric, selected_metric, method, n_samples)
            if st.button("📉 Visualizar Aproximación", key="riemann_plot"):
                st.markdown(f"#### 📉 Aproximación Discreta de {selected_metric}")
                plot_riemann_visualization(current_metric, method, n_samples)
    
    # ✅ 3. ÁREA BAJO LA CURVA
    with concept_tabs[2]:
        st.markdown("### 🔵 Concepto 3: Área bajo la Curva")
        
        st.markdown(f"""
        **🎯 Interpretación Geométrica:**
        
        El **área bajo la curva** visualiza el **impacto acumulado** del sistema.
        
        **💡 Significado por métrica:**
        - **📈 Tráfico:** Total de experiencias de usuario entregadas
        - **💾 Cache:** Eficiencia acumulada del sistema distribuido
        - **⚡ Latencia:** Impacto total en calidad de experiencia  
        - **🧠 Memoria:** Recursos computacionales totales consumidos
        """)
        
        # Análisis por períodos
        periods = {
            "🌙 Madrugada (0-6h)": (0, 6, "Bajo tráfico - Mantenimiento"),
            "🌅 Mañana (6-12h)": (6, 12, "Crecimiento gradual"),
            "☀️ Tarde (12-18h)": (12, 18, "Actividad sostenida"),
            "🌆 Noche (18-24h)": (18, 24, "Horas pico de streaming")
        }
        
        col1, col2 = st.columns(2)
        with col1:
            selected_period = st.selectbox("🕒 Período:", list(periods.keys()), key="period_select")
            period_info = periods[selected_period]
            st.info(f"**Contexto:** {period_info[2]}")
        
        with col2:
            if st.button("🔵 Calcular Área Período", key="area_calc"):
                calculate_area_analysis(current_metric, selected_metric, period_info)
            if st.button("📊 Visualizar Área", key="area_plot"):
                st.markdown(f"#### 📊 Visualización de {selected_metric} - {selected_period}")
                plot_integral(current_metric['function'], str(period_info[0]), 
                            str(period_info[1]), current_metric['variable'])
    
    # ✅ 4. VOLUMEN DE SÓLIDOS DE REVOLUCIÓN
    with concept_tabs[3]:
        st.markdown("### 🔄 Concepto 4: Volumen de Sólidos de Revolución")
        
        st.markdown(f"""
        **🎯 Modelado Tridimensional:**
        
        Los **sólidos de revolución** calculan la **capacidad volumétrica** del sistema.
        
        **💡 Aplicaciones en ingeniería:**
        - **Escalamiento Cúbico:** Crecimiento tridimensional de demanda
        - **Dimensionamiento de Clusters:** Capacidad total de procesamiento
        - **Arquitectura Distribuida:** Planificación de infraestructura 3D
        - **Análisis de Capacidad:** Volumen = recursos totales necesarios
        """)
        
        # Fórmula de volumen
        st.latex(f"V = \\pi \\int_{{0}}^{{24}} [f(t)]^2 \\, dt")
        
        col1, col2 = st.columns(2)
        with col1:
            axis = st.selectbox("🔄 Eje revolución:", 
                              ["⏰ Tiempo (horizontal)", "📊 Métrica (vertical)"], 
                              key="volume_axis")
            if st.button("🔄 Calcular Volumen", key="volume_calc"):
                calculate_volume_revolution_fixed(current_metric, selected_metric, axis)
        
        with col2:
            if st.button("🎯 Interpretación Ingeniería", key="volume_interpret"):
                interpret_volume_engineering_fixed(current_metric, selected_metric)
        
        # ✅ AGREGAR SECCIÓN 3D AL FINAL DEL TAB
        st.markdown("---")
        show_3d_volume_section(current_metric, selected_metric)

def show_educational_resources():
    """Mostrar recursos educativos."""
    st.markdown("## 🎥 Recursos Educativos")
    st.markdown("**Aprende cálculo integral con los mejores recursos online**")
    
    # Enlaces a recursos reales
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📺 Videos Educativos
        
        **Khan Academy - Cálculo Integral:**
        - [Introducción a Integrales](https://www.khanacademy.org/math/calculus-1/cs1-integration-and-accumulation-of-change)
        - [Sumas de Riemann](https://www.khanacademy.org/math/calculus-1/cs1-integration-and-accumulation-of-change/cs1-riemann-sums)
        - [Teorema Fundamental del Cálculo](https://www.khanacademy.org/math/calculus-1/cs1-integration-and-accumulation-of-change/cs1-fundamental-theorem-of-calculus)
        
        **3Blue1Brown - Essence of Calculus:**
        - [¿Qué es una integral?](https://www.youtube.com/watch?v=rfG8ce4nNh0)
        - [Integrales y Área](https://www.youtube.com/watch?v=FnJqaIESC2s)
        """)
    
    with col2:
        st.markdown("""
        ### 📚 Documentación y Cursos
        
        **MIT OpenCourseWare:**
        - [18.01 Single Variable Calculus](https://ocw.mit.edu/courses/mathematics/18-01-single-variable-calculus-fall-2006/)
        - [Calculus with Applications](https://ocw.mit.edu/courses/mathematics/18-013a-calculus-with-applications-spring-2005/)
        
        **Herramientas Interactivas:**
        - [Desmos Graphing Calculator](https://www.desmos.com/calculator)
        - [Wolfram Alpha](https://www.wolframalpha.com/)
        - [GeoGebra Calculus](https://www.geogebra.org/calculator)
        """)

# ✅ FUNCIONES AUXILIARES CORREGIDAS:

def calculate_integral_definite(current_metric, selected_metric):
    """Calcular integral definida."""
    try:
        from utils.calculator import calculate_definite_integral_robust
        
        with st.spinner(f"🚀 Calculando integral para {selected_metric}..."):
            success, result, details = calculate_definite_integral_robust(
                current_metric['function'], current_metric['lower'], 
                current_metric['upper'], current_metric['variable']
            )
        
        if success:
            st.success(f"### ✅ Resultado: {result:.2f} {current_metric['units']}")
            
            # Interpretación por métrica
            if "Usuarios" in selected_metric:
                st.metric("👥 Usuarios-hora totales", f"{result:,.0f}")
                st.info(f"💡 Capacidad necesaria: {result/24:.0f} usuarios promedio/hora")
            
            elif "Cache" in selected_metric:
                st.metric("💾 Eficiencia acumulada", f"{result:.1f}%·hora")
                st.info(f"💡 Eficiencia promedio: {result/24:.1f}% durante 24h")
            
            elif "Latencia" in selected_metric:
                st.metric("⚡ Latencia acumulada", f"{result:.0f} ms·hora")
                st.info(f"💡 Latencia promedio: {result/24:.1f} ms durante 24h")
            
            st.info(f"🔧 Método usado: {details.get('method_used', 'Numérico')}")
            
        else:
            st.error(f"❌ Error: {result}")
    
    except Exception as e:
        st.error(f"Error en cálculo: {str(e)}")

def calculate_riemann_sum(current_metric, selected_metric, method, n_samples):
    """Calcular suma de Riemann."""
    try:
        from utils.calculator import calculate_riemann_sum_robust
        
        with st.spinner(f"📊 Calculando Riemann {method} con {n_samples} muestras..."):
            riemann_result, riemann_details = calculate_riemann_sum_robust(
                current_metric['function'], 
                float(current_metric['lower']), 
                float(current_metric['upper']), 
                n_samples, method, current_metric['variable']
            )
        
        if riemann_result[0]:  # Si fue exitoso
            st.success(f"### 📐 Aproximación: {riemann_result[1]:.2f} {current_metric['units']}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("📊 Método", method.title())
                st.metric("🔢 Muestras", f"{n_samples}")
                
            with col2:
                accuracy = abs(riemann_result[1]) / max(abs(riemann_result[1]), 1) * 100
                st.metric("📈 Confiabilidad", f"{min(accuracy, 99):.1f}%")
            
            st.info(f"""
            💡 **Interpretación para {selected_metric}:**
            - Aproximación con {n_samples} mediciones discretas
            - Método {method}: {'Conservador' if method == 'left' else 'Optimista' if method == 'right' else 'Balanceado'}
            - Útil para monitoreo en tiempo real del sistema
            """)
        else:
            st.error(f"❌ Error en Riemann: {riemann_result[1]}")
    
    except Exception as e:
        st.error(f"Error en Riemann: {str(e)}")

def plot_riemann_visualization(current_metric, method, n_samples):
    """Visualizar aproximación de Riemann."""
    try:
        from utils.plotting import plot_riemann_sum
        
        plot_riemann_sum(
            current_metric['function'],
            float(current_metric['lower']),
            float(current_metric['upper']),
            n_samples,
            method,
            current_metric['variable']
        )
    except Exception as e:
        st.error(f"Error en visualización: {str(e)}")

def calculate_area_analysis(current_metric, selected_metric, period_info):
    """Calcular área para período específico."""
    try:
        from utils.calculator import calculate_definite_integral_robust
        
        start_hour, end_hour, description = period_info
        
        with st.spinner(f"🔵 Calculando área del período {start_hour}-{end_hour}h..."):
            success, result, details = calculate_definite_integral_robust(
                current_metric['function'], str(start_hour), str(end_hour), current_metric['variable']
            )
        
        if success:
            st.success(f"### 🔵 Área del Período: {result:.2f} {current_metric['units']}")
            
            # Porcentaje del total diario
            total_success, total_result, _ = calculate_definite_integral_robust(
                current_metric['function'], "0", "24", current_metric['variable']
            )
            
            if total_success:
                percentage = (result / total_result) * 100
                st.metric("📊 % del Total Diario", f"{percentage:.1f}%")
            
            st.info(f"""
            **🕒 Período:** {start_hour}:00 - {end_hour}:00  
            **📝 Contexto:** {description}  
            **📈 Contribución:** Este período representa el impacto acumulado en {description.lower()}
            """)
            
        else:
            st.error(f"❌ Error: {result}")
    
    except Exception as e:
        st.error(f"Error en análisis de área: {str(e)}")

def calculate_volume_revolution_fixed(current_metric, selected_metric, axis):
    """Calcular volumen de sólido de revolución."""
    try:
        from utils.calculator import calculate_definite_integral_robust
        
        # Volumen: V = π ∫ [f(x)]² dx
        volume_function = f"3.14159 * ({current_metric['function']})**2"
        
        with st.spinner(f"🔄 Calculando volumen 3D para {selected_metric}..."):
            success, result, details = calculate_definite_integral_robust(
                volume_function, current_metric['lower'], current_metric['upper'], current_metric['variable']
            )
        
        if success:
            st.success(f"### 🔄 Volumen 3D: {result:.2f} unidades³")
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.info(f"""
                **🎯 Interpretación del Volumen Tridimensional:**
                - **Eje de revolución:** {axis}
                - **Volumen calculado:** {result:.2f} unidades cúbicas
                - **Método:** {details.get('method_used', 'Numérico')}
                
                **🏗️ Aplicación en infraestructura:**
                - **Escalamiento cúbico:** Crecimiento volumétrico del sistema
                - **Dimensionamiento:** Capacidad total de procesamiento 3D
                - **Arquitectura distribuida:** Planificación de clusters
                
                💡 **Significado empresarial:** El volumen modela la capacidad 
                tridimensional necesaria para manejar {selected_metric.lower()}.
                """)
                
                # Estimaciones prácticas
                if "Usuarios" in selected_metric:
                    servers = result / 1000000
                    st.metric("🖥️ Servidores estimados", f"{servers:.0f}")
                elif "Cache" in selected_metric:
                    efficiency = min(result / 100000 * 10, 50)
                    st.metric("⚡ Mejora eficiencia", f"+{efficiency:.1f}%")
                
                # ✅ AGREGAR BOTÓN PARA VER 3D
                if st.button("🎯 Ver Visualización 3D", key=f"view_3d_{selected_metric}"):
                    st.markdown("#### 🔄 Sólido de Revolución en 3D")
                    from utils.plotting import plot_volume_3d
                    plot_volume_3d(current_metric['function'], current_metric['lower'], 
                                 current_metric['upper'], current_metric['variable'])
            
            with col2:
                st.markdown(f"#### 🔄 Función Original - {selected_metric}")
                plot_integral(current_metric['function'], current_metric['lower'], 
                            current_metric['upper'], current_metric['variable'])
                
                st.info(f"""
                **📊 Fórmula aplicada:**
                V = π ∫ [f(t)]² dt
                
                La función mostrada se eleva al cuadrado y se multiplica por π 
                para obtener el volumen del sólido de revolución.
                """)
                
                # ✅ AGREGAR BOTÓN PARA COMPARACIÓN 2D vs 3D
                if st.button("🔄 Comparar 2D vs 3D", key=f"compare_3d_{selected_metric}"):
                    st.markdown("#### 📊 Comparación 2D vs 3D")
                    from utils.plotting import plot_3d_comparison
                    plot_3d_comparison(current_metric['function'], current_metric['lower'], 
                                     current_metric['upper'], current_metric['variable'])
                
        else:
            st.error(f"❌ Error calculando volumen: {result}")
    except Exception as e:
        st.error(f"Error en cálculo de volumen: {str(e)}")

def interpret_volume_engineering_fixed(current_metric, selected_metric):
    """Interpretación avanzada del volumen para ingeniería."""
    st.markdown(f"#### 🎯 Interpretación Avanzada - {selected_metric}")
    
    st.markdown(f"""
    **🏗️ Aplicaciones del Volumen en Ingeniería de Software:**
    
    **Para {selected_metric}:**
    
    **📊 Perspectiva Arquitectural:**
    - **Microservicios:** Volumen indica escalamiento de servicios
    - **Load Balancing:** Distribución tridimensional de carga
    - **Auto-scaling:** Crecimiento horizontal y vertical
    - **CDN:** Distribución geográfica optimizada
    
    **💼 Perspectiva de Negocio:**
    - **Planificación de Capacidad:** Recursos necesarios a largo plazo
    - **Estimación de Costos:** Presupuestos basados en volumen
    - **SLA Management:** Capacidad para cumplir acuerdos
    - **Inversión en Infraestructura:** ROI basado en capacidad volumétrica
    
    **🔧 Implementación Técnica:**
    - **Kubernetes:** Dimensionamiento de pods y nodos
    - **Database Sharding:** Particionamiento volumétrico
    - **Cache Layers:** Distribución jerárquica de cache
    - **Network Topology:** Diseño de redes escalables
    
    **💡 Valor Empresarial:**
    El análisis volumétrico transforma métricas 2D en insights 3D 
    para decisiones estratégicas de arquitectura escalable.
    """)

def show_3d_volume_section(current_metric, selected_metric):
    """Sección dedicada para visualización 3D."""
    st.markdown("### 🔄 Visualización 3D del Volumen")
    
    # Opciones de visualización
    viz_option = st.radio(
        "🎯 Tipo de visualización:",
        ["📈 Función 2D", "🔄 Sólido 3D", "🔀 Comparación 2D vs 3D"],
        key="viz_3d_option"
    )
    
    if viz_option == "📈 Función 2D":
        st.markdown("#### 📈 Función Original")
        plot_integral(current_metric['function'], current_metric['lower'], 
                     current_metric['upper'], current_metric['variable'])
    
    elif viz_option == "🔄 Sólido 3D":
        st.markdown("#### 🔄 Sólido de Revolución en 3D")
        from utils.plotting import plot_volume_3d
        plot_volume_3d(current_metric['function'], current_metric['lower'], 
                      current_metric['upper'], current_metric['variable'])
    
    elif viz_option == "🔀 Comparación 2D vs 3D":
        st.markdown("#### 🔀 Comparación 2D vs 3D")
        from utils.plotting import plot_3d_comparison
        plot_3d_comparison(current_metric['function'], current_metric['lower'], 
                          current_metric['upper'], current_metric['variable'])