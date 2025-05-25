import sympy as sp
import numpy as np
from typing import Tuple, List, Dict, Union
from .expression_parser import safe_sympify, evaluate_expression_at_point
from .validation import validate_riemann_inputs

def calculate_riemann_sum(function_str: str, lower_bound: float, upper_bound: float, 
                         n: int, method: str = "left", variable: str = "x") -> Tuple[float, List[float]]:
    """
    Calculate Riemann sum with comprehensive error handling.
    
    Args:
        function_str (str): Function to integrate
        lower_bound (float): Lower bound
        upper_bound (float): Upper bound
        n (int): Number of subdivisions
        method (str): Method ('left', 'right', 'midpoint')
        variable (str): Variable name
    
    Returns:
        Tuple[float, List[float]]: (riemann_sum, list_of_rectangle_areas)
    """
    # Validate inputs
    valid, error, expr, lower_val, upper_val = validate_riemann_inputs(
        function_str, str(lower_bound), str(upper_bound), n, variable
    )
    if not valid:
        raise ValueError(error)
    
    # Calculate delta x
    delta_x = (upper_val - lower_val) / n
    
    # Generate sample points based on method
    sample_points = []
    rectangle_areas = []
    
    for i in range(n):
        x_left = lower_val + i * delta_x
        x_right = lower_val + (i + 1) * delta_x
        
        if method == "left":
            sample_point = x_left
        elif method == "right":
            sample_point = x_right
        elif method == "midpoint":
            sample_point = (x_left + x_right) / 2
        else:
            raise ValueError(f"Unknown method: {method}")
        
        sample_points.append(sample_point)
        
        # Evaluate function at sample point
        success, function_value = evaluate_expression_at_point(expr, variable, sample_point)
        if not success:
            raise ValueError(f"Error evaluating function at {variable} = {sample_point}: {function_value}")
        
        # Calculate rectangle area
        area = function_value * delta_x
        rectangle_areas.append(area)
    
    # Calculate total Riemann sum
    riemann_sum = sum(rectangle_areas)
    
    return riemann_sum, rectangle_areas

def get_riemann_sum_steps(function_str: str, lower_bound: float, upper_bound: float, 
                         n: int, method: str = "left", variable: str = "x") -> List[str]:
    """
    Generate step-by-step solution for Riemann sum calculation.
    
    Args:
        function_str (str): Function to integrate
        lower_bound (float): Lower bound
        upper_bound (float): Upper bound
        n (int): Number of subdivisions
        method (str): Method ('left', 'right', 'midpoint')
        variable (str): Variable name
    
    Returns:
        List[str]: Step-by-step solution
    """
    steps = []
    
    # Parse the function
    success, expr = safe_sympify(function_str, variable)
    if not success:
        raise ValueError(f"Invalid function: {expr}")
    
    # Step 1: Problem setup
    steps.append(f"**Step 1**: Set up the Riemann sum")
    steps.append(f"Function: $f({variable}) = {sp.latex(expr)}$")
    steps.append(f"Interval: $[{lower_bound}, {upper_bound}]$")
    steps.append(f"Number of subdivisions: $n = {n}$")
    steps.append(f"Method: {method.title()} endpoint")
    
    # Step 2: Calculate Δx
    delta_x = (upper_bound - lower_bound) / n
    steps.append(f"**Step 2**: Calculate the width of each subdivision")
    steps.append(f"$$\\Delta {variable} = \\frac{{b - a}}{{n}} = \\frac{{{upper_bound} - {lower_bound}}}{{{n}}} = {delta_x:.6f}$$")
    
    # Step 3: Identify sample points
    steps.append(f"**Step 3**: Identify sample points using {method} endpoint method")
    
    sample_points = []
    for i in range(n):
        x_left = lower_bound + i * delta_x
        x_right = lower_bound + (i + 1) * delta_x
        
        if method == "left":
            sample_point = x_left
            formula = f"{variable}_{{{i}}} = a + {i} \\cdot \\Delta {variable} = {lower_bound} + {i} \\cdot {delta_x:.6f} = {sample_point:.6f}"
        elif method == "right":
            sample_point = x_right
            formula = f"{variable}_{{{i}}} = a + {i+1} \\cdot \\Delta {variable} = {lower_bound} + {i+1} \\cdot {delta_x:.6f} = {sample_point:.6f}"
        elif method == "midpoint":
            sample_point = (x_left + x_right) / 2
            formula = f"{variable}_{{{i}}} = \\frac{{{x_left:.6f} + {x_right:.6f}}}{{2}} = {sample_point:.6f}"
        
        sample_points.append(sample_point)
        steps.append(f"$${formula}$$")
    
    # Step 4: Evaluate function at sample points
    steps.append(f"**Step 4**: Evaluate $f({variable})$ at each sample point")
    
    function_values = []
    for i, point in enumerate(sample_points):
        success, value = evaluate_expression_at_point(expr, variable, point)
        if not success:
            raise ValueError(f"Error evaluating function at {point}: {value}")
        
        function_values.append(value)
        steps.append(f"$$f({point:.6f}) = {value:.6f}$$")
    
    # Step 5: Calculate Riemann sum
    steps.append(f"**Step 5**: Calculate the Riemann sum")
    steps.append(f"$$R_n = \\Delta {variable} \\sum_{{i=0}}^{{{n-1}}} f({variable}_i)$$")
    
    # Show the sum calculation
    sum_terms = " + ".join([f"{val:.6f}" for val in function_values])
    steps.append(f"$$R_n = {delta_x:.6f} \\times ({sum_terms})$$")
    
    total_sum = sum(function_values)
    riemann_sum = delta_x * total_sum
    steps.append(f"$$R_n = {delta_x:.6f} \\times {total_sum:.6f} = {riemann_sum:.6f}$$")
    
    return steps

