import numpy as np
import sympy as sp
from typing import Tuple, List, Union
from utils.calculator import safe_sympify, safe_float_conversion, evaluate_expression
from assets.translations import get_text

def find_intersection_points(func1_str: str, func2_str: str, variable: str = "x", 
                           domain: Tuple[float, float] = (-100, 100)) -> List[float]:
    """
    Find intersection points between two functions.
    """
    try:
        # Parse functions
        expr1 = safe_sympify(func1_str, variable)
        expr2 = safe_sympify(func2_str, variable)
        var = sp.Symbol(variable)
        
        # Find intersection by solving f1(x) - f2(x) = 0
        difference = expr1 - expr2
        solutions = sp.solve(difference, var)
        
        # Filter real solutions within domain
        real_solutions = []
        for sol in solutions:
            try:
                numeric_sol = float(sol.evalf())
                if domain[0] <= numeric_sol <= domain[1]:
                    real_solutions.append(numeric_sol)
            except:
                # Skip complex or non-numeric solutions
                continue
        
        return sorted(real_solutions)
        
    except Exception as e:
        raise ValueError(f"{get_text('error_finding_intersections')}: {str(e)}")

def determine_upper_lower_functions(func1_str: str, func2_str: str, 
                                  lower_bound: float, upper_bound: float, 
                                  variable: str = "x") -> Tuple[str, str]:
    """
    Determine which function is upper and which is lower in the given interval.
    """
    try:
        # Sample several points in the interval
        n_samples = 10
        x_samples = np.linspace(lower_bound, upper_bound, n_samples)
        
        func1_higher_count = 0
        func2_higher_count = 0
        
        for x in x_samples:
            try:
                y1 = evaluate_expression(func1_str, x, variable)
                y2 = evaluate_expression(func2_str, x, variable)
                
                if y1 > y2:
                    func1_higher_count += 1
                elif y2 > y1:
                    func2_higher_count += 1
            except:
                continue
        
        if func1_higher_count >= func2_higher_count:
            return func1_str, func2_str  # func1 is upper, func2 is lower
        else:
            return func2_str, func1_str  # func2 is upper, func1 is lower
            
    except Exception as e:
        # Default to original order if determination fails
        return func1_str, func2_str

def calculate_area_between_curves(func1_str: str, func2_str: str, 
                                lower_bound: float, upper_bound: float, 
                                variable: str = "x") -> Tuple[float, List[str]]:
    """
    Calculate the area between two curves.
    """
    try:
        # Parse functions
        expr1 = safe_sympify(func1_str, variable)
        expr2 = safe_sympify(func2_str, variable)
        var = sp.Symbol(variable)
        
        # Find intersections within the interval
        intersections = find_intersection_points(func1_str, func2_str, variable, 
                                               (lower_bound, upper_bound))
        
        # Create integration intervals
        integration_points = [lower_bound] + intersections + [upper_bound]
        integration_points = sorted(list(set(integration_points)))  # Remove duplicates and sort
        
        total_area = 0
        steps = []
        
        steps.append(f"**{get_text('step')} 1:** {get_text('setup_area_calculation')}")
        steps.append(f"{get_text('function1')}: $f_1({variable}) = {sp.latex(expr1)}$")
        steps.append(f"{get_text('function2')}: $f_2({variable}) = {sp.latex(expr2)}$")
        steps.append(f"{get_text('interval')}: $[{lower_bound}, {upper_bound}]$")
        
        if intersections:
            steps.append(f"**{get_text('intersections_found')}:** {intersections}")
            steps.append(f"{get_text('split_intervals')}")
        
        steps.append(f"**{get_text('step')} 2:** {get_text('calculate_area_segments')}")
        
        # Calculate area for each segment
        for i in range(len(integration_points) - 1):
            a = integration_points[i]
            b = integration_points[i + 1]
            
            if abs(b - a) < 1e-10:  # Skip very small intervals
                continue
            
            # Determine which function is upper in this interval
            upper_func, lower_func = determine_upper_lower_functions(
                func1_str, func2_str, a, b, variable
            )
            
            # Parse the upper and lower functions
            upper_expr = safe_sympify(upper_func, variable)
            lower_expr = safe_sympify(lower_func, variable)
            
            # Calculate the area for this segment
            difference_expr = upper_expr - lower_expr
            segment_area = sp.integrate(difference_expr, (var, a, b))
            segment_area_numeric = float(abs(segment_area.evalf()))
            
            total_area += segment_area_numeric
            
            steps.append(f"{get_text('segment')} [{a:.4f}, {b:.4f}]:")
            steps.append(f"$\\text{{{get_text('area')}}} = \\int_{{{a:.4f}}}^{{{b:.4f}}} |{sp.latex(upper_expr)} - ({sp.latex(lower_expr)})| \\, d{variable}$")
            steps.append(f"$= \\int_{{{a:.4f}}}^{{{b:.4f}}} {sp.latex(difference_expr)} \\, d{variable} = {segment_area_numeric:.6f}$")
        
        steps.append(f"**{get_text('step')} 3:** {get_text('total_area')}")
        steps.append(f"$\\text{{{get_text('total_area')}}} = {total_area:.6f}$")
        
        return total_area, steps
        
    except Exception as e:
        raise ValueError(f"{get_text('error_calculating_area')}: {str(e)}")

