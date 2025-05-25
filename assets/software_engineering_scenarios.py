# Escenarios Específicos de Ingeniería de Software con Aplicaciones del Cálculo

SOFTWARE_ENGINEERING_SCENARIOS = {
    "title": "🏗️ Cálculo en Ingeniería de Software",
    "description": "Aplicaciones reales del cálculo integral en desarrollo de software y ciencias de la computación",
    
    "categories": [
        {
            "name": "🚀 Optimización de Rendimiento",
            "description": "Uso del cálculo para optimizar el rendimiento de sistemas",
            "scenarios": [
                {
                    "title": "Análisis de Complejidad Temporal",
                    "context": "Calcular el tiempo total de ejecución de un algoritmo",
                    "function": "2*t**2 + 5*t",
                    "bounds": [0, 10],
                    "unit": "milisegundos",
                    "variable": "t",
                    "explanation": "Esta integral calcula el tiempo total acumulado cuando la complejidad temporal es cuadrática.",
                    "real_application": "Análisis de algoritmos de ordenamiento como Bubble Sort o Selection Sort",
                    "why_calculus": "El cálculo integral nos permite encontrar el tiempo total de ejecución cuando tenemos una función de complejidad variable."
                },
                {
                    "title": "Consumo de Memoria Dinámico",
                    "context": "Memoria utilizada por una aplicación en función del número de usuarios",
                    "function": "50*log(t+1) + 100",
                    "bounds": [1, 100],
                    "unit": "MB",
                    "variable": "t",
                    "explanation": "Calcula el consumo total de memoria cuando crece logarítmicamente con los usuarios.",
                    "real_application": "Sistemas de cache inteligente o aplicaciones web escalables",
                    "why_calculus": "Las integrales nos ayudan a predecir el uso total de recursos en sistemas dinámicos."
                }
            ]
        },
        
        {
            "name": "📊 Análisis de Datos y Machine Learning",
            "description": "Aplicaciones del cálculo en ciencia de datos",
            "scenarios": [
                {
                    "title": "Función de Pérdida en Redes Neuronales",
                    "context": "Calcular la pérdida total durante el entrenamiento",
                    "function": "exp(-0.1*t)",
                    "bounds": [0, 50],
                    "unit": "unidades de error",
                    "variable": "t",
                    "explanation": "La integral de la función de pérdida nos da el error total acumulado durante el entrenamiento.",
                    "real_application": "Optimización de hiperparámetros en deep learning",
                    "why_calculus": "El cálculo es fundamental para entender cómo convergen los algoritmos de optimización."
                },
                {
                    "title": "Distribución de Probabilidad",
                    "context": "Calcular probabilidades en modelos estadísticos",
                    "function": "exp(-t**2/2)/sqrt(2*pi)",
                    "bounds": [-2, 2],
                    "unit": "probabilidad",
                    "variable": "t",
                    "explanation": "Integral de la distribución normal estándar para calcular probabilidades.",
                    "real_application": "Modelos bayesianos, análisis de incertidumbre en IA",
                    "why_calculus": "Las distribuciones de probabilidad se definen mediante integrales."
                }
            ]
        },
        
        {
            "name": "🌐 Sistemas Distribuidos y Redes",
            "description": "Cálculo aplicado a sistemas en red",
            "scenarios": [
                {
                    "title": "Análisis de Tráfico de Red",
                    "context": "Tráfico total de datos en un servidor durante un pico",
                    "function": "1000*sin(pi*t/12) + 1500",
                    "bounds": [0, 24],
                    "unit": "MB/hora",
                    "variable": "t",
                    "explanation": "Calcular el volumen total de datos transferido en un día con patrones cíclicos.",
                    "real_application": "Planificación de capacidad en CDNs (Content Delivery Networks)",
                    "why_calculus": "Los patrones de tráfico varían continuamente y requieren análisis integral."
                },
                {
                    "title": "Latencia Acumulada en Microservicios",
                    "context": "Latencia total en una cadena de microservicios",
                    "function": "20 + 5*log(t)",
                    "bounds": [1, 10],
                    "unit": "ms",
                    "variable": "t",
                    "explanation": "Suma de latencias cuando cada servicio adicional incrementa el tiempo logarítmicamente.",
                    "real_application": "Arquitecturas de microservicios en empresas como Netflix o Amazon",
                    "why_calculus": "Permite optimizar la secuencia de llamadas entre servicios."
                }
            ]
        },
        
        {
            "name": "🔐 Ciberseguridad y Criptografía",
            "description": "Matemáticas aplicadas a la seguridad informática",
            "scenarios": [
                {
                    "title": "Entropía de Contraseñas",
                    "context": "Calcular la entropía total de un sistema de contraseñas",
                    "function": "log(t)*t",
                    "bounds": [1, 64],
                    "unit": "bits",
                    "variable": "t",
                    "explanation": "La entropía acumulada determina la fortaleza criptográfica del sistema.",
                    "real_application": "Generadores de contraseñas seguras, análisis de fortaleza",
                    "why_calculus": "La teoría de la información usa integrales para medir la incertidumbre."
                },
                {
                    "title": "Análisis de Ataques de Fuerza Bruta",
                    "context": "Tiempo esperado para romper una encriptación",
                    "function": "2**t",
                    "bounds": [0, 8],
                    "unit": "intentos",
                    "variable": "t",
                    "explanation": "Crecimiento exponencial del número de intentos necesarios.",
                    "real_application": "Evaluación de la seguridad de algoritmos criptográficos",
                    "why_calculus": "Modela el crecimiento exponencial de la complejidad computacional."
                }
            ]
        },
        
        {
            "name": "🎮 Gráficos por Computadora y Videojuegos",
            "description": "Aplicaciones del cálculo en gráficos y simulaciones",
            "scenarios": [
                {
                    "title": "Cálculo de Iluminación Global",
                    "context": "Integral de iluminación en ray tracing",
                    "function": "cos(t)*exp(-t/2)",
                    "bounds": [0, pi],
                    "unit": "lúmenes",
                    "variable": "t",
                    "explanation": "Ecuación de renderizado para calcular la luz total que llega a un punto.",
                    "real_application": "Motores de renderizado como Unreal Engine, Blender Cycles",
                    "why_calculus": "La ecuación de renderizado es fundamentalmente una integral."
                },
                {
                    "title": "Física de Partículas en Simulación",
                    "context": "Trayectoria de partículas bajo gravedad",
                    "function": "9.8*t - 0.5*9.8*t**2",
                    "bounds": [0, 5],
                    "unit": "metros",
                    "variable": "t",
                    "explanation": "Distancia total recorrida por una partícula en caída libre.",
                    "real_application": "Simuladores físicos en videojuegos, efectos de partículas",
                    "why_calculus": "Las leyes de la física se expresan mediante ecuaciones diferenciales."
                }
            ]
        }
    ],
    
    "educational_resources": {
        "theory": [
            {
                "title": "Calculus in Computer Science - MIT",
                "url": "https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/",
                "description": "Fundamentos matemáticos para ciencias de la computación",
                "type": "Curso universitario"
            },
            {
                "title": "Mathematics for Computer Science",
                "url": "https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/",
                "description": "Matemáticas discretas y continuas aplicadas a CS",
                "type": "Curso especializado"
            },
            {
                "title": "Calculus for Machine Learning",
                "url": "https://www.coursera.org/learn/machine-learning-calculus",
                "description": "Cálculo específicamente para algoritmos de ML",
                "type": "Curso online"
            }
        ],
        
        "videos": [
            {
                "title": "3Blue1Brown - Essence of Calculus",
                "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr",
                "description": "Visualización intuitiva del cálculo y sus aplicaciones",
                "type": "Serie de videos"
            },
            {
                "title": "Khan Academy - Calculus Applications",
                "url": "https://www.khanacademy.org/math/ap-calculus-ab",
                "description": "Aplicaciones prácticas del cálculo paso a paso",
                "type": "Videos educativos"
            },
            {
                "title": "MIT 6.034 Artificial Intelligence",
                "url": "https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/",
                "description": "Fundamentos matemáticos de IA incluyendo cálculo",
                "type": "Conferencias universitarias"
            }
        ],
        
        "practical": [
            {
                "title": "Numerical Methods in Python",
                "url": "https://scipy-lectures.org/",
                "description": "Implementación práctica de métodos numéricos",
                "type": "Tutorial interactivo"
            },
            {
                "title": "Computer Graphics: Principles and Practice",
                "url": "https://www.amazon.com/Computer-Graphics-Principles-Practice-3rd/dp/0321399528",
                "description": "Matemáticas avanzadas para gráficos por computadora",
                "type": "Libro de referencia"
            },
            {
                "title": "Pattern Recognition and Machine Learning",
                "url": "https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf",
                "description": "Fundamentos matemáticos del aprendizaje automático",
                "type": "Libro académico"
            }
        ]
    },
    
    "tools_and_frameworks": [
        {
            "name": "NumPy",
            "description": "Computación numérica y álgebra lineal",
            "use_case": "Implementar algoritmos de integración numérica"
        },
        {
            "name": "SciPy",
            "description": "Métodos científicos y de optimización",
            "use_case": "Resolver integrales complejas en aplicaciones reales"
        },
        {
            "name": "TensorFlow/PyTorch",
            "description": "Frameworks de deep learning",
            "use_case": "Optimización automática usando cálculo (backpropagation)"
        },
        {
            "name": "OpenGL/DirectX",
            "description": "APIs de gráficos 3D",
            "use_case": "Implementar algoritmos de renderizado basados en integrales"
        }
    ],
    
    "career_applications": {
        "roles": [
            {
                "title": "🤖 Ingeniero de Machine Learning",
                "calculus_use": "Optimización de funciones de pérdida, análisis de convergencia",
                "examples": ["Gradient descent", "Backpropagation", "Regularización"]
            },
            {
                "title": "🎮 Desarrollador de Videojuegos",
                "calculus_use": "Física de partículas, iluminación, animaciones fluidas",
                "examples": ["Simulación física", "Ray tracing", "Curvas de Bézier"]
            },
            {
                "title": "📊 Científico de Datos",
                "calculus_use": "Análisis estadístico, modelos probabilísticos",
                "examples": ["Distribuciones", "Teorema central del límite", "Análisis bayesiano"]
            },
            {
                "title": "🔒 Especialista en Ciberseguridad",
                "calculus_use": "Criptografía, análisis de entropía, modelado de amenazas",
                "examples": ["Funciones hash", "Protocolos seguros", "Análisis de riesgo"]
            },
            {
                "title": "☁️ Arquitecto de Sistemas",
                "calculus_use": "Optimización de recursos, análisis de capacidad",
                "examples": ["Load balancing", "Auto-scaling", "Predicción de carga"]
            }
        ]
    }
}

