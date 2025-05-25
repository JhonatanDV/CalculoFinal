import random
import numpy as np
import sympy as sp
from typing import Dict, List, Tuple
from .expression_parser import safe_sympify, evaluate_expression_at_point

# Engineering function templates with proper mathematical expressions
ENGINEERING_TEMPLATES = [
    # Server resource usage patterns
    {
        "type": "exponential_decay",
        "functions": [
            "50*exp(-0.1*t)",
            "100*exp(-0.2*t)", 
            "75*exp(-0.15*t)",
            "25*exp(-0.05*t)",
            "150*exp(-0.3*t)"
        ],
        "contexts": [
            "Uso de CPU del servidor durante optimización",
            "Consumo de memoria en proceso de carga",
            "Tráfico de red después de pico",
            "Uso de recursos en caché",
            "Degradación de rendimiento"
        ],
        "units": ["MB/min", "% CPU", "GB/h", "requests/s", "MB/s"]
    },
    
    # Polynomial growth patterns
    {
        "type": "polynomial",
        "functions": [
            "t**2 + 3*t + 2",
            "2*t**2 + t + 5",
            "t**3 - 2*t**2 + 4",
            "3*t**2 - t + 1",
            "t**2 + 5*t"
        ],
        "contexts": [
            "Complejidad temporal de algoritmo",
            "Crecimiento de base de datos",
            "Uso de memoria por número de usuarios",
            "Tiempo de respuesta con carga",
            "Consumo de ancho de banda"
        ],
        "units": ["ms", "MB", "GB", "seconds", "Mbps"]
    },
    
    # Trigonometric patterns (for cyclical behavior)
    {
        "type": "trigonometric",
        "functions": [
            "10 + 5*sin(t)",
            "20 + 8*cos(2*t)",
            "15*sin(t) + 10",
            "25 + 10*cos(t)",
            "30*sin(0.5*t) + 20"
        ],
        "contexts": [
            "Carga de usuarios durante el día",
            "Uso de CPU en ciclos",
            "Tráfico de red por hora",
            "Consumo de memoria cíclico",
            "Requests por minuto en horario laboral"
        ],
        "units": ["users", "% CPU", "MB/s", "GB", "requests/min"]
    },
    
    # Logarithmic growth
    {
        "type": "logarithmic",
        "functions": [
            "10*log(t + 1)",
            "5*log(2*t + 1) + 3",
            "15*log(t) + 5",
            "8*log(t + 2)",
            "12*log(0.5*t + 1) + 2"
        ],
        "contexts": [
            "Tiempo de búsqueda en estructura optimizada",
            "Overhead de indexación",
            "Latencia de consulta con caché",
            "Tiempo de compilación incremental",
            "Convergencia de algoritmo iterativo"
        ],
        "units": ["ms", "seconds", "μs", "minutes", "iterations"]
    },
    
    # Rational functions (asymptotic behavior)
    {
        "type": "rational",
        "functions": [
            "100/(t + 1)",
            "50*t/(t^2 + 4)",
            "200/(2*t + 3)",
            "t^2/(t + 5)",
            "150/(t^2 + 1)"
        ],
        "contexts": [
            "Eficiencia de algoritmo con tamaño de entrada",
            "Throughput de sistema con carga",
            "Precisión vs velocidad en ML",
            "Cache hit rate con tiempo",
            "Convergencia de optimización"
        ],
        "units": ["ops/s", "requests/s", "accuracy %", "hit rate %", "error rate"]
    }
]

