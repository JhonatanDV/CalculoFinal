import numpy as np
import sympy as sp
from typing import Tuple, Union, List
from .expression_parser import safe_sympify, safe_float_conversion, validate_expression_domain

def validate_function_input(function_str: str, variable: str = "x") -> Tuple[bool, str, sp.Expr]:
    """
    Validate a function input string.
    
    Args:
        function_str (str): Function string to validate
        variable (str): Variable name
    
    Returns:
        Tuple[bool, str, sp.Expr]: (is_valid, error_message, parsed_expression)
    """
    if not function_str or not function_str.strip():
        return False, "Function cannot be empty", None
    
    # Parse the expression
    success, result = safe_sympify(function_str, variable)
    if not success:
        return False, f"Invalid function syntax: {result}", None
    
    expr = result
    
    # Check if expression contains the variable (or is a constant)
    free_symbols = expr.free_symbols
    var_symbol = sp.Symbol(variable, real=True)
    
    if free_symbols and var_symbol not in free_symbols:
        # Check if it's using a different variable name
        if len(free_symbols) == 1:
            # Suggest the correct variable
            found_var = list(free_symbols)[0]
            return False, f"Function uses variable '{found_var}' but expected '{variable}'", None
        elif len(free_symbols) > 1:
            return False, f"Function contains multiple variables: {[str(s) for s in free_symbols]}", None
    
    return True, "", expr

def validate_bounds(lower_bound: str, upper_bound: str) -> Tuple[bool, str, float, float]:
    """
    Validate integration bounds.
    
    Args:
        lower_bound (str): Lower bound string
        upper_bound (str): Upper bound string
    
    Returns:
        Tuple[bool, str, float, float]: (is_valid, error_message, lower_float, upper_float)
    """
    # Validate lower bound
    success_lower, result_lower = safe_float_conversion(lower_bound)
    if not success_lower:
        return False, f"Invalid lower bound: {result_lower}", None, None
    
    # Validate upper bound
    success_upper, result_upper = safe_float_conversion(upper_bound)
    if not success_upper:
        return False, f"Invalid upper bound: {result_upper}", None, None
    
    lower_val = result_lower
    upper_val = result_upper
    
    # Check that lower < upper
    if lower_val >= upper_val:
        return False, f"Lower bound ({lower_val}) must be less than upper bound ({upper_val})", None, None
    
    # Check for reasonable bounds (prevent extremely large computations)
    if abs(upper_val - lower_val) > 1000:
        return False, "Integration interval is too large (>1000 units)", None, None
    
    if abs(lower_val) > 10000 or abs(upper_val) > 10000:
        return False, "Bounds are too large (absolute value >10000)", None, None
    
    return True, "", lower_val, upper_val

