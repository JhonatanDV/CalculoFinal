import sympy as sp
import numpy as np
from typing import Tuple, List, Union
from assets.translations import get_text

def safe_sympify(expression: str, variable: str = "x") -> sp.Expr:
    """
    Safely convert a string expression to a SymPy expression.
    Simple approach using only working functions.
    """
    try:
        # Replace common notation
        expression = expression.replace("^", "**")
        expression = expression.replace("ln", "log")
        
        # Create symbol
        var = sp.Symbol(variable)
        
        # Parse with basic namespace
        expr = sp.sympify(expression)
        
        return expr
    except Exception as e:
        raise ValueError(f"Error al analizar la expresión: {str(e)}")

def safe_float_conversion(value: Union[str, float, int]) -> float:
    """
    Safely convert a value to float, handling mathematical constants.
    Simple approach using only working functions.
    """
    if isinstance(value, (int, float)):
        return float(value)
    
    try:
        return float(value)
    except ValueError:
        # Handle simple cases only
        if str(value).strip() == "pi":
            return float(sp.pi)
        elif str(value).strip() == "e":
            return float(sp.E)
        else:
            raise ValueError(f"No se puede convertir: {value}")

def evaluate_expression(func_str: str, value: float, variable: str = "x") -> float:
    """
    Evaluate a mathematical expression at a given point.
    Simple approach using only working functions.
    """
    try:
        expr = safe_sympify(func_str, variable)
        var = sp.Symbol(variable)
        result = expr.subs(var, value)
        return float(result.evalf())
    except Exception as e:
        raise ValueError(f"Error al evaluar la expresión: {str(e)}")

def solve_integral(func_str: str, lower_bound: Union[str, float], 
                  upper_bound: Union[str, float], variable: str = "x") -> Tuple[float, List[str]]:
    """
    Solve a definite integral and return the result with step-by-step solution.
    """
    try:
        # Parse the function
        expr = safe_sympify(func_str, variable)
        var = sp.Symbol(variable)
        
        # Convert bounds to float
        a = safe_float_conversion(lower_bound)
        b = safe_float_conversion(upper_bound)
        
        # Calculate the integral
        indefinite_integral = sp.integrate(expr, var)
        definite_integral = sp.integrate(expr, (var, a, b))
        
        # Generate step-by-step solution
        steps = []
        steps.append(f"**{get_text('step')} 1:** {get_text('find_antiderivative')}")
        steps.append(f"$\\int {sp.latex(expr)} \\, d{variable} = {sp.latex(indefinite_integral)} + C$")
        
        steps.append(f"**{get_text('step')} 2:** {get_text('apply_fundamental_theorem')}")
        steps.append(f"$\\int_{{{a}}}^{{{b}}} {sp.latex(expr)} \\, d{variable} = \\left[{sp.latex(indefinite_integral)}\\right]_{{{a}}}^{{{b}}}$")
        
        steps.append(f"**{get_text('step')} 3:** {get_text('evaluate_at_bounds')}")
        
        # Evaluate at upper bound
        upper_value = indefinite_integral.subs(var, b)
        steps.append(f"$F({b}) = {sp.latex(upper_value)}$")
        
        # Evaluate at lower bound
        lower_value = indefinite_integral.subs(var, a)
        steps.append(f"$F({a}) = {sp.latex(lower_value)}$")
        
        steps.append(f"**{get_text('step')} 4:** {get_text('final_calculation')}")
        steps.append(f"$F({b}) - F({a}) = {sp.latex(upper_value)} - ({sp.latex(lower_value)}) = {sp.latex(definite_integral)}$")
        
        result = float(definite_integral.evalf())
        return result, steps
        
    except Exception as e:
        raise ValueError(f"{get_text('error_solving_integral')}: {str(e)}")

def find_derivative(func_str: str, variable: str = "x", order: int = 1) -> Tuple[str, List[str]]:
    """
    Find the derivative of a function and return step-by-step solution.
    """
    try:
        expr = safe_sympify(func_str, variable)
        var = sp.Symbol(variable)
        
        steps = []
        current_expr = expr
        
        for i in range(order):
            steps.append(f"**{get_text('derivative_order')} {i+1}:**")
            derivative = sp.diff(current_expr, var)
            steps.append(f"$\\frac{{d{'d' * i}}}{{d{variable}^{i+1 if i > 0 else ''}}} \\left({sp.latex(current_expr)}\\right) = {sp.latex(derivative)}$")
            current_expr = derivative
        
        return str(current_expr), steps
        
    except Exception as e:
        raise ValueError(f"{get_text('error_finding_derivative')}: {str(e)}")

def solve_equation(equation_str: str, variable: str = "x") -> Tuple[List[float], List[str]]:
    """
    Solve an equation and return solutions with steps.
    """
    try:
        var = sp.Symbol(variable)
        
        # Handle equation format
        if "=" in equation_str:
            left, right = equation_str.split("=")
            expr = safe_sympify(left.strip(), variable) - safe_sympify(right.strip(), variable)
        else:
            expr = safe_sympify(equation_str, variable)
        
        solutions = sp.solve(expr, var)
        
        steps = []
        steps.append(f"**{get_text('equation_to_solve')}:** $f({variable}) = 0$")
        steps.append(f"$f({variable}) = {sp.latex(expr)}$")
        
        if solutions:
            steps.append(f"**{get_text('solutions')}:**")
            for i, sol in enumerate(solutions):
                steps.append(f"${variable}_{i+1} = {sp.latex(sol)}$")
        else:
            steps.append(f"**{get_text('no_real_solutions')}**")
        
        # Convert solutions to float
        numeric_solutions = []
        for sol in solutions:
            try:
                numeric_solutions.append(float(sol.evalf()))
            except:
                # Handle complex solutions
                pass
        
        return numeric_solutions, steps
        
    except Exception as e:
        raise ValueError(f"{get_text('error_solving_equation')}: {str(e)}")
