# Import sympy for constants
import sympy as sp

# Riemann sum examples from the course materials
riemann_sum_examples = {
    "Ejemplo 1: x² + 3x + 2 en [2, 4]": {
        "function": "x^2 + 3*x + 2",
        "lower_bound": 2,
        "upper_bound": 4,
        "subdivisions": 6,
        "method": "left"
    },
    "Ejemplo 2: x² + 2x en [0, 3]": {
        "function": "x^2 + 2*x",
        "lower_bound": 0,
        "upper_bound": 3,
        "subdivisions": 6,
        "method": "left"
    },
    "Ejemplo 3: e^x + 1 en [0, 4]": {
        "function": "exp(x) + 1",
        "lower_bound": 0,
        "upper_bound": 4,
        "subdivisions": 4,
        "method": "midpoint"
    },
    "Ejemplo 4: cos(x) en [0, 3π/2]": {
        "function": "cos(x)",
        "lower_bound": 0,
        "upper_bound": float(3*sp.pi/2),
        "subdivisions": 6,
        "method": "right"
    },
    "Ejemplo 5: 2x² + 3x - 2 en [0, 3]": {
        "function": "2*x^2 + 3*x - 2",
        "lower_bound": 0,
        "upper_bound": 3,
        "subdivisions": 6,
        "method": "left"
    },
    "Ejemplo 6: 3 + (1/2)x en [-1, 7]": {
        "function": "3 + (1/2)*x",
        "lower_bound": -1,
        "upper_bound": 7,
        "subdivisions": 6,
        "method": "left"
    },
    "Ejemplo 7: sin(x) + cos(x) en [π/2, 3π/2]": {
        "function": "sin(x) + cos(x)",
        "lower_bound": float(sp.pi/2),
        "upper_bound": float(3*sp.pi/2),
        "subdivisions": 6,
        "method": "right"
    },
    "Ejemplo 8: 2x³ - 3x² + 2 en [0, 4]": {
        "function": "2*x^3 - 3*x^2 + 2",
        "lower_bound": 0,
        "upper_bound": 4,
        "subdivisions": 6,
        "method": "left"
    },
    "Ejemplo 9: e^x + 2 en [2, 4]": {
        "function": "exp(x) + 2",
        "lower_bound": 2,
        "upper_bound": 4,
        "subdivisions": 4,
        "method": "midpoint"
    },
    "Ejemplo 10: (x-2)³ + (x-2)² + 1 en [0, 6]": {
        "function": "(x-2)^3 + (x-2)^2 + 1",
        "lower_bound": 0,
        "upper_bound": 6,
        "subdivisions": 6,
        "method": "left"
    }
}

# Definite integral examples
definite_integral_examples = {
    "Área bajo sin(x) y cos(x)": {
        "function": "sin(x)",
        "lower_bound": 0,
        "upper_bound": "pi",
        "variable": "x"
    },
    "Área bajo 2x² + 3x - 2": {
        "function": "2*x^2 + 3*x - 2",
        "lower_bound": 0,
        "upper_bound": 3,
        "variable": "x"
    },
    "Área bajo 5 - 2t²": {
        "function": "5 - 2*t^2",
        "lower_bound": 0,
        "upper_bound": 5,
        "variable": "t"
    },
    "Uso de recursos del servidor: 50e^(-0.2t)": {
        "function": "50*exp(-0.2*t)",
        "lower_bound": 0,
        "upper_bound": 30,
        "variable": "t"
    },
    "Complejidad temporal del algoritmo: 3n² + 2n + 1": {
        "function": "3*n^2 + 2*n + 1",
        "lower_bound": 1,
        "upper_bound": 10,
        "variable": "n"
    },
    "Crecimiento exponencial: 2^x": {
        "function": "2^x",
        "lower_bound": 0,
        "upper_bound": 5,
        "variable": "x"
    },
    "Función logarítmica: ln(x)": {
        "function": "ln(x)",
        "lower_bound": 1,
        "upper_bound": 10,
        "variable": "x"
    },
    "Función racional: 1/x": {
        "function": "1/x",
        "lower_bound": 1,
        "upper_bound": 5,
        "variable": "x"
    }
}