# Engineering scenario titles and descriptions
SCENARIO_TEMPLATES = [
    {
        "title": "Optimización de Rendimiento del Servidor",
        "description_template": "Un servidor web experimenta {context} modelado por la función f(t) = {function}, donde t representa el tiempo en {time_unit}. Calcula el valor acumulado total en el intervalo dado.",
        "time_units": ["minutos", "horas", "segundos", "días"]
    },
    {
        "title": "Análisis de Carga de Sistema",
        "description_template": "El sistema de producción tiene {context} que sigue el patrón f(t) = {function}. Determina la métrica acumulada durante el período especificado.",
        "time_units": ["minutos", "horas", "días", "segundos"]
    },
    {
        "title": "Evaluación de Algoritmos",
        "description_template": "Un algoritmo presenta {context} descrito por f(t) = {function}. Calcula el comportamiento integrado sobre el rango de entrada dado.",
        "time_units": ["iteraciones", "elementos", "operaciones", "pasos"]
    },
    {
        "title": "Monitoreo de Recursos",
        "description_template": "El monitoreo del sistema muestra {context} siguiendo f(t) = {function}. Evalúa el consumo total de recursos en el intervalo.",
        "time_units": ["minutos", "horas", "segundos", "días"]
    },
    {
        "title": "Análisis de Capacidad",
        "description_template": "La capacidad del sistema experimenta {context} modelada por f(t) = {function}. Determina la capacidad acumulada total.",
        "time_units": ["horas", "días", "minutos", "semanas"]
    }
]

def generate_safe_bounds(function_template: Dict, function_str: str) -> Tuple[float, float]:
    """
    Generate safe integration bounds based on function type and validation.
    
    Args:
        function_template (Dict): Function template information
        function_str (str): The actual function string
    
    Returns:
        Tuple[float, float]: (lower_bound, upper_bound)
    """
    func_type = function_template["type"]
    
    # Define bounds based on function type
    if func_type == "exponential_decay":
        # For exponential decay, use positive bounds
        bounds_options = [(0, 10), (0, 20), (1, 15), (0, 30), (2, 12)]
    elif func_type == "polynomial":
        # For polynomials, use various ranges
        bounds_options = [(0, 5), (1, 10), (-2, 3), (0, 8), (1, 6)]
    elif func_type == "trigonometric":
        # For trig functions, use ranges that capture cycles
        bounds_options = [(0, 6.28), (0, 3.14), (-3.14, 3.14), (0, 12.56), (0, 9.42)]
    elif func_type == "logarithmic":
        # For log functions, use positive bounds only
        bounds_options = [(1, 10), (2, 20), (1, 15), (3, 12), (1, 8)]
    elif func_type == "rational":
        # For rational functions, avoid potential asymptotes
        bounds_options = [(1, 10), (2, 8), (0.5, 5), (1, 12), (2, 15)]
    else:
        # Default bounds
        bounds_options = [(0, 5), (1, 10), (-2, 2), (0, 8)]
    
    # Try each bounds option and validate
    for lower, upper in bounds_options:
        try:
            # Parse function and test evaluation
            success, expr = safe_sympify(function_str, "t")
            if success:
                # Test evaluation at a few points
                test_points = np.linspace(lower, upper, 5)
                all_valid = True
                
                for point in test_points:
                    eval_success, value = evaluate_expression_at_point(expr, "t", point)
                    if not eval_success or abs(value) > 1e6 or np.isnan(value) or np.isinf(value):
                        all_valid = False
                        break
                
                if all_valid:
                    return lower, upper
        except:
            continue
    
    # Fallback bounds if nothing else works
    return 0, 5

def generate_engineering_scenario() -> Dict:
    """
    Generate a random engineering scenario with validated mathematical functions.
    
    Returns:
        Dict: Complete scenario with function, bounds, context, etc.
    """
    # Select random template categories
    template = random.choice(ENGINEERING_TEMPLATES)
    scenario = random.choice(SCENARIO_TEMPLATES)
    
    # Select random function from template
    function_str = random.choice(template["functions"])
    context = random.choice(template["contexts"])
    unit = random.choice(template["units"])
    time_unit = random.choice(scenario["time_units"])
    
    # Generate safe bounds for the function
    lower_bound, upper_bound = generate_safe_bounds(template, function_str)
    
    # Create description
    description = scenario["description_template"].format(
        context=context.lower(),
        function=function_str,
        time_unit=time_unit
    )
    
    # Determine complexity level
    complexity = get_scenario_complexity(function_str, template["type"])
    
    return {
        "title": scenario["title"],
        "description": description,
        "function": function_str,
        "lower_bound": str(lower_bound),
        "upper_bound": str(upper_bound),
        "variable": "t",
        "context": context,
        "unit": unit,
        "time_unit": time_unit,
        "complexity": complexity,
        "function_type": template["type"]
    }