def validate_subdivisions(n: int) -> Tuple[bool, str]:
    """
    Validate number of subdivisions for Riemann sums.
    
    Args:
        n (int): Number of subdivisions
    
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    if not isinstance(n, int):
        return False, "Number of subdivisions must be an integer"
    
    if n <= 0:
        return False, "Number of subdivisions must be positive"
    
    if n > 10000:
        return False, "Number of subdivisions is too large (>10000)"
    
    return True, ""

def validate_integration_inputs(function_str: str, lower_bound: str, upper_bound: str, variable: str = "x") -> Tuple[bool, str, sp.Expr, float, float]:
    """
    Validate all inputs for integration calculations.
    
    Args:
        function_str (str): Function string
        lower_bound (str): Lower bound string
        upper_bound (str): Upper bound string
        variable (str): Variable name
    
    Returns:
        Tuple[bool, str, sp.Expr, float, float]: (is_valid, error_message, expr, lower_val, upper_val)
    """
    # Validate function
    func_valid, func_error, expr = validate_function_input(function_str, variable)
    if not func_valid:
        return False, func_error, None, None, None
    
    # Validate bounds
    bounds_valid, bounds_error, lower_val, upper_val = validate_bounds(lower_bound, upper_bound)
    if not bounds_valid:
        return False, bounds_error, None, None, None
    
    # Validate domain
    domain_valid, domain_error = validate_expression_domain(expr, variable, lower_val, upper_val)
    if not domain_valid:
        return False, f"Function domain error: {domain_error}", None, None, None
    
    return True, "", expr, lower_val, upper_val

def validate_riemann_inputs(function_str: str, lower_bound: str, upper_bound: str, n: int, variable: str = "x") -> Tuple[bool, str, sp.Expr, float, float]:
    """
    Validate all inputs for Riemann sum calculations.
    
    Args:
        function_str (str): Function string
        lower_bound (str): Lower bound string
        upper_bound (str): Upper bound string
        n (int): Number of subdivisions
        variable (str): Variable name
    
    Returns:
        Tuple[bool, str, sp.Expr, float, float]: (is_valid, error_message, expr, lower_val, upper_val)
    """
    # Validate integration inputs
    valid, error, expr, lower_val, upper_val = validate_integration_inputs(function_str, lower_bound, upper_bound, variable)
    if not valid:
        return False, error, None, None, None
    
    # Validate subdivisions
    n_valid, n_error = validate_subdivisions(n)
    if not n_valid:
        return False, n_error, None, None, None
    
    return True, "", expr, lower_val, upper_val

def validate_two_functions(func1_str: str, func2_str: str, lower_bound: str, upper_bound: str, variable: str = "x") -> Tuple[bool, str, sp.Expr, sp.Expr, float, float]:
    """
    Validate inputs for area between curves calculations.
    
    Args:
        func1_str (str): First function string
        func2_str (str): Second function string
        lower_bound (str): Lower bound string
        upper_bound (str): Upper bound string
        variable (str): Variable name
    
    Returns:
        Tuple[bool, str, sp.Expr, sp.Expr, float, float]: (is_valid, error_message, expr1, expr2, lower_val, upper_val)
    """
    # Validate first function
    func1_valid, func1_error, expr1 = validate_function_input(func1_str, variable)
    if not func1_valid:
        return False, f"First function error: {func1_error}", None, None, None, None
    
    # Validate second function
    func2_valid, func2_error, expr2 = validate_function_input(func2_str, variable)
    if not func2_valid:
        return False, f"Second function error: {func2_error}", None, None, None, None
    
    # Validate bounds
    bounds_valid, bounds_error, lower_val, upper_val = validate_bounds(lower_bound, upper_bound)
    if not bounds_valid:
        return False, bounds_error, None, None, None, None
    
    # Validate domain for both functions
    domain1_valid, domain1_error = validate_expression_domain(expr1, variable, lower_val, upper_val)
    if not domain1_valid:
        return False, f"First function domain error: {domain1_error}", None, None, None, None
    
    domain2_valid, domain2_error = validate_expression_domain(expr2, variable, lower_val, upper_val)
    if not domain2_valid:
        return False, f"Second function domain error: {domain2_error}", None, None, None, None
    
    return True, "", expr1, expr2, lower_val, upper_val

def suggest_bounds_for_functions(expr1: sp.Expr, expr2: sp.Expr, variable: str = "x") -> List[Tuple[float, float]]:
    """
    Suggest reasonable bounds for two functions based on their intersection points.
    
    Args:
        expr1 (sp.Expr): First expression
        expr2 (sp.Expr): Second expression
        variable (str): Variable name
    
    Returns:
        List[Tuple[float, float]]: List of suggested (lower, upper) bound pairs
    """
    try:
        var = sp.Symbol(variable, real=True)
        
        # Find intersection points
        eq = sp.Eq(expr1, expr2)
        intersections = sp.solve(eq, var)
        
        # Convert to floats and filter real solutions
        real_intersections = []
        for point in intersections:
            try:
                success, float_val = safe_float_conversion(point)
                if success and abs(float_val) < 1000:  # Reasonable range
                    real_intersections.append(float_val)
            except:
                continue
        
        real_intersections.sort()
        
        suggestions = []
        
        if len(real_intersections) >= 2:
            # Suggest intervals between consecutive intersections
            for i in range(len(real_intersections) - 1):
                lower = real_intersections[i]
                upper = real_intersections[i + 1]
                if upper - lower > 0.01:  # Minimum interval size
                    suggestions.append((lower, upper))
        
        # Add some default suggestions if no intersections found
        if not suggestions:
            suggestions = [(-5, 5), (-2, 2), (0, 10), (-10, 0)]
        
        return suggestions[:5]  # Return at most 5 suggestions
        
    except Exception:
        return [(-5, 5), (-2, 2), (0, 10)]