# Area between curves examples
area_between_curves_examples = {
    "Intersección de Sin y Cos": {
        "function1": "sin(x)",
        "function2": "cos(x)",
        "lower_bound": 0,
        "upper_bound": "pi/4",
        "description": "Las curvas seno y coseno se intersectan infinitas veces, creando regiones de áreas iguales."
    },
    "Optimización de base de datos (Ejemplo 2)": {
        "function1": "3 + y^2",
        "function2": "y + 1",
        "lower_bound": 0,
        "upper_bound": 2,
        "description": "La optimización en consultas de base de datos se mide por la convergencia de velocidad (3 + y²) y precisión (y + 1)."
    },
    "Consumo de recursos del servidor (Ejemplo 3)": {
        "function1": "(t + 4)^2 + 2*(t + 4) + 1",
        "function2": "-t + 5",
        "lower_bound": 0,
        "upper_bound": 5,
        "description": "Uso de memoria M(t) = (t + 4)² + 2(t + 4) + 1 y uso de CPU C(t) = -t + 5 durante la carga de datos."
    },
    "Optimización de base de datos (Ejemplo 6)": {
        "function1": "sqrt(3 - x)",
        "function2": "x - 1",
        "lower_bound": 0,
        "upper_bound": 1,
        "description": "La optimización en consultas de base de datos se mide por la convergencia de velocidad (√(3-x)) y precisión (x-1)."
    },
    "Uso de memoria y CPU del servidor (Ejemplo 9)": {
        "function1": "t^2 + 2*t + 1",
        "function2": "2*t + 5",
        "lower_bound": 0,
        "upper_bound": 3,
        "description": "Uso de memoria M(t) = t² + 2t + 1 y uso de CPU C(t) = 2t + 5 durante la carga de datos."
    },
    "Optimización de base de datos (Ejemplo 10)": {
        "function1": "(x - 1)^2",
        "function2": "2*x - 4",
        "lower_bound": 1,
        "upper_bound": 2,
        "description": "La optimización en consultas de base de datos se mide por la convergencia de velocidad ((x-1)²) y precisión (2x-4)."
    },
    "Parábolas intersecantes": {
        "function1": "x^2",
        "function2": "4 - x^2",
        "lower_bound": -2,
        "upper_bound": 2,
        "description": "Área entre dos parábolas que se intersectan en múltiples puntos."
    },
    "Funciones lineales": {
        "function1": "2*x + 1",
        "function2": "x + 3",
        "lower_bound": 0,
        "upper_bound": 4,
        "description": "Área entre dos funciones lineales con diferentes pendientes."
    }
}

