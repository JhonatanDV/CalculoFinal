# Plan de Estudios Ampliado con Enlaces a Recursos Reales

# Plan de Estudios Mejorado para Integrales Definidas
enhanced_definite_integrals_plan = {
    "title": "📚 Plan de Estudios Completo: Integrales Definidas",
    "description": "Guía completa con recursos externos para dominar las integrales definidas",
    "modules": [
        {
            "level": "Básico",
            "title": "1. Fundamentos de Integrales",
            "duration": "2-3 semanas",
            "topics": [
                "Concepto de área bajo la curva",
                "Notación de integrales definidas",
                "Teorema Fundamental del Cálculo",
                "Propiedades básicas de integrales"
            ],
            "resources": [
                {
                    "type": "video",
                    "title": "Khan Academy - Introducción a Integrales",
                    "url": "https://www.khanacademy.org/math/ap-calculus-ab/ab-integration-new",
                    "description": "Videos gratuitos explicando conceptos básicos"
                },
                {
                    "type": "texto",
                    "title": "MIT OpenCourseWare - Cálculo",
                    "url": "https://ocw.mit.edu/courses/mathematics/18-01sc-single-variable-calculus-fall-2010/",
                    "description": "Curso completo del MIT disponible gratis"
                },
                {
                    "type": "práctica",
                    "title": "Wolfram Alpha",
                    "url": "https://www.wolframalpha.com/",
                    "description": "Verificar cálculos y ver pasos detallados"
                }
            ],
            "examples": [
                {
                    "function": "2*x",
                    "bounds": ["0", "3"],
                    "explanation": "Integral básica de función lineal - representa área de triángulo",
                    "difficulty": "⭐"
                },
                {
                    "function": "x**2",
                    "bounds": ["0", "2"],
                    "explanation": "Integral de función cuadrática - área bajo parábola",
                    "difficulty": "⭐⭐"
                }
            ]
        },
        {
            "level": "Intermedio",
            "title": "2. Funciones Trigonométricas y Exponenciales",
            "duration": "3-4 semanas",
            "topics": [
                "Integrales de sin(x), cos(x), tan(x)",
                "Integrales de funciones exponenciales",
                "Técnicas de sustitución simple",
                "Integración por partes básica"
            ],
            "resources": [
                {
                    "type": "video",
                    "title": "Professor Leonard - Integrales Trigonométricas",
                    "url": "https://www.youtube.com/user/professorleonard57",
                    "description": "Explicaciones detalladas con ejemplos"
                },
                {
                    "type": "libro",
                    "title": "Paul's Online Math Notes",
                    "url": "https://tutorial.math.lamar.edu/Classes/CalcI/CalcI.aspx",
                    "description": "Notas completas de cálculo con ejemplos"
                },
                {
                    "type": "simulador",
                    "title": "GeoGebra Calculadora",
                    "url": "https://www.geogebra.org/calculator",
                    "description": "Visualización interactiva de integrales"
                }
            ],
            "examples": [
                {
                    "function": "sin(x)",
                    "bounds": ["0", "3.14159"],
                    "explanation": "Integral de seno en medio período",
                    "difficulty": "⭐⭐⭐"
                },
                {
                    "function": "exp(x)",
                    "bounds": ["0", "2"],
                    "explanation": "Crecimiento exponencial",
                    "difficulty": "⭐⭐⭐"
                }
            ]
        },
        {
            "level": "Avanzado",
            "title": "3. Técnicas Avanzadas de Integración",
            "duration": "4-5 semanas",
            "topics": [
                "Integración por partes",
                "Sustitución trigonométrica",
                "Fracciones parciales",
                "Integrales impropias"
            ],
            "resources": [
                {
                    "type": "curso",
                    "title": "Coursera - Calculus for Engineers",
                    "url": "https://www.coursera.org/learn/calculus-for-engineers",
                    "description": "Curso universitario con aplicaciones"
                },
                {
                    "type": "referencia",
                    "title": "Integral Table",
                    "url": "https://en.wikipedia.org/wiki/Lists_of_integrals",
                    "description": "Tabla completa de integrales"
                },
                {
                    "type": "práctica",
                    "title": "Symbolab Calculator",
                    "url": "https://www.symbolab.com/",
                    "description": "Solver de integrales con pasos"
                }
            ],
            "examples": [
                {
                    "function": "x*sin(x)",
                    "bounds": ["0", "3.14159"],
                    "explanation": "Integración por partes",
                    "difficulty": "⭐⭐⭐⭐"
                },
                {
                    "function": "log(x)",
                    "bounds": ["1", "5"],
                    "explanation": "Función logarítmica",
                    "difficulty": "⭐⭐⭐⭐"
                }
            ]
        }
    ],
    "assessment": {
        "quizzes": [
            "Quiz 1: Conceptos básicos (después del módulo 1)",
            "Quiz 2: Funciones trigonométricas (después del módulo 2)",
            "Examen final: Técnicas mixtas (después del módulo 3)"
        ],
        "projects": [
            "Proyecto 1: Calcular área de figuras geométricas",
            "Proyecto 2: Análisis de funciones de ingeniería",
            "Proyecto final: Aplicación completa de integrales"
        ]
    }
}

