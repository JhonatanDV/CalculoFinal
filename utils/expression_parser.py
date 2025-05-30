import sympy as sp
import numpy as np
import re
from typing import Union, Tuple, Any

def safe_sympify(expression: str, variable: str = "x") -> Tuple[bool, Union[sp.Expr, str]]:
    """
    Safely parse a mathematical expression using SymPy with comprehensive error handling.
    
    Args:
        expression (str): Mathematical expression to parse
        variable (str): Variable name (default: 'x')
    
    Returns:
        Tuple[bool, Union[sp.Expr, str]]: (success, parsed_expression_or_error_message)
    """
    if not expression or not expression.strip():
        return False, "Empty expression"
    
    try:
        # Clean and normalize the expression
        cleaned_expr = clean_expression(expression)
        
        # Create symbol
        var = sp.Symbol(variable, real=True)
        
        # Define local namespace with common functions and constants
        local_dict = {
            variable: var,
            'x': var if variable == 'x' else sp.Symbol('x', real=True),
            'y': var if variable == 'y' else sp.Symbol('y', real=True),
            't': var if variable == 't' else sp.Symbol('t', real=True),
            'n': var if variable == 'n' else sp.Symbol('n', real=True),
            'pi': sp.pi,
            'e': sp.E,
            'E': sp.E,  # Alternative for e
            'exp': sp.exp,
            'ln': sp.log,
            'log': sp.log,
            'sin': sp.sin,
            'cos': sp.cos,
            'tan': sp.tan,
            'sqrt': sp.sqrt,
            'abs': sp.Abs,
            'Abs': sp.Abs,
            'atan': sp.atan,
            'asin': sp.asin,
            'acos': sp.acos,
            'sinh': sp.sinh,
            'cosh': sp.cosh,
            'tanh': sp.tanh
        }
        
        # Parse the expression WITHOUT transformations parameter
        parsed_expr = sp.sympify(cleaned_expr, locals=local_dict)
        
        return True, parsed_expr
        
    except Exception as e:
        return False, f"Error parsing expression: {str(e)}"

def clean_expression(expression: str) -> str:
    """Clean and normalize mathematical expression for SymPy parsing."""
    expr = expression.strip()
    
    # AGREGAR ESTAS CORRECCIONES AL INICIO:
    expr = re.sub(r'\bsq1t\b', 'sqrt', expr, flags=re.IGNORECASE)  # sq1t -> sqrt
    expr = re.sub(r'\bsqrt\b', 'sqrt', expr, flags=re.IGNORECASE)  # asegurar sqrt correcto
    # Remove extra whitespace
    expr = expression.strip()
    expr = expr.replace("sq1t", "sqrt")
    expr = expr.replace("sqlt", "sqrt")
    # En clean_expression, después de las otras correcciones:
    expr = re.sub(r'\bsq1t\b', 'sqrt', expr)  # sq1t -> sqrt
    expr = re.sub(r'\bSq1t\b', 'sqrt', expr)  # Sq1t -> sqrt
    expr = re.sub(r'\bSQ1T\b', 'sqrt', expr)  # SQ1T -> sqrt
    # Replace common notations
    expr = expr.replace("^", "**")  # Power notation
    expr = expr.replace("ln(", "log(")  # Natural logarithm
    
    # Fix common SymPy function names (case-insensitive)
    expr = re.sub(r'\bExp\b', 'exp', expr, flags=re.IGNORECASE)
    expr = re.sub(r'\bSin\b', 'sin', expr, flags=re.IGNORECASE)
    expr = re.sub(r'\bCos\b', 'cos', expr, flags=re.IGNORECASE)
    expr = re.sub(r'\bTan\b', 'tan', expr, flags=re.IGNORECASE)
    expr = re.sub(r'\bLog\b', 'log', expr, flags=re.IGNORECASE)
    expr = re.sub(r'\bSqrt\b', 'sqrt', expr, flags=re.IGNORECASE)
    
    # Handle specific problematic patterns first
    # Fix exp function patterns
    expr = re.sub(r'(\d+)\s*\*\s*exp\(', r'\1*exp(', expr)  # Clean up exp multiplication
    expr = re.sub(r'(\d+)exp\(', r'\1*exp(', expr)  # 2exp( -> 2*exp(
    expr = re.sub(r'exp\(([^)]+)\)\s*\*\s*(\w)', r'exp(\1)*\2', expr)  # exp(x)*y
    
    # Handle trigonometric function patterns
    expr = re.sub(r'(\w+)\s*\*\s*sin\(', r'\1*sin(', expr)
    expr = re.sub(r'(\w+)\s*\*\s*cos\(', r'\1*cos(', expr)
    expr = re.sub(r'(\w+)sin\(', r'\1*sin(', expr)  # xsin( -> x*sin(
    expr = re.sub(r'(\w+)cos\(', r'\1*cos(', expr)  # xcos( -> x*cos(
    
    # Handle implicit multiplication more carefully
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)  # 2x -> 2*x
    expr = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expr)  # x2 -> x*2
    expr = re.sub(r'\)(\w)', r')*\1', expr)  # )(var) -> )*(var)
    
    # Clean up multiple asterisks
    expr = re.sub(r'\*+', '*', expr)
    
    return expr