# Ejemplos específicos más detallados
DETAILED_SOFTWARE_EXAMPLES = [
    {
        "title": "Optimización de Cache en Base de Datos",
        "context": "Calcular el hit rate óptimo de cache para minimizar latencia",
        "function": "100/(1 + exp(-0.5*(t-10)))",
        "bounds": [0, 20],
        "variable": "t",
        "unit": "% hit rate",
        "difficulty": "Intermedio",
        "explanation": """
        Esta función sigmoide modela cómo mejora el hit rate del cache conforme aumenta su tamaño.
        La integral nos da el beneficio acumulado total del cache.
        """,
        "implementation": """
        # Pseudo-código para implementación real
        def cache_efficiency(cache_size):
            return 100 / (1 + math.exp(-0.5 * (cache_size - 10)))
        
        # Usar integración para encontrar tamaño óptimo
        total_benefit = integrate(cache_efficiency, 0, 20)
        """,
        "companies_using": ["Google", "Amazon", "Facebook", "Netflix"]
    },
    
    {
        "title": "Análisis de Throughput en API Gateway",
        "context": "Calcular el throughput total procesado durante picos de tráfico",
        "function": "1000*sin(pi*t/6)**2 + 500",
        "bounds": [0, 12],
        "variable": "t",
        "unit": "requests/second",
        "difficulty": "Avanzado",
        "explanation": """
        Función que modela el tráfico con patrones cíclicos durante el día.
        La integral calcula el número total de requests procesados.
        """,
        "implementation": """
        import numpy as np
        from scipy.integrate import quad
        
        def traffic_pattern(t):
            return 1000 * np.sin(np.pi * t / 6)**2 + 500
        
        total_requests, _ = quad(traffic_pattern, 0, 12)
        print(f"Total requests in 12 hours: {total_requests}")
        """,
        "companies_using": ["Stripe", "PayPal", "Uber", "Airbnb"]
    },
    
    {
        "title": "Optimización de Batch Processing",
        "context": "Determinar el tamaño óptimo de lotes para procesamiento",
        "function": "t*log(t) + 100/t",
        "bounds": [1, 100],
        "variable": "t",
        "unit": "costo computacional",
        "difficulty": "Avanzado",
        "explanation": """
        Función que balancea el costo de setup (logarítmico) vs overhead (1/t).
        Encontrar el mínimo de la integral nos da el batch size óptimo.
        """,
        "implementation": """
        def batch_cost(batch_size):
            return batch_size * math.log(batch_size) + 100 / batch_size
        
        # Encontrar mínimo usando cálculo
        from scipy.optimize import minimize_scalar
        result = minimize_scalar(batch_cost, bounds=(1, 100))
        optimal_size = result.x
        """,
        "companies_using": ["Apache Spark", "Hadoop", "AWS", "Azure"]
    }
]