# Engineering applications examples
engineering_applications_examples = {
    "Consumo de Recursos del Servidor": {
        "Ejemplo 1: Memoria y CPU del Servidor": {
            "description": "Un servidor web tiene uso de memoria M(t) = t² + 2t + 1 y uso de CPU C(t) = 2t + 5 durante la carga de datos, donde t es el tiempo en minutos. Calcula los recursos totales utilizados en los primeros 3 minutos.",
            "function1": "t^2 + 2*t + 1",
            "function2": "2*t + 5",
            "lower_bound": 0,
            "upper_bound": 3,
            "calculation_type": "area_between_curves"
        },
        "Ejemplo 2: Decaimiento de Recursos": {
            "description": "El consumo de recursos de un servidor se modela por R(t) = 5 - 2t² MB por minuto durante un proceso de carga de datos, donde t es el tiempo en minutos. Calcula los recursos totales utilizados en los primeros 5 minutos.",
            "function1": "5 - 2*t^2",
            "lower_bound": 0,
            "upper_bound": 5,
            "calculation_type": "definite_integral"
        }
    },
    "Análisis de Carga de Usuarios": {
        "Ejemplo 1: Decaimiento Exponencial": {
            "description": "La carga de usuarios en un sistema durante un evento se modela por C(t) = 50e^(-0.2t), donde t es el tiempo en minutos y C(t) es el número de usuarios activos. Calcula las interacciones totales de usuarios durante los primeros 30 minutos.",
            "function1": "50*exp(-0.2*t)",
            "lower_bound": 0,
            "upper_bound": 30,
            "calculation_type": "definite_integral"
        },
        "Ejemplo 2: Carga de Usuarios de 8 Horas": {
            "description": "La carga de usuarios en un sistema se modela por C(t) = 20e^(-0.5t), donde t es el tiempo en minutos. Calcula los usuarios acumulados totales de 1 a 8 horas (60 a 480 minutos).",
            "function1": "20*exp(-0.5*t)",
            "lower_bound": 60,
            "upper_bound": 480,
            "calculation_type": "definite_integral"
        }
    },
    "Optimización de Base de Datos": {
        "Ejemplo 1: Métricas de Optimización": {
            "description": "La optimización de base de datos se mide por la convergencia de velocidad (3 + y²) y precisión (y + 1) en revisiones de consultas. Encuentra el área entre estas funciones desde y = 0 hasta y = 2, representando el potencial máximo de optimización.",
            "function1": "3 + y^2",
            "function2": "y + 1",
            "lower_bound": 0,
            "upper_bound": 2,
            "calculation_type": "area_between_curves"
        },
        "Ejemplo 2: Optimización Parabólica": {
            "description": "La optimización de base de datos se mide por velocidad ((x-1)²) y precisión (2x-4). Encuentra el área entre estas funciones desde x = 1 hasta x = 2, representando el potencial máximo de optimización.",
            "function1": "(x-1)^2",
            "function2": "2*x-4",
            "lower_bound": 1,
            "upper_bound": 2,
            "calculation_type": "area_between_curves"
        }
    },
    "Complejidad de Algoritmos": {
        "Ejemplo 1: Complejidad Cuadrática": {
            "description": "Un algoritmo tiene una complejidad temporal T(n) = 3n² + 2n + 1 milisegundos, donde n es el tamaño de entrada. Calcula el tiempo total de ejecución para procesar datos desde n = 1 hasta n = 10.",
            "function1": "3*n^2 + 2*n + 1",
            "lower_bound": 1,
            "upper_bound": 10,
            "calculation_type": "definite_integral"
        },
        "Ejemplo 2: Comparación de Algoritmos": {
            "description": "Compara dos algoritmos: A1(n) = n^2 y A2(n) = n*log(n). Encuentra el área entre las curvas para determinar cuándo un algoritmo supera al otro.",
            "function1": "n^2",
            "function2": "n*log(n)",
            "lower_bound": 1,
            "upper_bound": 50,
            "calculation_type": "area_between_curves"
        }
    }
}

# Additional mathematical function examples for learning
mathematical_function_examples = {
    "Funciones Polinómiales": [
        "x^2",
        "x^3 - 2*x^2 + x",
        "2*x^4 - 3*x^3 + x^2 - 5",
        "x^5 + x^3 - 2*x"
    ],
    "Funciones Trigonométricas": [
        "sin(x)",
        "cos(x)",
        "tan(x)",
        "sin(2*x) + cos(x)",
        "sin(x)*cos(x)"
    ],
    "Funciones Exponenciales": [
        "exp(x)",
        "2^x",
        "e^(-x)",
        "exp(-x^2)",
        "3*exp(2*x)"
    ],
    "Funciones Logarítmicas": [
        "ln(x)",
        "log(x)",
        "ln(x^2 + 1)",
        "x*ln(x)",
        "ln(abs(x))"
    ],
    "Funciones Racionales": [
        "1/x",
        "1/(x^2 + 1)",
        "(x + 1)/(x - 1)",
        "x/(x^2 + 4)",
        "(2*x + 3)/(x^2 + x + 1)"
    ],
    "Funciones Radicales": [
        "sqrt(x)",
        "sqrt(x^2 + 1)",
        "x*sqrt(x)",
        "sqrt(4 - x^2)",
        "1/sqrt(x)"
    ]
}

# Common integration bounds for different types of problems
common_bounds = {
    "trigonometric": {
        "full_period": (0, "2*pi"),
        "half_period": (0, "pi"),
        "quarter_period": (0, "pi/2"),
        "symmetric": ("-pi/2", "pi/2")
    },
    "exponential": {
        "positive": (0, 5),
        "decay": (0, 10),
        "growth": (-2, 2)
    },
    "polynomial": {
        "unit_interval": (0, 1),
        "symmetric": (-1, 1),
        "positive": (0, 5),
        "standard": (-2, 2)
    },
    "logarithmic": {
        "positive": (1, 10),
        "natural": (1, "e"),
        "extended": (1, 100)
    }
}