def compare_riemann_methods(function_str: str, lower_bound: float, upper_bound: float, 
                           n: int, variable: str = "x") -> Dict[str, Union[float, str]]:
    """
    Compare different Riemann sum methods and compute exact integral if possible.
    
    Args:
        function_str (str): Function to integrate
        lower_bound (float): Lower bound
        upper_bound (float): Upper bound
        n (int): Number of subdivisions
        variable (str): Variable name
    
    Returns:
        Dict[str, Union[float, str]]: Comparison results
    """
    try:
        results = {}
        
        # Calculate Riemann sums for all methods
        methods = ['left', 'right', 'midpoint']
        
        for method in methods:
            try:
                riemann_sum, _ = calculate_riemann_sum(
                    function_str, lower_bound, upper_bound, n, method, variable
                )
                results[method] = riemann_sum
            except Exception as e:
                results[method] = f"Error: {str(e)}"
        
        # Try to calculate exact integral
        try:
            success, expr = safe_sympify(function_str, variable)
            if success:
                var = sp.Symbol(variable, real=True)
                exact = float(sp.integrate(expr, (var, lower_bound, upper_bound)).evalf())
                results['exact'] = exact
                
                # Calculate errors
                for method in methods:
                    if isinstance(results[method], (int, float)):
                        error = abs(results[method] - exact)
                        results[f'{method}_error'] = error
            else:
                results['exact'] = None
                
        except Exception:
            results['exact'] = None
        
        return results
        
    except Exception as e:
        return {"error": str(e)}

def get_optimal_subdivisions(function_str: str, lower_bound: float, upper_bound: float, 
                           target_error: float = 0.001, variable: str = "x") -> Dict[str, int]:
    """
    Estimate optimal number of subdivisions for each method to achieve target error.
    
    Args:
        function_str (str): Function to integrate
        lower_bound (float): Lower bound
        upper_bound (float): Upper bound
        target_error (float): Target error tolerance
        variable (str): Variable name
    
    Returns:
        Dict[str, int]: Optimal subdivisions for each method
    """
    try:
        # Try to calculate exact value first
        success, expr = safe_sympify(function_str, variable)
        if not success:
            return {"error": "Cannot parse function"}
        
        var = sp.Symbol(variable, real=True)
        try:
            exact = float(sp.integrate(expr, (var, lower_bound, upper_bound)).evalf())
        except:
            return {"error": "Cannot compute exact integral"}
        
        optimal_n = {}
        methods = ['left', 'right', 'midpoint']
        
        for method in methods:
            # Start with small n and increase until error is acceptable
            n = 10
            max_n = 10000
            
            while n <= max_n:
                try:
                    riemann_sum, _ = calculate_riemann_sum(
                        function_str, lower_bound, upper_bound, n, method, variable
                    )
                    error = abs(riemann_sum - exact)
                    
                    if error <= target_error:
                        optimal_n[method] = n
                        break
                        
                    n = min(n * 2, max_n)
                    
                except Exception:
                    break
            
            if method not in optimal_n:
                optimal_n[method] = max_n  # If target not reached
        
        return optimal_n
        
    except Exception as e:
        return {"error": str(e)}