# Documentación de instalación y uso
installation_documentation = {
    "title": "📖 Documentación: Instalación y Uso",
    "sections": [
        {
            "title": "🔧 Instalación",
            "content": [
                {
                    "step": "1. Requisitos del Sistema",
                    "description": "Python 3.8 o superior",
                    "details": [
                        "Windows 10/11, macOS 10.14+, o Linux Ubuntu 18.04+",
                        "4GB RAM mínimo (8GB recomendado)",
                        "500MB espacio en disco",
                        "Conexión a internet para instalación de dependencias"
                    ]
                },
                {
                    "step": "2. Instalación de Python",
                    "description": "Descargar e instalar Python",
                    "details": [
                        "Ir a https://python.org/downloads/",
                        "Descargar Python 3.11 (versión recomendada)",
                        "Ejecutar instalador y marcar 'Add Python to PATH'",
                        "Verificar instalación: abrir terminal y escribir 'python --version'"
                    ]
                },
                {
                    "step": "3. Descargar el Proyecto",
                    "description": "Obtener el código fuente",
                    "details": [
                        "Opción A: Descargar ZIP desde GitHub",
                        "Opción B: Clonar repositorio con 'git clone [URL]'",
                        "Extraer archivos en carpeta deseada",
                        "Abrir terminal en la carpeta del proyecto"
                    ]
                },
                {
                    "step": "4. Instalar Dependencias",
                    "description": "Instalar librerías necesarias",
                    "details": [
                        "Abrir terminal en la carpeta del proyecto",
                        "Ejecutar: pip install -r requirements.txt",
                        "O instalar manualmente:",
                        "pip install streamlit sympy matplotlib plotly numpy"
                    ]
                },
                {
                    "step": "5. Ejecutar la Aplicación",
                    "description": "Iniciar la calculadora",
                    "details": [
                        "En terminal, escribir: streamlit run app.py",
                        "Esperar a que aparezca la URL (normalmente http://localhost:8501)",
                        "Abrir la URL en tu navegador web",
                        "¡La calculadora estará lista para usar!"
                    ]
                }
            ]
        },
        {
            "title": "🚀 Guía de Uso Rápido",
            "content": [
                {
                    "feature": "Integrales Definidas",
                    "steps": [
                        "1. Ve a la sección 'Integrales Definidas'",
                        "2. Ingresa tu función (ej: x**2, sin(x), exp(x))",
                        "3. Define los límites inferior y superior",
                        "4. Haz clic en 'Calcular Integral'",
                        "5. Observa la solución paso a paso y la gráfica"
                    ]
                },
                {
                    "feature": "Sumas de Riemann",
                    "steps": [
                        "1. Selecciona 'Sumas de Riemann'",
                        "2. Ingresa la función a aproximar",
                        "3. Define el intervalo [a, b]",
                        "4. Elige número de subdivisiones",
                        "5. Selecciona método (izquierdo, derecho, medio)",
                        "6. Visualiza los rectángulos en la gráfica"
                    ]
                },
                {
                    "feature": "Área Entre Curvas",
                    "steps": [
                        "1. Accede a 'Área Entre Curvas'",
                        "2. Ingresa las dos funciones",
                        "3. Define el intervalo de integración",
                        "4. La app calculará intersecciones automáticamente",
                        "5. Observa el área sombreada en la gráfica"
                    ]
                }
            ]
        },
        {
            "title": "💡 Consejos y Trucos",
            "content": [
                {
                    "tip": "Sintaxis de Funciones",
                    "description": "Usa notación de Python para funciones matemáticas",
                    "examples": [
                        "Potencias: x**2, x**3 (no x^2)",
                        "Exponencial: exp(x) (no e^x)",
                        "Logaritmo: log(x) para ln(x)",
                        "Trigonométricas: sin(x), cos(x), tan(x)",
                        "Constantes: pi para π, e para e"
                    ]
                },
                {
                    "tip": "Límites de Integración",
                    "description": "Puedes usar valores numéricos o constantes",
                    "examples": [
                        "Números: 0, 1, 2.5, -3",
                        "Constantes: pi, pi/2, 2*pi",
                        "Expresiones: sqrt(2), log(10)"
                    ]
                },
                {
                    "tip": "Interpretación de Resultados",
                    "description": "Comprende el significado de los resultados",
                    "examples": [
                        "Resultado positivo: área neta sobre el eje x",
                        "Resultado negativo: área neta bajo el eje x",
                        "Gráfica muestra región integrada visualmente",
                        "Pasos muestran proceso matemático completo"
                    ]
                }
            ]
        }
    ]
}

