# Plan de Estudios y Ejemplos Adicionales para la Calculadora Matemática

# Plan de Estudios para Integrales Definidas
definite_integrals_study_plan = {
    "title": "Plan de Estudios: Integrales Definidas",
    "description": "Guía completa para dominar las integrales definidas paso a paso",
    "modules": [
        {
            "level": "Básico",
            "title": "1. Fundamentos de Integrales",
            "topics": [
                "Concepto de área bajo la curva",
                "Notación de integrales definidas",
                "Teorema Fundamental del Cálculo",
                "Propiedades básicas de integrales"
            ],
            "examples": [
                {
                    "function": "2*x",
                    "bounds": ["0", "3"],
                    "explanation": "Integral básica de función lineal - representa área de triángulo"
                },
                {
                    "function": "x**2",
                    "bounds": ["0", "2"],
                    "explanation": "Integral de función cuadrática - área bajo parábola"
                },
                {
                    "function": "3",
                    "bounds": ["1", "4"],
                    "explanation": "Integral de constante - área de rectángulo"
                }
            ]
        },
        {
            "level": "Intermedio",
            "title": "2. Funciones Trigonométricas",
            "topics": [
                "Integrales de sin(x) y cos(x)",
                "Identidades trigonométricas",
                "Períodos y simetrías",
                "Aplicaciones en ondas"
            ],
            "examples": [
                {
                    "function": "sin(x)",
                    "bounds": ["0", "3.14159"],
                    "explanation": "Integral de seno en medio período - área completa bajo curva"
                },
                {
                    "function": "cos(x)",
                    "bounds": ["0", "1.5708"],
                    "explanation": "Integral de coseno en cuarto de período"
                },
                {
                    "function": "sin(x)**2",
                    "bounds": ["0", "6.28318"],
                    "explanation": "Integral de seno cuadrado - uso de identidades"
                }
            ]
        },
        {
            "level": "Avanzado",
            "title": "3. Funciones Exponenciales y Logarítmicas",
            "topics": [
                "Integral de e^x",
                "Funciones logarítmicas",
                "Crecimiento y decaimiento",
                "Aplicaciones en ciencias"
            ],
            "examples": [
                {
                    "function": "exp(x)",
                    "bounds": ["0", "2"],
                    "explanation": "Crecimiento exponencial - base de modelos de población"
                },
                {
                    "function": "log(x)",
                    "bounds": ["1", "5"],
                    "explanation": "Integral logarítmica - aplicaciones en entropía"
                },
                {
                    "function": "x*exp(-x)",
                    "bounds": ["0", "3"],
                    "explanation": "Combinación polinomial-exponencial - modelos de decaimiento"
                }
            ]
        }
    ]
}

# Plan de Estudios para Sumas de Riemann
riemann_sums_study_plan = {
    "title": "Plan de Estudios: Sumas de Riemann",
    "description": "Aprende a aproximar integrales usando rectángulos",
    "modules": [
        {
            "level": "Básico",
            "title": "1. Conceptos Fundamentales",
            "topics": [
                "¿Qué es una suma de Riemann?",
                "Particiones de intervalos",
                "Puntos de muestra (izquierdo, derecho, medio)",
                "Interpretación geométrica"
            ],
            "examples": [
                {
                    "function": "x",
                    "bounds": [0, 2],
                    "subdivisions": 4,
                    "method": "left",
                    "explanation": "Función lineal simple - fácil visualización del método"
                },
                {
                    "function": "x**2",
                    "bounds": [0, 2],
                    "subdivisions": 4,
                    "method": "right",
                    "explanation": "Función cuadrática - observa la diferencia entre métodos"
                }
            ]
        },
        {
            "level": "Intermedio",
            "title": "2. Métodos de Aproximación",
            "topics": [
                "Comparación de métodos (izquierdo vs derecho vs medio)",
                "Error de aproximación",
                "Convergencia al aumentar subdivisiones",
                "Elección del método óptimo"
            ],
            "examples": [
                {
                    "function": "sin(x)",
                    "bounds": [0, 3.14159],
                    "subdivisions": 8,
                    "method": "midpoint",
                    "explanation": "Función trigonométrica - el punto medio es más preciso"
                },
                {
                    "function": "exp(x)",
                    "bounds": [0, 1],
                    "subdivisions": 6,
                    "method": "left",
                    "explanation": "Función exponencial creciente - observa subestimación"
                }
            ]
        },
        {
            "level": "Avanzado",
            "title": "3. Convergencia y Precisión",
            "topics": [
                "Límite cuando n → ∞",
                "Relación con integral definida",
                "Análisis de error",
                "Aplicaciones computacionales"
            ],
            "examples": [
                {
                    "function": "sqrt(x)",
                    "bounds": [1, 4],
                    "subdivisions": 12,
                    "method": "midpoint",
                    "explanation": "Función radical - alta precisión con muchas subdivisiones"
                },
                {
                    "function": "1/x",
                    "bounds": [1, 3],
                    "subdivisions": 10,
                    "method": "right",
                    "explanation": "Función racional - cuidado con singularidades"
                }
            ]
        }
    ]
}

