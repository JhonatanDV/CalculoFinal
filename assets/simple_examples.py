# Ejemplos simples y validados para evitar errores de expresiones

# Ejemplos de Integrales Definidas (sin errores de sintaxis)
definite_integral_examples = {
    "Función cuadrática: x^2": {
        "function": "x**2",
        "lower_bound": "0",
        "upper_bound": "2",
        "variable": "x"
    },
    "Función lineal: 2*x + 1": {
        "function": "2*x + 1",
        "lower_bound": "0",
        "upper_bound": "3",
        "variable": "x"
    },
    "Función cúbica: x^3": {
        "function": "x**3",
        "lower_bound": "1",
        "upper_bound": "2",
        "variable": "x"
    },
    "Polinomio: x^2 + 3*x + 2": {
        "function": "x**2 + 3*x + 2",
        "lower_bound": "0",
        "upper_bound": "2",
        "variable": "x"
    },
    "Función seno: sin(x)": {
        "function": "sin(x)",
        "lower_bound": "0",
        "upper_bound": "3.14159",
        "variable": "x"
    },
    "Función coseno: cos(x)": {
        "function": "cos(x)",
        "lower_bound": "0",
        "upper_bound": "1.5708",
        "variable": "x"
    },
    "Función exponencial: exp(x)": {
        "function": "exp(x)",
        "lower_bound": "0",
        "upper_bound": "1",
        "variable": "x"
    },
    "Función logarítmica: log(x)": {
        "function": "log(x)",
        "lower_bound": "1",
        "upper_bound": "3",
        "variable": "x"
    },
    "Función racional: 1/x": {
        "function": "1/x",
        "lower_bound": "1",
        "upper_bound": "5",
        "variable": "x"
    },
    "Función radical: sqrt(x)": {
        "function": "sqrt(x)",
        "lower_bound": "1",
        "upper_bound": "4",
        "variable": "x"
    }
}

# Ejemplos de Sumas de Riemann
riemann_sum_examples = {
    "Ejemplo 1: x^2 + 3*x + 2 en [0, 2]": {
        "function": "x**2 + 3*x + 2",
        "lower_bound": 0,
        "upper_bound": 2,
        "subdivisions": 6,
        "method": "left"
    },
    "Ejemplo 2: x^2 + 2*x en [0, 3]": {
        "function": "x**2 + 2*x",
        "lower_bound": 0,
        "upper_bound": 3,
        "subdivisions": 6,
        "method": "left"
    },
    "Ejemplo 3: exp(x) + 1 en [0, 2]": {
        "function": "exp(x) + 1",
        "lower_bound": 0,
        "upper_bound": 2,
        "subdivisions": 4,
        "method": "midpoint"
    },
    "Ejemplo 4: sin(x) en [0, 3.14]": {
        "function": "sin(x)",
        "lower_bound": 0,
        "upper_bound": 3.14,
        "subdivisions": 6,
        "method": "right"
    },
    "Ejemplo 5: 2*x^2 + 3*x - 2 en [0, 3]": {
        "function": "2*x**2 + 3*x - 2",
        "lower_bound": 0,
        "upper_bound": 3,
        "subdivisions": 6,
        "method": "left"
    }
}

# Ejemplos de Área entre Curvas
area_between_curves_examples = {
    "Parábolas: x^2 y 2*x": {
        "function1": "x**2",
        "function2": "2*x",
        "lower_bound": 0,
        "upper_bound": 2,
        "description": "Área entre una parábola y una línea recta."
    },
    "Funciones lineales: 2*x + 1 y x + 3": {
        "function1": "2*x + 1",
        "function2": "x + 3",
        "lower_bound": 0,
        "upper_bound": 3,
        "description": "Área entre dos funciones lineales."
    },
    "Cuadrática y lineal: x^2 y x": {
        "function1": "x**2",
        "function2": "x",
        "lower_bound": 0,
        "upper_bound": 1,
        "description": "Área clásica entre parábola y línea."
    },
    "Trigonométricas: sin(x) y cos(x)": {
        "function1": "sin(x)",
        "function2": "cos(x)",
        "lower_bound": 0,
        "upper_bound": 0.785,
        "description": "Área entre seno y coseno."
    }
}

# Escenarios de Ingeniería Simplificados
engineering_scenarios = {
    "Uso de CPU del Servidor": {
        "description": "El uso de CPU del servidor sigue el patrón f(t) = t^2 + 2*t + 1 % por minuto. Calcula el uso total desde t = 0 hasta t = 3 minutos.",
        "function": "t**2 + 2*t + 1",
        "lower_bound": "0",
        "upper_bound": "3",
        "variable": "t",
        "calculation_type": "definite_integral"
    },
    "Consumo de Memoria": {
        "description": "El consumo de memoria sigue f(t) = 3*t + 5 MB por minuto. Calcula el consumo total desde t = 1 hasta t = 5 minutos.",
        "function": "3*t + 5",
        "lower_bound": "1",
        "upper_bound": "5",
        "variable": "t",
        "calculation_type": "definite_integral"
    },
    "Tráfico de Red": {
        "description": "El tráfico de red sigue f(t) = 2*t^2 + t MB/s. Calcula el tráfico total desde t = 0 hasta t = 4 segundos.",
        "function": "2*t**2 + t",
        "lower_bound": "0",
        "upper_bound": "4",
        "variable": "t",
        "calculation_type": "definite_integral"
    },
    "Procesamiento de Datos": {
        "description": "El procesamiento de datos sigue f(t) = t^2 + 4 operaciones por segundo. Calcula el total desde t = 1 hasta t = 3 segundos.",
        "function": "t**2 + 4",
        "lower_bound": "1",
        "upper_bound": "3",
        "variable": "t",
        "calculation_type": "definite_integral"
    },
    "Uso de Base de Datos": {
        "description": "Las consultas a la base de datos siguen f(t) = 5*t + 2 consultas por minuto. Calcula el total desde t = 2 hasta t = 6 minutos.",
        "function": "5*t + 2",
        "lower_bound": "2",
        "upper_bound": "6",
        "variable": "t",
        "calculation_type": "definite_integral"
    }
}