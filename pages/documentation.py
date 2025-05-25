import streamlit as st
from assets.enhanced_study_plans import installation_documentation, faq_section, additional_learning_resources

def show():
    """Display comprehensive documentation for installation and usage."""
    st.title("📖 Documentación Completa")
    st.markdown("Guía completa para instalar, usar y aprovechar al máximo tu Calculadora Matemática")
    
    # Navigation tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "🔧 Instalación", 
        "🚀 Guía de Uso", 
        "❓ FAQ", 
        "📚 Recursos Adicionales"
    ])
    
    with tab1:
        show_installation_guide()
    
    with tab2:
        show_usage_guide()
    
    with tab3:
        show_faq()
    
    with tab4:
        show_additional_resources()

def show_installation_guide():
    """Display installation instructions."""
    st.markdown("# 🔧 Guía de Instalación")
    st.markdown("Sigue estos pasos para tener la calculadora funcionando en tu computadora")
    
    for section in installation_documentation["sections"]:
        if section["title"] == "🔧 Instalación":
            for step_info in section["content"]:
                with st.expander(f"**{step_info['step']}**: {step_info['description']}", expanded=False):
                    st.markdown(f"### {step_info['description']}")
                    
                    for detail in step_info["details"]:
                        st.markdown(f"• {detail}")
                    
                    # Special handling for different steps
                    if "Python" in step_info["step"]:
                        st.code("""
# Verificar instalación de Python
python --version

# Debería mostrar algo como: Python 3.11.x
                        """, language="bash")
                    
                    elif "Dependencias" in step_info["step"]:
                        st.code("""
# Opción 1: Usar requirements.txt
pip install -r requirements.txt

# Opción 2: Instalar manualmente
pip install streamlit sympy matplotlib plotly numpy
                        """, language="bash")
                        
                        # Show requirements.txt content
                        st.markdown("**Contenido del archivo requirements.txt:**")
                        st.code("""
streamlit>=1.28.0
sympy==1.11.1
matplotlib>=3.7.0
plotly>=5.15.0
numpy>=1.24.0
                        """, language="text")
                    
                    elif "Ejecutar" in step_info["step"]:
                        st.code("""
# Ejecutar la aplicación
streamlit run app.py

# La aplicación estará disponible en:
# http://localhost:8501
                        """, language="bash")
                        
                        st.success("🎉 ¡Una vez que veas 'You can now view your Streamlit app in your browser', estarás listo!")

def show_usage_guide():
    """Display usage instructions."""
    st.markdown("# 🚀 Guía de Uso Rápido")
    st.markdown("Aprende a usar todas las funciones de la calculadora")
    
    # Quick start
    st.markdown("## ⚡ Inicio Rápido")
    st.markdown("""
    1. 🌐 **Abre la aplicación** en tu navegador (normalmente http://localhost:8501)
    2. 🧮 **Selecciona una calculadora** del menú lateral
    3. ✏️ **Ingresa tu función** usando sintaxis de Python
    4. 📊 **Obtén resultados** con gráficas y explicaciones paso a paso
    """)
    
    # Feature guides
    for section in installation_documentation["sections"]:
        if section["title"] == "🚀 Guía de Uso Rápido":
            for feature_info in section["content"]:
                with st.expander(f"📱 **{feature_info['feature']}**", expanded=False):
                    st.markdown(f"### Cómo usar {feature_info['feature']}")
                    
                    for i, step in enumerate(feature_info["steps"], 1):
                        st.markdown(f"**{step}**")
                    
                    # Add visual examples
                    if "Integrales" in feature_info["feature"]:
                        st.markdown("**Ejemplos de funciones:**")
                        st.code("""
# Funciones básicas
x**2          # x al cuadrado
2*x + 1       # función lineal
sin(x)        # función seno
exp(x)        # función exponencial
log(x)        # logaritmo natural

# Funciones complejas
x**3 - 2*x**2 + x - 1    # polinomio
sin(x) * cos(x)          # producto trigonométrico
exp(-x**2)               # gaussiana
                        """, language="python")
                    
                    elif "Riemann" in feature_info["feature"]:
                        st.markdown("**Métodos disponibles:**")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.info("**Izquierdo**\nUsa el extremo izquierdo de cada rectángulo")
                        with col2:
                            st.warning("**Derecho**\nUsa el extremo derecho de cada rectángulo")
                        with col3:
                            st.success("**Medio**\nUsa el punto medio (más preciso)")
    
    # Syntax guide
    st.markdown("## 📝 Guía de Sintaxis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ✅ **Sintaxis Correcta**")
        syntax_examples = [
            ("Potencias", "x**2, x**3", "No x^2"),
            ("Multiplicación", "2*x, x*y", "Siempre usar *"),
            ("Exponencial", "exp(x)", "No e^x"),
            ("Logaritmo", "log(x)", "Logaritmo natural"),
            ("Trigonométricas", "sin(x), cos(x)", "Funciones en radianes"),
            ("Constantes", "pi, e", "Constantes predefinidas")
        ]
        
        for desc, correct, note in syntax_examples:
            st.markdown(f"**{desc}:** `{correct}`")
            st.caption(note)
    
    with col2:
        st.markdown("### ❌ **Errores Comunes**")
        common_errors = [
            "x^2 → Usar x**2",
            "2x → Usar 2*x", 
            "e^x → Usar exp(x)",
            "ln(x) → Usar log(x)",
            "sen(x) → Usar sin(x)",
            "√x → Usar sqrt(x)"
        ]
        
        for error in common_errors:
            st.markdown(f"• {error}")