# Plan de Estudios para Área Entre Curvas
area_between_curves_study_plan = {
    "title": "Plan de Estudios: Área Entre Curvas",
    "description": "Calcula áreas entre funciones usando integrales",
    "modules": [
        {
            "level": "Básico",
            "title": "1. Fundamentos del Área Entre Curvas",
            "topics": [
                "Concepto de área entre dos funciones",
                "Identificar función superior e inferior",
                "Fórmula: ∫[f(x) - g(x)]dx",
                "Interpretación geométrica"
            ],
            "examples": [
                {
                    "function1": "x + 2",
                    "function2": "x",
                    "bounds": [0, 3],
                    "explanation": "Dos líneas paralelas - área constante entre ellas"
                },
                {
                    "function1": "x**2",
                    "function2": "x",
                    "bounds": [0, 1],
                    "explanation": "Parábola y línea - área clásica de cálculo"
                }
            ]
        },
        {
            "level": "Intermedio",
            "title": "2. Puntos de Intersección",
            "topics": [
                "Encontrar puntos donde f(x) = g(x)",
                "Dividir integrales en intervalos",
                "Cambio de función superior/inferior",
                "Área total como suma de partes"
            ],
            "examples": [
                {
                    "function1": "sin(x)",
                    "function2": "cos(x)",
                    "bounds": [0, 1.5708],
                    "explanation": "Funciones trigonométricas que se cruzan"
                },
                {
                    "function1": "x**2",
                    "function2": "4 - x**2",
                    "bounds": [-2, 2],
                    "explanation": "Parábolas que se intersectan en múltiples puntos"
                }
            ]
        },
        {
            "level": "Avanzado",
            "title": "3. Aplicaciones Avanzadas",
            "topics": [
                "Área en coordenadas polares",
                "Volúmenes de revolución",
                "Centroides y momentos",
                "Aplicaciones en ingeniería"
            ],
            "examples": [
                {
                    "function1": "exp(x)",
                    "function2": "exp(-x)",
                    "bounds": [-1, 1],
                    "explanation": "Funciones exponenciales simétricas"
                },
                {
                    "function1": "log(x + 1)",
                    "function2": "sqrt(x)",
                    "bounds": [0, 2],
                    "explanation": "Logaritmo y radical - formas complejas"
                }
            ]
        }
    ]
}

