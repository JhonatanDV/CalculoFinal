import sympy as sp
import numpy as np
from typing import Tuple, List, Union
from .expression_parser import safe_sympify, evaluate_expression_at_point
from .validation import validate_integration_inputs

def solve_integral(function_str: str, lower_bound: str, upper_bound: str, variable: str = "x") -> Tuple[float, List[str]]:
    """
    Solve a definite integral with comprehensive error handling and step-by-step solution.
    
    Args:
        function_str (str): Function to integrate
        lower_bound (str): Lower bound of integration
        upper_bound (str): Upper bound of integration
        variable (str): Integration variable
    
    Returns:
        Tuple[float, List[str]]: (result, step_by_step_solution)
    """
    # Validate inputs
    valid, error, expr, lower_val, upper_val = validate_integration_inputs(
        function_str, lower_bound, upper_bound, variable
    )
    if not valid:
        raise ValueError(error)
    
    steps = []
    var = sp.Symbol(variable, real=True)
    
    try:
        # Step 1: Show the integral to be evaluated
        steps.append(f"**Step 1**: Evaluate the definite integral")
        steps.append(f"$$\\int_{{{lower_val}}}^{{{upper_val}}} {sp.latex(expr)} \\, d{variable}$$")
        
        # Step 2: Find the antiderivative
        steps.append(f"**Step 2**: Find the antiderivative of ${sp.latex(expr)}$")
        
        try:
            antiderivative = sp.integrate(expr, var)
            steps.append(f"$$F({variable}) = {sp.latex(antiderivative)}$$")
        except Exception as e:
            # Try numerical integration if symbolic fails
            steps.append(f"Symbolic integration not possible, using numerical methods.")
            result = float(sp.integrate(expr, (var, lower_val, upper_val)).evalf())
            steps.append(f"**Final Result**: ${result:.6f}$")
            return result, steps
        
        # Step 3: Apply fundamental theorem of calculus
        steps.append(f"**Step 3**: Apply the Fundamental Theorem of Calculus")
        steps.append(f"$$\\int_{{{lower_val}}}^{{{upper_val}}} {sp.latex(expr)} \\, d{variable} = F({upper_val}) - F({lower_val})$$")
        
        # Step 4: Evaluate at bounds
        steps.append(f"**Step 4**: Evaluate at the bounds")
        
        # Evaluate at upper bound
        upper_eval = antiderivative.subs(var, upper_val)
        steps.append(f"$$F({upper_val}) = {sp.latex(upper_eval)}$$")
        
        # Evaluate at lower bound
        lower_eval = antiderivative.subs(var, lower_val)
        steps.append(f"$$F({lower_val}) = {sp.latex(lower_eval)}$$")
        
        # Step 5: Final calculation
        steps.append(f"**Step 5**: Calculate the final result")
        result_expr = upper_eval - lower_eval
        steps.append(f"$$F({upper_val}) - F({lower_val}) = {sp.latex(result_expr)}$$")
        
        # Get numerical result
        result = float(result_expr.evalf())
        steps.append(f"$$= {result:.6f}$$")
        
        return result, steps
        
    except Exception as e:
        # Fallback to numerical integration
        try:
            result = float(sp.integrate(expr, (var, lower_val, upper_val)).evalf())
            steps.append(f"**Numerical Integration Result**: ${result:.6f}$")
            return result, steps
        except Exception as e2:
            raise ValueError(f"Integration failed: {str(e2)}")

def get_function_info(function_str: str, variable: str = "x") -> dict:
    """
    Get information about a mathematical function.
    
    Args:
        function_str (str): Function string
        variable (str): Variable name
    
    Returns:
        dict: Function information including domain, range, etc.
    """
    success, result = safe_sympify(function_str, variable)
    if not success:
        return {"error": result}
    
    expr = result
    var = sp.Symbol(variable, real=True)
    
    info = {
        "expression": expr,
        "latex": sp.latex(expr),
        "free_symbols": [str(s) for s in expr.free_symbols],
        "complexity": "unknown"
    }
    
    try:
        # Try to find derivative
        info["derivative"] = sp.diff(expr, var)
        info["derivative_latex"] = sp.latex(info["derivative"])
    except:
        info["derivative"] = None
    
    try:
        # Try to find critical points
        if info["derivative"] is not None:
            critical_points = sp.solve(info["derivative"], var)
            info["critical_points"] = [float(p.evalf()) for p in critical_points if p.is_real]
        else:
            info["critical_points"] = []
    except:
        info["critical_points"] = []
    
    return info

def check_integration_convergence(function_str: str, lower_bound: str, upper_bound: str, variable: str = "x") -> dict:
    """
    Check if an integral converges and provide convergence information.
    
    Args:
        function_str (str): Function string
        lower_bound (str): Lower bound
        upper_bound (str): Upper bound
        variable (str): Variable name
    
    Returns:
        dict: Convergence information
    """
    valid, error, expr, lower_val, upper_val = validate_integration_inputs(
        function_str, lower_bound, upper_bound, variable
    )
    if not valid:
        return {"error": error}
    
    var = sp.Symbol(variable, real=True)
    
    result = {
        "converges": True,
        "is_improper": False,
        "warnings": []
    }
    
    try:
        # Check for infinite bounds
        if lower_val == float('-inf') or upper_val == float('inf'):
            result["is_improper"] = True
            result["warnings"].append("Improper integral with infinite bounds")
        
        # Check for singularities in the interval
        # This is a simplified check - in practice, this would be more sophisticated
        test_points = np.linspace(lower_val, upper_val, 20)
        for point in test_points:
            success, value = evaluate_expression_at_point(expr, variable, point)
            if not success or abs(value) > 1e10:
                result["warnings"].append(f"Potential singularity near {variable} = {point}")
        
        # Try to evaluate the integral
        integral_result = sp.integrate(expr, (var, lower_val, upper_val))
        if integral_result.has(sp.oo) or integral_result.has(-sp.oo):
            result["converges"] = False
            result["warnings"].append("Integral diverges")
        
    except Exception as e:
        result["warnings"].append(f"Error in convergence analysis: {str(e)}")
    
    return result
