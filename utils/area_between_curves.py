import sympy as sp
import numpy as np
from typing import Tuple, List, Dict, Union
from .expression_parser import safe_sympify, evaluate_expression_at_point, safe_float_conversion
from .validation import validate_two_functions

def find_intersection_points(func1_str: str, func2_str: str, variable: str = "x", 
                           search_range: Tuple[float, float] = (-10, 10)) -> List[float]:
    """
    Find intersection points between two functions.
    
    Args:
        func1_str (str): First function
        func2_str (str): Second function
        variable (str): Variable name
        search_range (Tuple[float, float]): Range to search for intersections
    
    Returns:
        List[float]: List of intersection points
    """
    try:
        # Parse both functions
        success1, expr1 = safe_sympify(func1_str, variable)
        success2, expr2 = safe_sympify(func2_str, variable)
        
        if not success1 or not success2:
            return []
        
        var = sp.Symbol(variable, real=True)
        
        # Solve f1(x) = f2(x)
        equation = sp.Eq(expr1, expr2)
        solutions = sp.solve(equation, var)
        
        # Convert to floats and filter real solutions within range
        intersections = []
        for sol in solutions:
            try:
                success, float_val = safe_float_conversion(sol)
                if success and search_range[0] <= float_val <= search_range[1]:
                    # Verify the intersection by evaluating both functions
                    success1, val1 = evaluate_expression_at_point(expr1, variable, float_val)
                    success2, val2 = evaluate_expression_at_point(expr2, variable, float_val)
                    
                    if success1 and success2 and abs(val1 - val2) < 1e-10:
                        intersections.append(float_val)
            except:
                continue
        
        # Remove duplicates and sort
        intersections = sorted(list(set(intersections)))
        
        return intersections
        
    except Exception:
        return []

def calculate_area_between_curves(func1_str: str, func2_str: str, lower_bound: str, 
                                upper_bound: str, variable: str = "x") -> Tuple[float, List[str]]:
    """
    Calculate area between two curves with step-by-step solution.
    
    Args:
        func1_str (str): First function
        func2_str (str): Second function
        lower_bound (str): Lower bound
        upper_bound (str): Upper bound
        variable (str): Variable name
    
    Returns:
        Tuple[float, List[str]]: (area, step_by_step_solution)
    """
    # Validate inputs
    valid, error, expr1, expr2, lower_val, upper_val = validate_two_functions(
        func1_str, func2_str, lower_bound, upper_bound, variable
    )
    if not valid:
        raise ValueError(error)
    
    steps = []
    var = sp.Symbol(variable, real=True)
    
    try:
        # Step 1: Problem setup
        steps.append(f"**Step 1**: Calculate area between curves")
        steps.append(f"Function 1: $f_1({variable}) = {sp.latex(expr1)}$")
        steps.append(f"Function 2: $f_2({variable}) = {sp.latex(expr2)}$")
        steps.append(f"Interval: $[{lower_val}, {upper_val}]$")
        
        # Step 2: Determine which function is on top
        steps.append(f"**Step 2**: Determine which function is on top")
        
        # Check at midpoint to determine ordering
        midpoint = (lower_val + upper_val) / 2
        success1, val1_mid = evaluate_expression_at_point(expr1, variable, midpoint)
        success2, val2_mid = evaluate_expression_at_point(expr2, variable, midpoint)
        
        if not success1 or not success2:
            raise ValueError("Cannot evaluate functions at midpoint")
        
        # Check if functions cross within the interval
        num_test_points = 10
        test_points = np.linspace(lower_val, upper_val, num_test_points)
        differences = []
        
        for point in test_points:
            success1, val1 = evaluate_expression_at_point(expr1, variable, point)
            success2, val2 = evaluate_expression_at_point(expr2, variable, point)
            if success1 and success2:
                differences.append(val1 - val2)
        
        # Check if sign changes (functions cross)
        sign_changes = sum(1 for i in range(len(differences)-1) 
                          if differences[i] * differences[i+1] < 0)
        
        if sign_changes > 0:
            steps.append("⚠️ Functions intersect within the interval. Computing absolute area.")
            
            # For simplicity, we'll compute |f1 - f2| 
            diff_expr = sp.Abs(expr1 - expr2)
            steps.append(f"Area = $\\int_{{{lower_val}}}^{{{upper_val}}} |f_1({variable}) - f_2({variable})| \\, d{variable}$")
        else:
            # Functions don't cross, determine which is on top
            if val1_mid >= val2_mid:
                diff_expr = expr1 - expr2
                steps.append(f"$f_1({variable}) \\geq f_2({variable})$ on the interval")
                steps.append(f"Area = $\\int_{{{lower_val}}}^{{{upper_val}}} [f_1({variable}) - f_2({variable})] \\, d{variable}$")
            else:
                diff_expr = expr2 - expr1
                steps.append(f"$f_2({variable}) \\geq f_1({variable})$ on the interval")
                steps.append(f"Area = $\\int_{{{lower_val}}}^{{{upper_val}}} [f_2({variable}) - f_1({variable})] \\, d{variable}$")
        
        steps.append(f"$$= \\int_{{{lower_val}}}^{{{upper_val}}} {sp.latex(diff_expr)} \\, d{variable}$$")
        
        # Step 3: Calculate the integral
        steps.append(f"**Step 3**: Evaluate the integral")
        
        try:
            # For absolute value, we need to handle it specially
            if isinstance(diff_expr, sp.Abs):
                # Use numerical integration for absolute value
                integral_result = sp.integrate(diff_expr, (var, lower_val, upper_val))
                area = float(integral_result.evalf())
            else:
                # Regular integration
                antiderivative = sp.integrate(diff_expr, var)
                steps.append(f"Antiderivative: $F({variable}) = {sp.latex(antiderivative)}$")
                
                # Evaluate at bounds
                upper_eval = antiderivative.subs(var, upper_val)
                lower_eval = antiderivative.subs(var, lower_val)
                
                steps.append(f"$F({upper_val}) = {sp.latex(upper_eval)}$")
                steps.append(f"$F({lower_val}) = {sp.latex(lower_eval)}$")
                
                result_expr = upper_eval - lower_eval
                area = float(result_expr.evalf())
                
                # Take absolute value to ensure positive area
                area = abs(area)
            
            steps.append(f"**Final Result**: Area = ${area:.6f}$ square units")
            
        except Exception as e:
            # Fallback to numerical integration
            try:
                integral_result = sp.integrate(sp.Abs(expr1 - expr2), (var, lower_val, upper_val))
                area = float(integral_result.evalf())
                steps.append(f"**Numerical Integration Result**: Area = ${area:.6f}$ square units")
            except Exception as e2:
                raise ValueError(f"Integration failed: {str(e2)}")
        
        return area, steps
        
    except Exception as e:
        raise ValueError(f"Area calculation failed: {str(e)}")

