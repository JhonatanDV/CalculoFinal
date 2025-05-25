"""
Generador de escenarios aleatorios para la calculadora matemática.
"""

import random
import sympy as sp
from typing import Dict, List, Tuple

def generate_random_function(complexity: str = "medium") -> Dict[str, str]:
    """
    Genera una función matemática aleatoria.
    
    Args:
        complexity: Nivel de complejidad ("simple", "medium", "complex")
        
    Returns:
        Dict con función, descripción y tipo
    """
    
    simple_functions = [
        "x**2",
        "x**3", 
        "2*x + 1",
        "x**2 + 1",
        "3*x**2 + 2*x + 1",
        "x**2 - 4*x + 3"
    ]
    
    medium_functions = [
        "sin(x)",
        "cos(x)", 
        "x*sin(x)",
        "sin(x)**2",
        "x**2*cos(x)",
        "x**2 + sin(x)",
        "cos(x) + 1",
        "2*sin(x)"
    ]
    
    complex_functions = [
        "x*sin(x)",
        "x**2*cos(x)",
        "sin(x)*cos(x)",
        "x**3 + cos(x)",
        "x**2*sin(x)",
        "sin(x) + cos(x)",
        "x*cos(x)",
        "x**3*sin(x)"
    ]
    
    if complexity == "simple":
        func = random.choice(simple_functions)
        description = "Función polinomial básica"
    elif complexity == "medium":
        func = random.choice(medium_functions)
        description = "Función trigonométrica o exponencial"
    else:
        func = random.choice(complex_functions)
        description = "Función combinada compleja"
    
    return {
        "function": func,
        "description": description,
        "type": complexity
    }

def generate_random_bounds() -> Tuple[str, str]:
    """
    Genera límites de integración aleatorios.
    
    Returns:
        Tupla (límite_inferior, límite_superior)
    """
    
    bound_options = [
        ("0", "1"),
        ("0", "2"), 
        ("0", "3"),
        ("1", "2"),
        ("-1", "1"),
        ("-2", "2"),
        ("1", "3"),
        ("0", "4"),
        ("-1", "2"),
        ("1", "4")
    ]
    
    return random.choice(bound_options)

def generate_engineering_scenario() -> Dict[str, str]:
    """
    Genera un escenario de ingeniería aleatorio.
    
    Returns:
        Dict con título, descripción, función y límites
    """
    
    scenarios = [
        {
            "title": "Análisis de Uso de Memoria",
            "description": "Calcular el área bajo la curva de consumo de memoria durante la ejecución",
            "context": "memoria",
            "unit": "MB·segundo"
        },
        {
            "title": "Tiempo de Respuesta del Sistema",
            "description": "Integral del tiempo de respuesta en función de la carga del sistema",
            "context": "rendimiento",
            "unit": "ms·solicitud"
        },
        {
            "title": "Consumo de CPU por Proceso",
            "description": "Área bajo la curva de utilización de CPU a lo largo del tiempo",
            "context": "cpu",
            "unit": "%·segundo"
        },
        {
            "title": "Throughput de Red",
            "description": "Integral del flujo de datos transmitidos en el tiempo",
            "context": "red",
            "unit": "MB·segundo"
        },
        {
            "title": "Carga de Trabajo del Servidor",
            "description": "Calcular la carga total acumulada durante un período",
            "context": "servidor",
            "unit": "unidades·hora"
        },
        {
            "title": "Análisis de Latencia",
            "description": "Integral de la latencia promedio en función del número de usuarios",
            "context": "latencia",
            "unit": "ms·usuario"
        },
        {
            "title": "Consumo de Energía",
            "description": "Área bajo la curva de consumo energético del sistema",
            "context": "energia",
            "unit": "W·hora"
        },
        {
            "title": "Tasa de Errores",
            "description": "Integral de la tasa de errores durante el monitoreo",
            "context": "errores",
            "unit": "errores·minuto"
        }
    ]
    
    scenario = random.choice(scenarios)
    func_data = generate_random_function("medium")
    bounds = generate_random_bounds()
    
    return {
        "title": scenario["title"],
        "description": scenario["description"],
        "function": func_data["function"],
        "lower_bound": bounds[0],
        "upper_bound": bounds[1],
        "context": scenario["context"],
        "unit": scenario["unit"],
        "complexity": func_data["type"]
    }

def generate_riemann_scenario() -> Dict[str, any]:
    """
    Genera un escenario de suma de Riemann aleatorio.
    
    Returns:
        Dict con función, límites, subdivisiones y método
    """
    
    func_data = generate_random_function("simple")  # Usar funciones simples para Riemann
    bounds = generate_random_bounds()
    
    # Evitar límites con pi para sumas de Riemann (más fácil de calcular)
    simple_bounds = [
        ("0", "1"),
        ("0", "2"), 
        ("1", "3"),
        ("-1", "1"),
        ("0", "4")
    ]
    bounds = random.choice(simple_bounds)
    
    subdivisions = random.choice([4, 6, 8, 10, 12])
    method = random.choice(["left", "right", "midpoint"])
    
    method_names = {
        "left": "Punto izquierdo",
        "right": "Punto derecho", 
        "midpoint": "Punto medio"
    }
    
    return {
        "function": func_data["function"],
        "lower_bound": bounds[0],
        "upper_bound": bounds[1],
        "subdivisions": subdivisions,
        "method": method,
        "method_name": method_names[method],
        "description": f"Aproximación usando {subdivisions} subdivisiones con {method_names[method].lower()}"
    }

def generate_area_between_curves_scenario() -> Dict[str, str]:
    """
    Genera un escenario de área entre curvas aleatorio.
    
    Returns:
        Dict con dos funciones y límites
    """
    
    curve_pairs = [
        {
            "func1": "x**2",
            "func2": "x**3",
            "bounds": ("0", "1"),
            "description": "Área entre parábola y función cúbica"
        },
        {
            "func1": "sin(x)",
            "func2": "cos(x)", 
            "bounds": ("0", "1"),
            "description": "Área entre funciones trigonométricas"
        },
        {
            "func1": "x**2",
            "func2": "2*x",
            "bounds": ("0", "2"),
            "description": "Área entre parábola y línea recta"
        },
        {
            "func1": "x + 1",
            "func2": "x**2",
            "bounds": ("0", "1"),
            "description": "Área entre línea y parábola"
        },
        {
            "func1": "x**3",
            "func2": "x",
            "bounds": ("0", "1"),
            "description": "Área entre función cúbica y línea"
        }
    ]
    
    scenario = random.choice(curve_pairs)
    
    return {
        "function1": scenario["func1"],
        "function2": scenario["func2"],
        "lower_bound": scenario["bounds"][0],
        "upper_bound": scenario["bounds"][1],
        "description": scenario["description"]
    }