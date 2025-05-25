import sympy as sp
import numpy as np
import re
from typing import Union, Tuple, Any

def safe_sympify(expression: str, variable: str = "x") -> Tuple[bool, Union[sp.Expr, str]]:
    """
    Safely parse a mathematical expression using SymPy with comprehensive error handling.
    """
    if not expression or not expression.strip():
        return False, "Empty expression"
    
    try:
        # Clean the expression
        cleaned_expr = clean_expression(expression)
        
        # Create symbol
        var = sp.Symbol(variable, real=True)
        
        # Define local namespace
        local_dict = {
            variable: var,
            'x': var if variable == 'x' else sp.Symbol('x', real=True),
            'y': var if variable == 'y' else sp.Symbol('y', real=True),
            't': var if variable == 't' else sp.Symbol('t', real=True),
            'n': var if variable == 'n' else sp.Symbol('n', real=True),
            'pi': sp.pi,
            'e': sp.E,
            'E': sp.E,
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
        
        # Parse without transformations parameter
        parsed_expr = sp.sympify(cleaned_expr, locals=local_dict)
        
        return True, parsed_expr
        
    except Exception as e:
        return False, f"Error parsing expression: {str(e)}"

def clean_expression(expression: str) -> str:
    """Clean and normalize mathematical expression."""
    expr = expression.strip()
    
    # Replace common notations
    expr = expr.replace("^", "**")
    expr = expr.replace("ln(", "log(")
    
    # Fix function names
    expr = re.sub(r'\bExp\b', 'exp', expr, flags=re.IGNORECASE)
    expr = re.sub(r'\bSin\b', 'sin', expr, flags=re.IGNORECASE)
    expr = re.sub(r'\bCos\b', 'cos', expr, flags=re.IGNORECASE)
    expr = re.sub(r'\bTan\b', 'tan', expr, flags=re.IGNORECASE)
    expr = re.sub(r'\bLog\b', 'log', expr, flags=re.IGNORECASE)
    expr = re.sub(r'\bSqrt\b', 'sqrt', expr, flags=re.IGNORECASE)
    
    # Handle implicit multiplication
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
    expr = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expr)
    expr = re.sub(r'\)(\w)', r')*\1', expr)
    expr = re.sub(r'(\w)\(', r'\1*(', expr)
    
    return expr

def safe_float_conversion(value: Union[str, float, int, sp.Expr]) -> Tuple[bool, Union[float, str]]:
    """Safely convert values to float."""
    if value is None:
        return False, "None value provided"
    
    try:
        if isinstance(value, (int, float)):
            return True, float(value)
        
        if isinstance(value, str):
            if not value.strip():
                return False, "Empty string"
            
            try:
                return True, float(value)
            except ValueError:
                pass
            
            success, parsed = safe_sympify(value.strip())
            if success:
                try:
                    result = float(parsed.evalf())
                    return True, result
                except Exception as e:
                    return False, f"Cannot evaluate expression numerically: {str(e)}"
            else:
                return False, f"Cannot parse expression: {parsed}"
        
        if hasattr(value, 'evalf'):
            try:
                result = float(value.evalf())
                return True, result
            except Exception as e:
                return False, f"Cannot evaluate SymPy expression: {str(e)}"
        
        return True, float(value)
        
    except Exception as e:
        return False, f"Conversion error: {str(e)}"

def evaluate_expression_at_point(expr: sp.Expr, variable: str, point: float) -> Tuple[bool, Union[float, str]]:
    """Safely evaluate a SymPy expression at a specific point."""
    try:
        var = sp.Symbol(variable, real=True)
        result = expr.subs(var, point)
        
        success, float_result = safe_float_conversion(result)
        if success:
            if np.isnan(float_result) or np.isinf(float_result):
                return False, f"Invalid result: {float_result}"
            return True, float_result
        else:
            return False, float_result
            
    except Exception as e:
        return False, f"Error evaluating expression: {str(e)}"