import streamlit as st
import numpy as np
from utils.calculator import solve_integral
from utils.plotting import plot_integral
from components.solution_display import display_solution, display_error_message
from assets.translations import get_text

def show():
    """Display software engineering scenarios related to integrals."""
    
    st.title("🏗️ Cálculo en Ingeniería de Software")
    st.markdown("**Descubre cómo el cálculo integral impulsa la innovación tecnológica**")
    
    # Navigation tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "🎯 Escenarios Prácticos",
        "📚 Teoría y Aplicaciones", 
        "🎥 Recursos Educativos",
        "💼 Aplicaciones Profesionales"
    ])
    
    with tab1:
        show_practical_scenarios()
    
    with tab2:
        show_theory_and_applications()
    
    with tab3:
        show_educational_resources()
    
    with tab4:
        show_professional_applications()

def show_practical_scenarios():
    """Show practical software engineering scenarios with calculus applications."""
    st.markdown("## 🎯 Escenarios Prácticos de Ingeniería de Software")
    st.markdown("Explora aplicaciones reales del cálculo integral en desarrollo de software")
    
    # Define scenarios directly here to avoid import issues
    scenarios = [
        {
            "title": "Optimización de Algoritmos",
            "context": "Análisis de complejidad temporal de algoritmo de ordenamiento",
            "function": "2*t**2 + 5*t",
            "bounds": [0, 10],
            "unit": "milisegundos",
            "variable": "t",
            "explanation": "Esta integral calcula el tiempo total de ejecución cuando la complejidad temporal es cuadrática.",
            "real_application": "Algoritmos como Bubble Sort, Selection Sort en sistemas reales"
        },
        {
            "title": "Machine Learning - Función de Pérdida",
            "context": "Calcular la pérdida total durante entrenamiento de red neuronal",
            "function": "exp(-0.1*t)",
            "bounds": [0, 50],
            "unit": "unidades de error",
            "variable": "t",
            "explanation": "La integral de la función de pérdida nos da el error total acumulado durante el entrenamiento.",
            "real_application": "Optimización en TensorFlow, PyTorch, Keras"
        },
        {
            "title": "Análisis de Tráfico Web",
            "context": "Tráfico total de datos en servidor durante 24 horas",
            "function": "1000*sin(3.14159*t/12) + 1500",
            "bounds": [0, 24],
            "unit": "MB/hora",
            "variable": "t",
            "explanation": "Calcular el volumen total de datos transferido con patrones cíclicos diarios.",
            "real_application": "CDNs como Cloudflare, AWS CloudFront"
        },
        {
            "title": "Optimización de Cache",
            "context": "Hit rate óptimo de cache para minimizar latencia",
            "function": "100/(1 + exp(-0.5*(t-10)))",
            "bounds": [0, 20],
            "unit": "% hit rate",
            "variable": "t",
            "explanation": "Función sigmoide que modela cómo mejora el hit rate conforme aumenta el tamaño del cache.",
            "real_application": "Sistemas de cache en Redis, Memcached, bases de datos"
        },
        {
            "title": "Análisis de Ciberseguridad",
            "context": "Entropía total de sistema de contraseñas",
            "function": "log(t)*t",
            "bounds": [1, 32],
            "unit": "bits de entropía",
            "variable": "t",
            "explanation": "La entropía acumulada determina la fortaleza criptográfica del sistema.",
            "real_application": "Generadores de contraseñas, análisis de seguridad"
        }
    ]
    
    # Scenario selector
    col1, col2 = st.columns([2, 1])
    
    with col1:
        selected_scenario = st.selectbox(
            "Selecciona un escenario:",
            range(len(scenarios)),
            format_func=lambda x: scenarios[x]["title"],
            key="scenario_selector"
        )
    
    with col2:
        if st.button("🎲 Escenario Aleatorio", key="random_scenario"):
            import random
            selected_scenario = random.randint(0, len(scenarios) - 1)
            st.session_state.scenario_selector = selected_scenario
            st.rerun()
    
    # Display selected scenario
    scenario = scenarios[selected_scenario]
    
    st.markdown(f"### 🔍 {scenario['title']}")
    st.info(f"**Contexto:** {scenario['context']}")
    st.markdown(f"**Aplicación real:** {scenario['real_application']}")
    
    # Display function and bounds
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"**Función:** `{scenario['function']}`")
    with col2:
        st.markdown(f"**Límites:** [{scenario['bounds'][0]}, {scenario['bounds'][1]}]")
    with col3:
        st.markdown(f"**Unidad:** {scenario['unit']}")
    
    # Calculate and display result
    if st.button("🧮 Calcular Integral", key="calculate_scenario"):
        try:
            result, steps = solve_integral(
                scenario['function'], 
                str(scenario['bounds'][0]), 
                str(scenario['bounds'][1]), 
                scenario['variable']
            )
            
            st.success(f"**Resultado:** {result:.4f} {scenario['unit']}")
            
            # Show plot
            try:
                plot_integral(
                    scenario['function'],
                    str(scenario['bounds'][0]),
                    str(scenario['bounds'][1]),
                    scenario['variable']
                )
            except Exception as e:
                st.warning("No se pudo generar la gráfica")
            
            # Show explanation
            st.markdown("### 💡 Explicación")
            st.markdown(scenario['explanation'])
            
            # Show steps
            with st.expander("👁️ Ver pasos de la solución"):
                for step in steps:
                    st.markdown(f"• {step}")
                    
        except Exception as e:
            display_error_message("calculation_error", str(e))