def show_faq():
    """Display frequently asked questions."""
    st.markdown("# ❓ Preguntas Frecuentes")
    
    for i, qa in enumerate(faq_section["questions"]):
        with st.expander(f"**{qa['q']}**", expanded=False):
            st.markdown(qa["a"])
            
            # Add visual examples for certain questions
            if "función" in qa["q"].lower() and "sintaxis" in qa["a"].lower():
                st.markdown("**Ejemplo visual:**")
                col1, col2 = st.columns(2)
                with col1:
                    st.error("❌ Incorrecto")
                    st.code("x^2 + sen(x)")
                with col2:
                    st.success("✅ Correcto")
                    st.code("x**2 + sin(x)")
    
    # Troubleshooting section
    st.markdown("## 🔧 Solución de Problemas")
    
    troubleshooting = [
        {
            "problem": "La aplicación no se abre",
            "solutions": [
                "Verifica que Streamlit esté instalado: `pip show streamlit`",
                "Asegúrate de estar en la carpeta correcta del proyecto",
                "Prueba con: `python -m streamlit run app.py`",
                "Revisa que no haya otro proceso usando el puerto 8501"
            ]
        },
        {
            "problem": "Error al calcular integrales",
            "solutions": [
                "Revisa la sintaxis de la función (usar ** en lugar de ^)",
                "Verifica que los límites sean números válidos",
                "Asegúrate de que la función esté definida en el intervalo",
                "Intenta con una función más simple primero"
            ]
        },
        {
            "problem": "Las gráficas no se muestran",
            "solutions": [
                "Reinstala matplotlib: `pip install --upgrade matplotlib`",
                "Verifica que plotly esté actualizado: `pip install --upgrade plotly`",
                "Reinicia la aplicación completamente",
                "Comprueba la consola del navegador para errores"
            ]
        }
    ]
    
    for item in troubleshooting:
        with st.expander(f"🚨 **{item['problem']}**"):
            st.markdown("**Posibles soluciones:**")
            for solution in item["solutions"]:
                st.markdown(f"• {solution}")

def show_additional_resources():
    """Display additional learning resources."""
    st.markdown("# 📚 Recursos Adicionales de Aprendizaje")
    st.markdown("Enlaces a recursos externos para profundizar tu conocimiento")
    
    for category in additional_learning_resources["categories"]:
        st.markdown(f"## 🔗 {category['category']}")
        
        for resource in category["resources"]:
            with st.expander(f"📖 **{resource['name']}**"):
                st.markdown(f"**Descripción:** {resource['description']}")
                st.markdown(f"**Enlace:** [{resource['name']}]({resource['url']})")
                
                # Add specific recommendations
                if "Khan Academy" in resource["name"]:
                    st.success("💡 **Recomendado para principiantes** - Explicaciones claras y ejercicios interactivos")
                elif "MIT" in resource["name"]:
                    st.info("🎓 **Nivel universitario** - Contenido riguroso y completo")
                elif "3Blue1Brown" in resource["name"]:
                    st.warning("🎥 **Altamente visual** - Excelente para entender conceptos intuitivamente")
                
                if st.button(f"Visitar {resource['name']}", key=f"visit_{resource['name']}", help="Se abrirá en una nueva pestaña"):
                    st.markdown(f"🌐 **Dirígete a:** {resource['url']}")
    
    # Study tips
    st.markdown("## 💡 Consejos de Estudio")
    
    study_tips = [
        {
            "tip": "📅 Estudia Regularmente",
            "description": "Dedica al menos 30 minutos diarios a practicar integrales"
        },
        {
            "tip": "✍️ Practica a Mano",
            "description": "Resuelve problemas en papel antes de usar la calculadora"
        },
        {
            "tip": "📊 Visualiza Siempre",
            "description": "Usa las gráficas para entender qué representa cada integral"
        },
        {
            "tip": "🔄 Repite Ejemplos",
            "description": "Resuelve el mismo problema con diferentes métodos"
        },
        {
            "tip": "👥 Estudia en Grupo",
            "description": "Explica conceptos a otros para reforzar tu comprensión"
        },
        {
            "tip": "🎯 Enfócate en Conceptos",
            "description": "Entiende el 'por qué' antes de memorizar fórmulas"
        }
    ]
    
    cols = st.columns(2)
    for i, tip in enumerate(study_tips):
        with cols[i % 2]:
            st.info(f"**{tip['tip']}**\n\n{tip['description']}")
    
    # Final motivation
    st.markdown("---")
    st.balloons()
    st.success("""
    🌟 **¡Recuerda!** 
    
    El dominio de las matemáticas viene con la práctica constante. 
    Esta calculadora es tu herramienta, pero el verdadero aprendizaje 
    ocurre cuando entiendes los conceptos detrás de cada cálculo.
    
    ¡Sigue practicando y verás resultados increíbles! 💪
    """)