def get_area_steps_with_intersections(func1_str: str, func2_str: str, 
                                    auto_bounds: bool = True, variable: str = "x") -> Dict:
    """
    Get comprehensive information about area between curves including intersections.
    
    Args:
        func1_str (str): First function
        func2_str (str): Second function
        auto_bounds (bool): Whether to find intersection points automatically
        variable (str): Variable name
    
    Returns:
        Dict: Complete analysis including intersections and suggested bounds
    """
    try:
        result = {
            "intersections": [],
            "suggested_intervals": [],
            "function_info": {}
        }
        
        # Parse functions
        success1, expr1 = safe_sympify(func1_str, variable)
        success2, expr2 = safe_sympify(func2_str, variable)
        
        if not success1:
            result["error"] = f"Invalid first function: {expr1}"
            return result
        
        if not success2:
            result["error"] = f"Invalid second function: {expr2}"
            return result
        
        # Store function info
        result["function_info"] = {
            "f1_latex": sp.latex(expr1),
            "f2_latex": sp.latex(expr2),
            "f1_expr": expr1,
            "f2_expr": expr2
        }
        
        if auto_bounds:
            # Find intersection points
            intersections = find_intersection_points(func1_str, func2_str, variable)
            result["intersections"] = intersections
            
            if len(intersections) >= 2:
                # Suggest intervals between consecutive intersections
                for i in range(len(intersections) - 1):
                    lower = intersections[i]
                    upper = intersections[i + 1]
                    if upper - lower > 0.01:  # Minimum interval width
                        result["suggested_intervals"].append((lower, upper))
            
            # Add some default intervals if no intersections found
            if not result["suggested_intervals"]:
                result["suggested_intervals"] = [(-5, 5), (-2, 2), (0, 10)]
        
        return result
        
    except Exception as e:
        return {"error": str(e)}

def compare_area_methods(func1_str: str, func2_str: str, lower_bound: str, 
                        upper_bound: str, variable: str = "x") -> Dict:
    """
    Compare different methods for calculating area between curves.
    
    Args:
        func1_str (str): First function
        func2_str (str): Second function
        lower_bound (str): Lower bound
        upper_bound (str): Upper bound
        variable (str): Variable name
    
    Returns:
        Dict: Comparison of different calculation methods
    """
    try:
        result = {}
        
        # Method 1: Standard area calculation
        try:
            area1, steps1 = calculate_area_between_curves(
                func1_str, func2_str, lower_bound, upper_bound, variable
            )
            result["standard_method"] = {
                "area": area1,
                "steps": len(steps1),
                "success": True
            }
        except Exception as e:
            result["standard_method"] = {
                "area": None,
                "error": str(e),
                "success": False
            }
        
        # Method 2: Numerical integration (Monte Carlo approximation)
        try:
            # Simple numerical approximation using rectangle rule
            valid, error, expr1, expr2, lower_val, upper_val = validate_two_functions(
                func1_str, func2_str, lower_bound, upper_bound, variable
            )
            
            if valid:
                n_points = 1000
                x_points = np.linspace(lower_val, upper_val, n_points)
                dx = (upper_val - lower_val) / n_points
                
                total_area = 0
                for x in x_points:
                    success1, val1 = evaluate_expression_at_point(expr1, variable, x)
                    success2, val2 = evaluate_expression_at_point(expr2, variable, x)
                    if success1 and success2:
                        total_area += abs(val1 - val2) * dx
                
                result["numerical_method"] = {
                    "area": total_area,
                    "points_used": n_points,
                    "success": True
                }
            else:
                result["numerical_method"] = {
                    "area": None,
                    "error": error,
                    "success": False
                }
                
        except Exception as e:
            result["numerical_method"] = {
                "area": None,
                "error": str(e),
                "success": False
            }
        
        return result
        
    except Exception as e:
        return {"error": str(e)}