def get_scenario_complexity(function_str: str, function_type: str) -> str:
    """
    Determine complexity level of a scenario based on function.
    
    Args:
        function_str (str): Function string
        function_type (str): Type of function
    
    Returns:
        str: Complexity level
    """
    try:
        success, expr = safe_sympify(function_str, "t")
        if not success:
            return "moderate"
        
        # Count mathematical operations and functions
        function_count = len(expr.atoms(sp.Function))
        has_trig = any(isinstance(f, (sp.sin, sp.cos, sp.tan)) for f in expr.atoms(sp.Function))
        has_exp = any(isinstance(f, sp.exp) for f in expr.atoms(sp.Function))
        has_log = any(isinstance(f, sp.log) for f in expr.atoms(sp.Function))
        
        # Determine polynomial degree
        try:
            degree = sp.degree(expr, sp.Symbol('t'))
            if degree is None:
                degree = 0
        except:
            degree = 0
        
        # Classify complexity
        if has_exp or has_log or degree > 3 or function_count > 2:
            return "alta"
        elif has_trig or degree > 1 or function_count > 0:
            return "media"
        else:
            return "baja"
    except:
        return "media"

def generate_multiple_scenarios(count: int = 5) -> List[Dict]:
    """
    Generate multiple unique engineering scenarios.
    
    Args:
        count (int): Number of scenarios to generate
    
    Returns:
        List[Dict]: List of generated scenarios
    """
    scenarios = []
    used_functions = set()
    
    max_attempts = count * 3  # Prevent infinite loops
    attempts = 0
    
    while len(scenarios) < count and attempts < max_attempts:
        scenario = generate_engineering_scenario()
        
        # Ensure uniqueness by function
        if scenario["function"] not in used_functions:
            scenarios.append(scenario)
            used_functions.add(scenario["function"])
        
        attempts += 1
    
    return scenarios

def validate_scenario(scenario: Dict) -> Tuple[bool, str]:
    """
    Validate that a generated scenario is mathematically sound.
    
    Args:
        scenario (Dict): Scenario to validate
    
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    try:
        # Validate function parsing
        success, expr = safe_sympify(scenario["function"], scenario["variable"])
        if not success:
            return False, f"Invalid function: {expr}"
        
        # Validate bounds
        try:
            lower = float(scenario["lower_bound"])
            upper = float(scenario["upper_bound"])
            
            if lower >= upper:
                return False, "Invalid bounds: lower >= upper"
                
        except ValueError:
            return False, "Invalid bound values"
        
        # Test function evaluation at bounds
        success_lower, _ = evaluate_expression_at_point(expr, scenario["variable"], lower)
        success_upper, _ = evaluate_expression_at_point(expr, scenario["variable"], upper)
        
        if not success_lower:
            return False, "Function undefined at lower bound"
        if not success_upper:
            return False, "Function undefined at upper bound"
        
        # Test midpoint evaluation
        midpoint = (lower + upper) / 2
        success_mid, value_mid = evaluate_expression_at_point(expr, scenario["variable"], midpoint)
        
        if not success_mid:
            return False, "Function undefined at midpoint"
        
        if abs(value_mid) > 1e10:
            return False, "Function values too large"
        
        return True, ""
        
    except Exception as e:
        return False, f"Validation error: {str(e)}"

def get_scenario_statistics() -> Dict:
    """
    Get statistics about available scenario templates.
    
    Returns:
        Dict: Statistics about templates and functions
    """
    total_functions = sum(len(template["functions"]) for template in ENGINEERING_TEMPLATES)
    total_contexts = sum(len(template["contexts"]) for template in ENGINEERING_TEMPLATES)
    total_scenarios = len(SCENARIO_TEMPLATES)
    
    function_types = [template["type"] for template in ENGINEERING_TEMPLATES]
    
    return {
        "total_function_templates": total_functions,
        "total_contexts": total_contexts,
        "total_scenario_templates": total_scenarios,
        "function_types": function_types,
        "estimated_unique_combinations": total_functions * total_contexts * total_scenarios
    }
