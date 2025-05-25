import numpy as np
import sympy as sp
from typing import Tuple, List
from utils.calculator import safe_sympify, evaluate_expression
from assets.translations import get_text

def calculate_riemann_sum(func_str: str, lower_bound: float, upper_bound: float, 
                         n: int, method: str = "left", variable: str = "x") -> Tuple[float, List[float]]:
    """
    Calculate Riemann sum for a given function.
    
    Args:
        func_str: String representation of the function
        lower_bound: Lower bound of integration
        upper_bound: Upper bound of integration
        n: Number of subdivisions
        method: Method for selecting sample points ('left', 'right', 'midpoint')
        variable: Variable name
    
    Returns:
        Tuple of (riemann_sum, list_of_rectangle_areas)
    """
    try:
        a, b = lower_bound, upper_bound
        delta_x = (b - a) / n
        
        rectangle_areas = []
        total_sum = 0
        
        for i in range(n):
            x_left = a + i * delta_x
            x_right = a + (i + 1) * delta_x
            
            # Determine sample point based on method
            if method == "left":
                x_sample = x_left
            elif method == "right":
                x_sample = x_right
            elif method == "midpoint":
                x_sample = (x_left + x_right) / 2
            else:
                raise ValueError(f"{get_text('invalid_method')}: {method}")
            
            # Evaluate function at sample point with improved error handling
            try:
                # Use direct sympy evaluation to avoid conversion errors
                expr = safe_sympify(func_str, variable)
                var = sp.Symbol(variable)
                result = expr.subs(var, x_sample)
                height = float(result.evalf())
                area = height * delta_x
                rectangle_areas.append(area)
                total_sum += area
            except Exception as e:
                raise ValueError(f"{get_text('error_evaluating_at_point')} {x_sample}: {str(e)}")
        
        return total_sum, rectangle_areas
        
    except Exception as e:
        raise ValueError(f"{get_text('error_calculating_riemann')}: {str(e)}")

def get_riemann_sum_steps(func_str: str, lower_bound: float, upper_bound: float, 
                         n: int, method: str = "left", variable: str = "x") -> List[str]:
    """
    Generate step-by-step solution for Riemann sum calculation.
    """
    try:
        a, b = lower_bound, upper_bound
        delta_x = (b - a) / n
        
        steps = []
        steps.append(f"**{get_text('step')} 1:** {get_text('calculate_delta_x')}")
        steps.append(f"$\\Delta {variable} = \\frac{{b - a}}{{n}} = \\frac{{{b} - {a}}}{{{n}}} = {delta_x}$")
        
        steps.append(f"**{get_text('step')} 2:** {get_text('identify_sample_points')}")
        
        method_text = get_text(f"method_{method}")
        steps.append(f"{get_text('using_method')}: {method_text}")
        
        # Calculate sample points and function values
        sample_points = []
        function_values = []
        
        for i in range(n):
            x_left = a + i * delta_x
            x_right = a + (i + 1) * delta_x
            
            if method == "left":
                x_sample = x_left
            elif method == "right":
                x_sample = x_right
            else:  # midpoint
                x_sample = (x_left + x_right) / 2
            
            sample_points.append(x_sample)
            
            try:
                height = evaluate_expression(func_str, x_sample, variable)
                function_values.append(height)
            except:
                function_values.append(0)
        
        # Show sample points
        sample_points_str = ", ".join([f"{x:.4f}" for x in sample_points])
        steps.append(f"{get_text('sample_points')}: {sample_points_str}")
        
        steps.append(f"**{get_text('step')} 3:** {get_text('evaluate_function')}")
        for i, (x_sample, f_value) in enumerate(zip(sample_points, function_values)):
            steps.append(f"$f({x_sample:.4f}) = {f_value:.4f}$")
        
        steps.append(f"**{get_text('step')} 4:** {get_text('calculate_riemann_formula')}")
        steps.append(f"$R_n = \\Delta {variable} \\sum_{{i=1}}^{{n}} f({variable}_i^*)$")
        
        # Calculate total
        total_sum = sum(function_values) * delta_x
        function_values_str = " + ".join([f"{f:.4f}" for f in function_values])
        steps.append(f"$R_{{{n}}} = {delta_x} \\times ({function_values_str})$")
        steps.append(f"$R_{{{n}}} = {delta_x} \\times {sum(function_values):.4f} = {total_sum:.6f}$")
        
        return steps
        
    except Exception as e:
        return [f"{get_text('error_generating_steps')}: {str(e)}"]

def compare_riemann_methods(func_str: str, lower_bound: float, upper_bound: float, 
                           n: int, variable: str = "x") -> dict:
    """
    Compare different Riemann sum methods for the same function.
    """
    try:
        methods = ["left", "right", "midpoint"]
        results = {}
        
        for method in methods:
            riemann_sum, _ = calculate_riemann_sum(func_str, lower_bound, upper_bound, n, method, variable)
            results[method] = riemann_sum
        
        # Calculate exact integral for comparison if possible
        try:
            expr = safe_sympify(func_str, variable)
            var = sp.Symbol(variable)
            exact_integral = float(sp.integrate(expr, (var, lower_bound, upper_bound)).evalf())
            results["exact"] = exact_integral
            
            # Calculate errors
            for method in methods:
                error = abs(results[method] - exact_integral)
                results[f"{method}_error"] = error
                
        except:
            results["exact"] = None
        
        return results
        
    except Exception as e:
        return {"error": str(e)}

def riemann_sum_convergence(func_str: str, lower_bound: float, upper_bound: float, 
                           max_n: int = 100, method: str = "midpoint", variable: str = "x") -> List[Tuple[int, float]]:
    """
    Calculate Riemann sums for increasing values of n to show convergence.
    """
    try:
        convergence_data = []
        n_values = [2**i for i in range(1, int(np.log2(max_n)) + 1)]
        
        for n in n_values:
            if n > max_n:
                break
            try:
                riemann_sum, _ = calculate_riemann_sum(func_str, lower_bound, upper_bound, n, method, variable)
                convergence_data.append((n, riemann_sum))
            except:
                continue
        
        return convergence_data
        
    except Exception as e:
        return [(0, 0)]