# Plan de Estudios para Escenarios de Ingeniería
engineering_scenarios_study_plan = {
    "title": "Plan de Estudios: Aplicaciones en Ingeniería",
    "description": "Aplica integrales a problemas reales de ingeniería",
    "modules": [
        {
            "level": "Básico",
            "title": "1. Modelado de Sistemas",
            "topics": [
                "Interpretación de integrales en contexto",
                "Unidades y dimensiones",
                "Modelos lineales y cuadráticos",
                "Análisis de tendencias"
            ],
            "examples": [
                {
                    "scenario": "Uso de CPU",
                    "function": "2*t + 5",
                    "bounds": ["0", "4"],
                    "interpretation": "CPU usage increases linearly - total processing time"
                },
                {
                    "scenario": "Consumo de memoria",
                    "function": "t**2 + 3",
                    "bounds": ["1", "3"],
                    "interpretation": "Memory usage grows quadratically with load"
                }
            ]
        },
        {
            "level": "Intermedio",
            "title": "2. Análisis de Rendimiento",
            "topics": [
                "Métricas de rendimiento acumulado",
                "Optimización de recursos",
                "Análisis de carga de trabajo",
                "Predicción de comportamiento"
            ],
            "examples": [
                {
                    "scenario": "Throughput de red",
                    "function": "100*log(t + 1)",
                    "bounds": ["0", "10"],
                    "interpretation": "Network throughput follows logarithmic saturation"
                },
                {
                    "scenario": "Latencia del sistema",
                    "function": "50/t",
                    "bounds": ["1", "5"],
                    "interpretation": "Latency decreases as system optimizes"
                }
            ]
        },
        {
            "level": "Avanzado",
            "title": "3. Optimización y Escalabilidad",
            "topics": [
                "Modelos de crecimiento exponencial",
                "Análisis de capacidad",
                "Planificación de recursos",
                "Evaluación de algoritmos"
            ],
            "examples": [
                {
                    "scenario": "Escalabilidad de microservicios",
                    "function": "t*exp(-t/10)",
                    "bounds": ["0", "20"],
                    "interpretation": "Service load peaks then stabilizes with auto-scaling"
                },
                {
                    "scenario": "Complejidad algorítmica",
                    "function": "n*log(n)",
                    "bounds": ["1", "100"],
                    "interpretation": "Algorithm complexity analysis for large datasets"
                }
            ]
        }
    ]
}

# Ejemplos adicionales de integrales por dificultad
additional_integral_examples = {
    "principiante": [
        {
            "function": "5",
            "bounds": ["0", "3"],
            "result": 15,
            "explanation": "Integral de constante = base × altura"
        },
        {
            "function": "x",
            "bounds": ["0", "4"],
            "result": 8,
            "explanation": "Área de triángulo = (1/2) × base × altura"
        },
        {
            "function": "2*x + 1",
            "bounds": ["0", "2"],
            "result": 6,
            "explanation": "Integral de función lineal"
        }
    ],
    "intermedio": [
        {
            "function": "x**2 + x",
            "bounds": ["0", "2"],
            "result": 4.67,
            "explanation": "Polinomio de segundo grado"
        },
        {
            "function": "sin(x)",
            "bounds": ["0", "3.14159"],
            "result": 2,
            "explanation": "Integral de seno en medio período"
        },
        {
            "function": "exp(x)",
            "bounds": ["0", "1"],
            "result": 1.718,
            "explanation": "Función exponencial natural"
        }
    ],
    "avanzado": [
        {
            "function": "x*sin(x)",
            "bounds": ["0", "3.14159"],
            "result": 3.14159,
            "explanation": "Producto de polinomio y trigonométrica"
        },
        {
            "function": "log(x)",
            "bounds": ["1", "5"],
            "result": 3.047,
            "explanation": "Función logarítmica natural"
        },
        {
            "function": "sqrt(x**2 + 1)",
            "bounds": ["0", "2"],
            "result": 2.957,
            "explanation": "Función radical compuesta"
        }
    ]
}

# Ejercicios prácticos paso a paso
practice_exercises = {
    "integrales_definidas": [
        {
            "problem": "Calcula el área bajo f(x) = x² desde x = 0 hasta x = 3",
            "steps": [
                "1. Identifica la función: f(x) = x²",
                "2. Encuentra la antiderivada: F(x) = x³/3",
                "3. Aplica el teorema fundamental: F(3) - F(0)",
                "4. Calcula: (27/3) - (0/3) = 9"
            ],
            "answer": 9
        },
        {
            "problem": "Evalúa ∫₀^π sin(x) dx",
            "steps": [
                "1. La antiderivada de sin(x) es -cos(x)",
                "2. Evalúa en los límites: [-cos(π)] - [-cos(0)]",
                "3. Simplifica: -(-1) - (-1) = 1 + 1 = 2"
            ],
            "answer": 2
        }
    ],
    "sumas_riemann": [
        {
            "problem": "Aproxima ∫₀² x² dx usando 4 rectángulos (método izquierdo)",
            "steps": [
                "1. Δx = (2-0)/4 = 0.5",
                "2. Puntos: x₀=0, x₁=0.5, x₂=1, x₃=1.5",
                "3. Alturas: f(0)=0, f(0.5)=0.25, f(1)=1, f(1.5)=2.25",
                "4. Suma: 0.5 × (0 + 0.25 + 1 + 2.25) = 1.75"
            ],
            "answer": 1.75
        }
    ]
}