# Preguntas frecuentes
faq_section = {
    "title": "❓ Preguntas Frecuentes",
    "questions": [
        {
            "q": "¿Por qué mi función no se calcula?",
            "a": "Verifica la sintaxis: usa ** para potencias, exp() para exponencial, sin(), cos(), tan() para trigonométricas. Ejemplo correcto: x**2 + sin(x)"
        },
        {
            "q": "¿Cómo ingreso funciones complejas?",
            "a": "Usa paréntesis para agrupar: (x+1)**2, sin(2*x), exp(-x/2). La calculadora soporta operaciones anidadas."
        },
        {
            "q": "¿Qué hacer si el resultado parece incorrecto?",
            "a": "Verifica los límites de integración y la sintaxis de la función. Usa la gráfica para validar visualmente el resultado."
        },
        {
            "q": "¿Puedo usar la calculadora sin internet?",
            "a": "Sí, una vez instalada localmente, funciona completamente offline. Solo necesitas internet para la instalación inicial."
        },
        {
            "q": "¿Cómo guardo mis cálculos?",
            "a": "Usa la función de captura de pantalla de tu navegador, o copia los resultados. Próximamente agregaremos exportación a PDF."
        },
        {
            "q": "¿La calculadora funciona en móviles?",
            "a": "Sí, la interfaz es responsiva y funciona en tablets y móviles, aunque la experiencia es mejor en computadora."
        }
    ]
}

# Recursos adicionales de aprendizaje
additional_learning_resources = {
    "title": "📚 Recursos Adicionales de Aprendizaje",
    "categories": [
        {
            "category": "Videos Gratuitos",
            "resources": [
                {
                    "name": "Khan Academy - Cálculo Integral",
                    "url": "https://www.khanacademy.org/math/integral-calculus",
                    "description": "Curso completo y gratuito con ejercicios interactivos"
                },
                {
                    "name": "3Blue1Brown - Essence of Calculus",
                    "url": "https://www.3blue1brown.com/topics/calculus",
                    "description": "Visualizaciones extraordinarias de conceptos de cálculo"
                },
                {
                    "name": "Professor Leonard - Cálculo Integral",
                    "url": "https://www.youtube.com/playlist?list=PLF797E961509B4EB5",
                    "description": "Clases universitarias completas y detalladas"
                }
            ]
        },
        {
            "category": "Cursos Online",
            "resources": [
                {
                    "name": "MIT OpenCourseWare - 18.01SC",
                    "url": "https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/",
                    "description": "Curso completo del MIT con videos, notas y exámenes"
                },
                {
                    "name": "Coursera - Calculus for Engineers",
                    "url": "https://www.coursera.org/specializations/calculus-for-engineers",
                    "description": "Especialización con aplicaciones prácticas"
                },
                {
                    "name": "edX - Calculus 1C: Coordinate Systems & Infinite Series",
                    "url": "https://www.edx.org/course/calculus-1c-coordinate-systems-infinite-series",
                    "description": "Curso avanzado del MIT en edX"
                }
            ]
        },
        {
            "category": "Herramientas Complementarias",
            "resources": [
                {
                    "name": "Wolfram Alpha",
                    "url": "https://www.wolframalpha.com/",
                    "description": "Motor computacional para verificar resultados"
                },
                {
                    "name": "GeoGebra",
                    "url": "https://www.geogebra.org/calculator",
                    "description": "Calculadora gráfica interactiva"
                },
                {
                    "name": "Desmos",
                    "url": "https://www.desmos.com/calculator",
                    "description": "Graficador avanzado online"
                },
                {
                    "name": "Symbolab",
                    "url": "https://www.symbolab.com/",
                    "description": "Solver de matemáticas con pasos detallados"
                }
            ]
        },
        {
            "category": "Libros de Texto",
            "resources": [
                {
                    "name": "Stewart's Calculus (8th Edition)",
                    "url": "https://www.cengage.com/c/calculus-8e-stewart",
                    "description": "Libro de texto estándar universitario"
                },
                {
                    "name": "Paul's Online Math Notes",
                    "url": "https://tutorial.math.lamar.edu/",
                    "description": "Notas completas y gratuitas de cálculo"
                },
                {
                    "name": "OpenStax Calculus",
                    "url": "https://openstax.org/details/books/calculus-volume-1",
                    "description": "Libro de texto gratuito y de alta calidad"
                }
            ]
        }
    ]
}