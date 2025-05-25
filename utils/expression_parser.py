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
            'Abs': sp.Abs
        }
        
        # Parse the expression
        parsed_expr = sp.sympify(cleaned_expr, locals=local_dict, transformations='all')
        
        return True, parsed_expr
        
    except Exception as e:
        return False, f"Error parsing expression: {str(e)}"

def clean_expression(expression: str) -> str:
    """
    Clean and normalize mathematical expression for SymPy parsing.
    
    Args:
        expression (str): Raw expression
    
    Returns:
        str: Cleaned expression
    """
    # Remove extra whitespace
    expr = expression.strip()
    
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
    
    # Handle implicit multiplication
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)  # 2x -> 2*x
    expr = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expr)  # x2 -> x*2
    expr = re.sub(r'\)(\w)', r')*\1', expr)  # )(var) -> )*(var)
    expr = re.sub(r'(\w)\(', r'\1*(', expr)  # var( -> var*(
    
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
        # If already a number
        if isinstance(value, (int, float)):
            return True, float(value)
        
        # If it's a string
        if isinstance(value, str):
            # Handle empty strings
            if not value.strip():
                return False, "Empty string"
            
            # Try direct conversion first
            try:
                return True, float(value)
            except ValueError:
                pass
            
            # Try to parse as symbolic expression
            success, parsed = safe_sympify(value.strip())
            if success:
                try:
                    # Evaluate numerically
                    result = float(parsed.evalf())
                    return True, result
                except Exception as e:
                    return False, f"Cannot evaluate expression numerically: {str(e)}"
            else:
                return False, f"Cannot parse expression: {parsed}"
        
        # If it's a SymPy expression
        if hasattr(value, 'evalf'):
            try:
                result = float(value.evalf())
                return True, result
            except Exception as e:
                return False, f"Cannot evaluate SymPy expression: {str(e)}"
        
        # Try to convert other types
        return True, float(value)
        
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
        var = sp.Symbol(variable, real=True)
        result = expr.subs(var, point)
        
        # Convert to float
        success, float_result = safe_float_conversion(result)
        if success:
            # Check for NaN or infinity
            if np.isnan(float_result) or np.isinf(float_result):
                return False, f"Invalid result: {float_result}"
            return True, float_result
        else:
            return False, float_result
            
    except Exception as e:
        return False, f"Error evaluating expression: {str(e)}"

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