def safe_float_conversion(value: Union[str, float, int, sp.Expr]) -> Tuple[bool, Union[float, str]]:
    """
    Safely convert various types to float with support for symbolic expressions.
    
    Args:
        value: Value to convert to float
    
    Returns:
        Tuple[bool, Union[float, str]]: (success, float_value_or_error_message)
    """
    if value is None:
        return False, "None value provided"
    
    try:
        # CORRECCIÓN: Manejar tipos NumPy primero
        if hasattr(value, 'item'):
            # NumPy array con un elemento
            return True, float(value.item())
        elif isinstance(value, (np.floating, np.integer)):
            # Tipos escalares NumPy
            return True, float(value)
        elif isinstance(value, (int, float)):
            # Tipos Python nativos
            if np.isnan(value) or np.isinf(value):
                return False, f"Invalid numeric value: {value}"
            return True, float(value)
        elif isinstance(value, str):
            # Handle empty strings
            if not value.strip():
                return False, "Empty string"
            
            # Try direct conversion first
            try:
                result = float(value)
                if np.isnan(result) or np.isinf(result):
                    return False, f"Invalid numeric value: {result}"
                return True, result
            except ValueError:
                pass
            
            # Try to parse as symbolic expression
            success, parsed = safe_sympify(value.strip())
            if success:
                try:
                    # Evaluate numerically
                    result = float(parsed.evalf())
                    if np.isnan(result) or np.isinf(result):
                        return False, f"Expression evaluates to invalid value: {result}"
                    return True, result
                except Exception as e:
                    return False, f"Cannot evaluate expression numerically: {str(e)}"
            else:
                return False, f"Cannot parse expression: {parsed}"
        elif hasattr(value, 'evalf'):
            # SymPy expression
            try:
                result = float(value.evalf())
                if np.isnan(result) or np.isinf(result):
                    return False, f"Expression evaluates to invalid value: {result}"
                return True, result
            except Exception as e:
                return False, f"Cannot evaluate SymPy expression: {str(e)}"
        else:
            # Try to convert other types
            result = float(value)
            if np.isnan(result) or np.isinf(result):
                return False, f"Invalid numeric value: {result}"
            return True, result
        
    except Exception as e:
        return False, f"Conversion error: {str(e)}"

def evaluate_expression_at_point(expr: sp.Expr, variable: str, point: float) -> Tuple[bool, Union[float, str]]:
    """
    Safely evaluate a SymPy expression at a specific point.
    
    Args:
        expr (sp.Expr): SymPy expression
        variable (str): Variable name
        point (float): Point to evaluate at
    
    Returns:
        Tuple[bool, Union[float, str]]: (success, result_or_error_message)
    """
    try:
        # CORRECCIÓN DEFINITIVA: Conversión robusta del punto de entrada
        
        # Paso 1: Convertir el punto a float de Python nativo
        if hasattr(point, 'item'):
            # NumPy array con un elemento -> extraer valor nativo
            point_value = point.item()
        elif hasattr(point, 'dtype'):
            # Tipo NumPy escalar -> convertir a Python nativo
            point_value = point.item() if hasattr(point, 'item') else float(point)
        elif isinstance(point, str):
            # String -> parsear como número
            point_value = float(point)
        else:
            # Asumir que ya es un tipo Python nativo
            point_value = point
        
        # Paso 2: Asegurar que es exactamente un float de Python
        point_value = float(point_value)
        
        # Paso 3: Verificar validez del punto
        if not isinstance(point_value, float):
            return False, f"Point conversion failed: {type(point_value)}"
        
        if np.isnan(point_value) or np.isinf(point_value):
            return False, f"Invalid point value: {point_value}"
        
        # Paso 4: Crear símbolo con el mismo nombre de variable
        var_symbol = sp.Symbol(variable, real=True)
        
        # Paso 5: Realizar sustitución directa con valor Python nativo
        try:
            # Usar float puro de Python para evitar problemas con NumPy
            substituted = expr.subs(var_symbol, point_value)
        except Exception as subs_error:
            return False, f"Substitution error at {variable} = {point_value}: {str(subs_error)}"
        
        # Paso 6: Evaluar el resultado
        try:
            if substituted.is_number:
                # Es un número directo
                if hasattr(substituted, 'evalf'):
                    result_value = float(substituted.evalf())
                else:
                    result_value = float(substituted)
            else:
                # Necesita evaluación numérica
                numerical_result = substituted.evalf()
                
                if hasattr(numerical_result, 'is_real') and numerical_result.is_real is False:
                    return False, f"Result has imaginary component at {variable} = {point_value}"
                
                # Extraer parte real si es complejo
                if hasattr(numerical_result, 're'):
                    result_value = float(numerical_result.re)
                else:
                    result_value = float(numerical_result)
                    
        except Exception as eval_error:
            return False, f"Evaluation error at {variable} = {point_value}: {str(eval_error)}"
        
        # Paso 7: Verificar validez del resultado
        if not isinstance(result_value, (int, float)):
            return False, f"Result is not numeric: {type(result_value)}"
        
        if np.isnan(result_value):
            return False, f"Function undefined at {variable} = {point_value}: result is NaN"
        
        if np.isinf(result_value):
            return False, f"Function approaches infinity at {variable} = {point_value}"
        
        return True, float(result_value)
        
    except ZeroDivisionError:
        return False, f"Division by zero at {variable} = {point_value}"
    except OverflowError:
        return False, f"Numerical overflow at {variable} = {point_value}"
    except Exception as e:
        # Capturar el error específico que estás viendo
        error_msg = str(e)
        if "could not convert string to float" in error_msg:
            return False, f"Type conversion error at {variable} = {point}: NumPy type not properly converted"
        else:
            return False, f"Unexpected error at {variable} = {point}: {error_msg}"