def show_theory_and_applications():
    """Show theory and applications of calculus in software engineering."""
    st.markdown("## 📚 Teoría y Aplicaciones del Cálculo en Software")
    
    applications = [
        {
            "category": "🚀 Optimización de Rendimiento",
            "description": "Uso del cálculo para optimizar sistemas de software",
            "applications": [
                "Análisis de complejidad temporal y espacial",
                "Optimización de algoritmos de búsqueda y ordenamiento",
                "Gestión eficiente de memoria y recursos",
                "Balanceadores de carga adaptativos"
            ],
            "math_concepts": [
                "Derivadas para encontrar puntos óptimos",
                "Integrales para calcular costos totales",
                "Límites para análisis asintótico"
            ]
        },
        {
            "category": "🤖 Machine Learning e IA",
            "description": "Fundamentos matemáticos del aprendizaje automático",
            "applications": [
                "Backpropagation en redes neuronales",
                "Optimización de funciones de pérdida",
                "Análisis de convergencia en algoritmos",
                "Procesamiento de señales y imágenes"
            ],
            "math_concepts": [
                "Gradientes y derivadas parciales",
                "Integrales para distribuciones de probabilidad",
                "Ecuaciones diferenciales para dinámicas"
            ]
        },
        {
            "category": "🎮 Gráficos por Computadora",
            "description": "Matemáticas avanzadas para rendering y simulación",
            "applications": [
                "Ray tracing y path tracing",
                "Física de partículas y fluidos",
                "Animaciones procedurales",
                "Iluminación global y sombras"
            ],
            "math_concepts": [
                "Integrales de Monte Carlo",
                "Ecuaciones de renderizado",
                "Transformadas de Fourier"
            ]
        },
        {
            "category": "🔐 Criptografía y Seguridad",
            "description": "Matemáticas para protección de información",
            "applications": [
                "Generación de números aleatorios",
                "Análisis de entropía",
                "Protocolos criptográficos",
                "Detección de anomalías"
            ],
            "math_concepts": [
                "Teoría de números",
                "Análisis estadístico",
                "Funciones hash"
            ]
        }
    ]
    
    for app in applications:
        with st.expander(f"**{app['category']}** - {app['description']}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Aplicaciones Prácticas:**")
                for item in app['applications']:
                    st.markdown(f"• {item}")
            
            with col2:
                st.markdown("**Conceptos Matemáticos:**")
                for concept in app['math_concepts']:
                    st.markdown(f"• {concept}")

def show_educational_resources():
    """Show educational resources for learning calculus in software engineering."""
    st.markdown("## 🎥 Recursos Educativos")
    st.markdown("Enlaces a videos, cursos y material educativo sobre aplicaciones del cálculo en software")
    
    resources = {
        "Videos y Cursos": [
            {
                "title": "3Blue1Brown - Essence of Calculus",
                "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr",
                "description": "Visualización intuitiva del cálculo y sus aplicaciones en tecnología",
                "type": "🎥 Serie de videos"
            },
            {
                "title": "MIT 18.01SC - Single Variable Calculus",
                "url": "https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/",
                "description": "Curso completo del MIT aplicado a ciencias e ingeniería",
                "type": "🎓 Curso universitario"
            },
            {
                "title": "Khan Academy - Calculus Applications",
                "url": "https://www.khanacademy.org/math/ap-calculus-ab",
                "description": "Aplicaciones prácticas del cálculo con ejercicios interactivos",
                "type": "📚 Plataforma educativa"
            },
            {
                "title": "Coursera - Machine Learning Mathematics",
                "url": "https://www.coursera.org/specializations/mathematics-machine-learning",
                "description": "Matemáticas específicas para machine learning incluyendo cálculo",
                "type": "💻 Curso online"
            }
        ],
        
        "Libros y Referencias": [
            {
                "title": "Calculus for Computer Graphics",
                "url": "https://www.amazon.com/Calculus-Computer-Graphics-John-Vince/dp/1447173791",
                "description": "Aplicaciones específicas del cálculo en gráficos por computadora",
                "type": "📖 Libro especializado"
            },
            {
                "title": "Mathematics for Computer Science - MIT",
                "url": "https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/",
                "description": "Fundamentos matemáticos completos para CS",
                "type": "📚 Material académico"
            },
            {
                "title": "Pattern Recognition and Machine Learning",
                "url": "https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf",
                "description": "Fundamentos matemáticos del aprendizaje automático",
                "type": "📄 Libro académico"
            }
        ],
        
        "Herramientas Prácticas": [
            {
                "title": "NumPy y SciPy",
                "url": "https://scipy-lectures.org/",
                "description": "Implementación práctica de métodos numéricos en Python",
                "type": "🛠️ Tutorial práctico"
            },
            {
                "title": "Wolfram Alpha",
                "url": "https://www.wolframalpha.com/",
                "description": "Calculadora avanzada para verificar cálculos complejos",
                "type": "🔧 Herramienta online"
            },
            {
                "title": "GeoGebra",
                "url": "https://www.geogebra.org/",
                "description": "Visualización interactiva de funciones y conceptos matemáticos",
                "type": "📊 Simulador"
            }
        ]
    }
    
    for category, items in resources.items():
        st.markdown(f"### {category}")
        
        for resource in items:
            with st.expander(f"{resource['type']} - {resource['title']}"):
                st.markdown(f"**Descripción:** {resource['description']}")
                st.markdown(f"**Enlace:** [{resource['title']}]({resource['url']})")
                
                if "3Blue1Brown" in resource['title']:
                    st.success("💡 **Altamente recomendado** - Excelente para comprensión visual")
                elif "MIT" in resource['title']:
                    st.info("🎓 **Nivel universitario** - Contenido riguroso y completo")
                elif "Khan Academy" in resource['title']:
                    st.warning("📚 **Para principiantes** - Explicaciones claras paso a paso")