def calculate_area_with_respect_to_y(func1_str: str, func2_str: str, 
                                    lower_bound: float, upper_bound: float, 
                                    variable: str = "y") -> Tuple[float, List[str]]:
    """
    Calculate area between curves with respect to y-axis.
    """
    try:
        # This would require solving for x in terms of y
        # For now, we'll convert the problem or provide guidance
        steps = []
        steps.append(f"**{get_text('area_wrt_y')}:**")
        steps.append(f"{get_text('solve_for_x_in_terms_of_y')}")
        steps.append(f"$x = g_1({variable})$ {get_text('and')} $x = g_2({variable})$")
        steps.append(f"$\\text{{{get_text('area')}}} = \\int_{{{lower_bound}}}^{{{upper_bound}}} |g_1({variable}) - g_2({variable})| \\, d{variable}$")
        
        # For now, return 0 as this requires more complex inverse function solving
        return 0.0, steps
        
    except Exception as e:
        raise ValueError(f"{get_text('error_calculating_area_y')}: {str(e)}")

def find_centroid_between_curves(func1_str: str, func2_str: str, 
                                lower_bound: float, upper_bound: float, 
                                variable: str = "x") -> Tuple[Tuple[float, float], List[str]]:
    """
    Find the centroid of the region between two curves.
    """
    try:
        # Calculate area first
        area, _ = calculate_area_between_curves(func1_str, func2_str, lower_bound, upper_bound, variable)
        
        if area == 0:
            return (0, 0), [f"{get_text('zero_area_centroid')}"]
        
        # Parse functions
        expr1 = safe_sympify(func1_str, variable)
        expr2 = safe_sympify(func2_str, variable)
        var = sp.Symbol(variable)
        
        # Calculate x-coordinate of centroid
        x_numerator = sp.integrate(var * (expr1 - expr2), (var, lower_bound, upper_bound))
        x_centroid = float(x_numerator.evalf()) / area
        
        # Calculate y-coordinate of centroid
        y_numerator = sp.integrate(0.5 * (expr1**2 - expr2**2), (var, lower_bound, upper_bound))
        y_centroid = float(y_numerator.evalf()) / area
        
        steps = []
        steps.append(f"**{get_text('centroid_calculation')}:**")
        steps.append(f"$\\bar{{x}} = \\frac{{1}}{{A}} \\int_{{{lower_bound}}}^{{{upper_bound}}} x[f_1(x) - f_2(x)] \\, dx = {x_centroid:.6f}$")
        steps.append(f"$\\bar{{y}} = \\frac{{1}}{{2A}} \\int_{{{lower_bound}}}^{{{upper_bound}}} [f_1(x)^2 - f_2(x)^2] \\, dx = {y_centroid:.6f}$")
        steps.append(f"{get_text('centroid')}: $({x_centroid:.6f}, {y_centroid:.6f})$")
        
        return (x_centroid, y_centroid), steps
        
    except Exception as e:
        return (0, 0), [f"{get_text('error_calculating_centroid')}: {str(e)}"]