def validate_expression_domain(expr: sp.Expr, variable: str, lower_bound: float, upper_bound: float, num_points: int = 10) -> Tuple[bool, str]:
    """
    Validate that an expression is well-defined over a given domain.
    
    Args:
        expr (sp.Expr): SymPy expression
        variable (str): Variable name
        lower_bound (float): Lower bound of domain
        upper_bound (float): Upper bound of domain
        num_points (int): Number of test points
    
    Returns:
        Tuple[bool, str]: (is_valid, error_message_if_invalid)
    """
    try:
        # Generate test points
        test_points = np.linspace(lower_bound, upper_bound, num_points)
        
        # Test evaluation at each point
        for point in test_points:
            success, result = evaluate_expression_at_point(expr, variable, point)
            if not success:
                return False, f"Expression undefined at {variable} = {point}: {result}"
        
        return True, ""
        
    except Exception as e:
        return False, f"Domain validation error: {str(e)}"

def get_expression_complexity(expr: sp.Expr) -> str:
    """
    Determine the complexity level of a mathematical expression.
    
    Args:
        expr (sp.Expr): SymPy expression
    
    Returns:
        str: Complexity level ('simple', 'moderate', 'complex')
    """
    try:
        # Count different types of functions
        functions = expr.atoms(sp.Function)
        has_trig = any(isinstance(f, (sp.sin, sp.cos, sp.tan)) for f in functions)
        has_exp = any(isinstance(f, sp.exp) for f in functions)
        has_log = any(isinstance(f, sp.log) for f in functions)
        
        # Check degree of polynomials
        free_symbols = expr.free_symbols
        if len(free_symbols) == 1:
            var = list(free_symbols)[0]
            try:
                degree = sp.degree(expr, var)
                if degree is None:
                    degree = 0
            except:
                degree = 0
        else:
            degree = 0
        
        # Classify complexity
        if has_exp or has_log or has_trig or degree > 3:
            return "complex"
        elif degree > 1 or len(functions) > 0:
            return "moderate"
        else:
            return "simple"
            
    except:
        return "moderate"
def safe_numpy_to_python(value):
    """
    Convertir valores NumPy a tipos nativos de Python de manera segura.
    
    Args:
        value: Valor a convertir (puede ser NumPy o Python nativo)
    
    Returns:
        Valor convertido a tipo Python nativo
    """
    try:
        if hasattr(value, 'item'):
            # NumPy array con un elemento
            return value.item()
        elif isinstance(value, (np.floating, np.integer)):
            # Tipos escalares NumPy
            return float(value) if isinstance(value, np.floating) else int(value)
        elif isinstance(value, np.ndarray):
            # Array NumPy, tomar primer elemento
            return value.flat[0] if value.size > 0 else 0.0
        else:
            # Ya es tipo Python nativo
            return value
    except Exception:
        # En caso de error, retornar 0
        return 0.0
    

def debug_point_conversion(point):
    """
    Función de debug para identificar problemas de conversión de tipos.
    """
    print(f"Original point: {point}")
    print(f"Point type: {type(point)}")
    print(f"Has item method: {hasattr(point, 'item')}")
    print(f"Has dtype: {hasattr(point, 'dtype')}")
    
    if hasattr(point, 'item'):
        converted = point.item()
        print(f"After .item(): {converted}, type: {type(converted)}")
    else:
        converted = float(point)
        print(f"After float(): {converted}, type: {type(converted)}")
    
    return converted