def show_professional_applications():
    """Show professional applications and career opportunities."""
    st.markdown("## 💼 Aplicaciones Profesionales")
    st.markdown("Cómo el cálculo impulsa carreras en tecnología")
    
    careers = [
        {
            "role": "🤖 Ingeniero de Machine Learning",
            "description": "Desarrolla sistemas de inteligencia artificial",
            "calculus_use": [
                "Optimización de funciones de pérdida",
                "Análisis de convergencia de algoritmos",
                "Backpropagation en redes neuronales",
                "Procesamiento de señales"
            ],
            "companies": ["Google", "OpenAI", "Tesla", "Meta"],
            "salary_range": "$120,000 - $300,000 USD"
        },
        {
            "role": "🎮 Desarrollador de Videojuegos",
            "description": "Crea experiencias interactivas inmersivas",
            "calculus_use": [
                "Física de partículas y fluidos",
                "Algoritmos de iluminación (ray tracing)",
                "Animaciones procedurales",
                "Optimización de rendimiento"
            ],
            "companies": ["Epic Games", "Unity", "Blizzard", "Ubisoft"],
            "salary_range": "$85,000 - $180,000 USD"
        },
        {
            "role": "📊 Científico de Datos",
            "description": "Extrae insights de grandes volúmenes de datos",
            "calculus_use": [
                "Análisis estadístico avanzado",
                "Modelos probabilísticos",
                "Optimización de métricas",
                "Análisis de series temporales"
            ],
            "companies": ["Netflix", "Spotify", "Airbnb", "Uber"],
            "salary_range": "$95,000 - $200,000 USD"
        },
        {
            "role": "☁️ Arquitecto de Sistemas",
            "description": "Diseña infraestructura tecnológica escalable",
            "calculus_use": [
                "Optimización de recursos",
                "Análisis de capacidad",
                "Modelado de tráfico",
                "Predicción de carga"
            ],
            "companies": ["Amazon AWS", "Microsoft Azure", "Cloudflare"],
            "salary_range": "$130,000 - $250,000 USD"
        }
    ]
    
    for career in careers:
        with st.expander(f"**{career['role']}** - {career['description']}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Aplicaciones del Cálculo:**")
                for use in career['calculus_use']:
                    st.markdown(f"• {use}")
                    
                st.markdown(f"**Rango Salarial:** {career['salary_range']}")
            
            with col2:
                st.markdown("**Empresas que Contratan:**")
                for company in career['companies']:
                    st.markdown(f"• {company}")
    
    # Success stories section
    st.markdown("### 🌟 Historias de Éxito")
    st.info("""
    **¿Sabías que...?**
    
    • **Elon Musk** usa cálculo para optimizar las trayectorias de cohetes SpaceX
    • **Los algoritmos de Netflix** usan integrales para personalizar recomendaciones
    • **Google PageRank** se basa en matrices y cálculo vectorial
    • **Las criptomonedas** usan matemáticas avanzadas para proof-of-work
    • **Los videojuegos AAA** implementan física realista usando ecuaciones diferenciales
    """)
    
    st.markdown("### 🚀 Próximos Pasos")
    st.success("""
    **Para comenzar tu carrera en tech:**
    
    1. 📚 **Domina los fundamentos** - Cálculo, álgebra lineal, estadística
    2. 💻 **Aprende programación** - Python, JavaScript, o tu lenguaje preferido  
    3. 🔨 **Construye proyectos** - Aplica matemáticas en proyectos reales
    4. 🌐 **Comparte tu trabajo** - GitHub, portafolio online, blog técnico
    5. 🤝 **Conecta con la comunidad** - Meetups, conferencias, redes sociales
    
    ¡El cálculo que aprendes hoy será la base de la innovación del mañana! 🌟
    """)
    
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
        
        **Unidad:** {scenario.get('unit', 'unidades por minuto')}
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
