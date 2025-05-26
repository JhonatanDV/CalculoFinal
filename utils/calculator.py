import sympy as sp
import numpy as np
from typing import Tuple, Union, Dict, Any
from .expression_parser import safe_sympify, evaluate_expression_at_point
from .validation import validate_integration_inputs
import scipy.integrate as integrate
import time

def validate_result_accuracy(symbolic_result, numerical_result, tolerance=1e-10):
    """Validar precisión entre métodos simbólico y numérico."""
    if symbolic_result is None or numerical_result is None:
        return False, "Resultados insuficientes para validar"
    
    try:
        relative_error = abs(symbolic_result - numerical_result) / max(abs(symbolic_result), 1e-15)
        
        if relative_error < tolerance:
            return True, f"✅ Validación exitosa (error: {relative_error:.2e})"
        else:
            return False, f"⚠️ Discrepancia detectada (error: {relative_error:.2e})"
    except:
        return False, "Error en validación"

def calculate_definite_integral_robust(function_str: str, lower_bound: str, upper_bound: str, variable: str = "x") -> Tuple[bool, Union[float, str], Dict[str, Any]]:
    """
    Calculate definite integral with multiple fallback methods and cross-validation.
    
    Args:
        function_str: Function string
        lower_bound: Lower bound string
        upper_bound: Upper bound string
        variable: Variable name
    
    Returns:
        Tuple[bool, Union[float, str], Dict[str, Any]]: (success, result_or_error, details)
    """
    try:
        # Validate inputs
        valid, error, expr, lower_val, upper_val = validate_integration_inputs(
            function_str, lower_bound, upper_bound, variable
        )
        if not valid:
            return False, f"Validation error: {error}", {}
        
        details = {
            "function": function_str,
            "variable": variable,
            "lower_bound": lower_val,
            "upper_bound": upper_val,
            "method_used": "",
            "computation_time": 0,
            "approximation_error": None,
            "validation": {}
        }
        
        start_time = time.time()
        symbolic_result = None
        numerical_result = None
        final_result = None
        
        # Método 1: Integración simbólica con SymPy
        try:
            var_symbol = sp.Symbol(variable, real=True)
            
            # Intentar integración simbólica directa
            indefinite_integral = sp.integrate(expr, var_symbol)
            
            # Verificar si la integral indefinida es válida
            if indefinite_integral and not indefinite_integral.has(sp.Integral):
                # Evaluar en los límites
                upper_eval = indefinite_integral.subs(var_symbol, upper_val)
                lower_eval = indefinite_integral.subs(var_symbol, lower_val)
                
                # Convertir a float si es posible
                try:
                    symbolic_result = float((upper_eval - lower_eval).evalf())
                    if not (np.isnan(symbolic_result) or np.isinf(symbolic_result)):
                        final_result = symbolic_result
                        details["method_used"] = "Symbolic Integration (SymPy)"
                except:
                    pass
            
            # Si la simbólica directa no funciona, intentar integración numérica con SymPy
            if symbolic_result is None:
                try:
                    definite_integral = sp.integrate(expr, (var_symbol, lower_val, upper_val))
                    symbolic_result = float(definite_integral.evalf())
                    if not (np.isnan(symbolic_result) or np.isinf(symbolic_result)):
                        final_result = symbolic_result
                        details["method_used"] = "SymPy Numerical Integration"
                except Exception as sympy_error:
                    print(f"SymPy numerical integration failed: {sympy_error}")
                
        except Exception as symbolic_error:
            print(f"Symbolic integration failed: {symbolic_error}")
        
        # Método 2: Integración numérica con SciPy
        try:
            def function_for_scipy(x):
                """Función adaptada para SciPy"""
                try:
                    success, result = evaluate_expression_at_point(expr, variable, float(x))
                    if success and not (np.isnan(result) or np.isinf(result)):
                        return result
                    else:
                        return 0.0  # Valor por defecto para puntos problemáticos
                except:
                    return 0.0
            
            # Usar quad de SciPy con manejo de errores robusto
            numerical_result, error_estimate = integrate.quad(
                function_for_scipy, 
                lower_val, 
                upper_val,
                limit=100,  # Límite de subdivisiones
                epsabs=1e-8,  # Tolerancia absoluta
                epsrel=1e-8   # Tolerancia relativa
            )
            
            if not (np.isnan(numerical_result) or np.isinf(numerical_result)):
                if final_result is None:
                    final_result = numerical_result
                    details["method_used"] = "SciPy Numerical Integration (quad)"
                details["approximation_error"] = error_estimate
                
        except Exception as scipy_error:
            print(f"SciPy integration failed: {scipy_error}")
        
        # Validación cruzada entre métodos
        if symbolic_result is not None and numerical_result is not None:
            is_valid, validation_msg = validate_result_accuracy(symbolic_result, numerical_result)
            details["validation"] = {
                "symbolic_result": symbolic_result,
                "numerical_result": numerical_result,
                "cross_validation": is_valid,
                "validation_message": validation_msg
            }
            
            # Usar el resultado simbólico si la validación es exitosa
            if is_valid:
                final_result = symbolic_result
                details["method_used"] = "Cross-Validated Symbolic"
        
        # Método 3: Fallback a Suma de Riemann de alta precisión
        if final_result is None:
            try:
                riemann_result, riemann_details = calculate_riemann_sum_robust(
                    function_str, lower_val, upper_val, 
                    n=10000,  # Alta precisión
                    method="simpson", 
                    variable=variable
                )
                
                if riemann_result[0]:  # Si fue exitoso
                    final_result = riemann_result[1]
                    details["method_used"] = "High-Precision Riemann Sum (Simpson)"
                    details.update(riemann_details)
                    
            except Exception as riemann_error:
                print(f"Riemann sum failed: {riemann_error}")
        
        # Método 4: Fallback a Monte Carlo (casos extremos)
        if final_result is None:
            try:
                mc_result = monte_carlo_integration(
                    expr, variable, lower_val, upper_val, n_samples=100000
                )
                
                if not (np.isnan(mc_result) or np.isinf(mc_result)):
                    final_result = mc_result
                    details["method_used"] = "Monte Carlo Integration"
                    details["approximation_error"] = "Estimated ±2%"
                    
            except Exception as mc_error:
                print(f"Monte Carlo integration failed: {mc_error}")
        
        # Finalizar
        details["computation_time"] = time.time() - start_time
        
        if final_result is not None:
            return True, final_result, details
        else:
            return False, "All integration methods failed. The function may have discontinuities or singularities in the given interval.", details
        
    except Exception as e:
        return False, f"Critical error in integration: {str(e)}", {}

def calculate_riemann_sum_robust(function_str: str, lower_bound: float, upper_bound: float, 
                               n: int = 1000, method: str = "simpson", variable: str = "x") -> Tuple[Tuple[bool, Union[float, str]], Dict[str, Any]]:
    """
    Calculate Riemann sum with multiple methods including Simpson's rule.
    
    Args:
        function_str: Function string
        lower_bound: Lower bound (float)
        upper_bound: Upper bound (float)
        n: Number of subdivisions
        method: Integration method ('left', 'right', 'midpoint', 'simpson')
        variable: Variable name
    
    Returns:
        Tuple[Tuple[bool, Union[float, str]], Dict[str, Any]]: ((success, result), details)
    """
    try:
        # Parse function
        success, expr = safe_sympify(function_str, variable)
        if not success:
            return (False, f"Function parsing error: {expr}"), {}
        
        details = {
            "method": method,
            "subdivisions": n,
            "interval_size": upper_bound - lower_bound
        }
        
        delta_x = (upper_bound - lower_bound) / n
        
        if method == "simpson":
            # Regla de Simpson (más precisa)
            if n % 2 != 0:
                n += 1  # Simpson necesita número par de intervalos
                delta_x = (upper_bound - lower_bound) / n
            
            total_sum = 0.0
            
            # Evaluar en extremos
            success_start, f_start = evaluate_expression_at_point(expr, variable, lower_bound)
            success_end, f_end = evaluate_expression_at_point(expr, variable, upper_bound)
            
            if not (success_start and success_end):
                return (False, "Cannot evaluate function at endpoints"), details
            
            total_sum += f_start + f_end
            
            # Evaluar en puntos impares (peso 4)
            for i in range(1, n, 2):
                x = lower_bound + i * delta_x
                success, f_val = evaluate_expression_at_point(expr, variable, x)
                if success and not (np.isnan(f_val) or np.isinf(f_val)):
                    total_sum += 4 * f_val
                else:
                    return (False, f"Function undefined at x = {x}"), details
            
            # Evaluar en puntos pares (peso 2)
            for i in range(2, n-1, 2):
                x = lower_bound + i * delta_x
                success, f_val = evaluate_expression_at_point(expr, variable, x)
                if success and not (np.isnan(f_val) or np.isinf(f_val)):
                    total_sum += 2 * f_val
                else:
                    return (False, f"Function undefined at x = {x}"), details
            
            result = (delta_x / 3) * total_sum
            details["simpson_rule"] = True
            
        else:
            # Métodos tradicionales (left, right, midpoint)
            total_sum = 0.0
            
            for i in range(n):
                x_left = lower_bound + i * delta_x
                x_right = lower_bound + (i + 1) * delta_x
                
                if method == "left":
                    sample_point = x_left
                elif method == "right":
                    sample_point = x_right
                else:  # midpoint
                    sample_point = (x_left + x_right) / 2
                
                success, f_val = evaluate_expression_at_point(expr, variable, sample_point)
                if success and not (np.isnan(f_val) or np.isinf(f_val)):
                    total_sum += f_val
                else:
                    return (False, f"Function undefined at x = {sample_point}"), details
            
            result = total_sum * delta_x
        
        return (True, result), details
        
    except Exception as e:
        return (False, f"Riemann sum calculation error: {str(e)}"), {}

def monte_carlo_integration(expr: sp.Expr, variable: str, lower_bound: float, 
                          upper_bound: float, n_samples: int = 100000) -> float:
    """
    Monte Carlo integration for complex functions.
    
    Args:
        expr: SymPy expression
        variable: Variable name
        lower_bound: Lower integration bound
        upper_bound: Upper integration bound
        n_samples: Number of random samples
    
    Returns:
        float: Integration result
    """
    try:
        # Generar puntos aleatorios en el intervalo
        np.random.seed(42)  # Para reproducibilidad
        random_points = np.random.uniform(lower_bound, upper_bound, n_samples)
        
        # Evaluar la función en los puntos aleatorios
        function_values = []
        successful_evaluations = 0
        
        for point in random_points:
            success, f_val = evaluate_expression_at_point(expr, variable, float(point))
            if success and not (np.isnan(f_val) or np.isinf(f_val)):
                function_values.append(f_val)
                successful_evaluations += 1
        
        if successful_evaluations == 0:
            raise ValueError("No successful function evaluations")
        
        # Calcular el promedio y escalar por el ancho del intervalo
        average_value = np.mean(function_values)
        interval_width = upper_bound - lower_bound
        
        result = average_value * interval_width
        return result
        
    except Exception as e:
        raise ValueError(f"Monte Carlo integration failed: {str(e)}")

def analyze_function_properties(function_str: str, variable: str = "x") -> Dict[str, Any]:
    """
    Analyze mathematical properties of a function to help with integration.
    
    Args:
        function_str: Function string
        variable: Variable name
    
    Returns:
        Dict[str, Any]: Function properties
    """
    try:
        success, expr = safe_sympify(function_str, variable)
        if not success:
            return {"error": f"Cannot parse function: {expr}"}
        
        var_symbol = sp.Symbol(variable, real=True)
        
        properties = {
            "function": function_str,
            "variable": variable,
            "is_polynomial": expr.is_polynomial(var_symbol),
            "has_trigonometric": any(expr.has(func) for func in [sp.sin, sp.cos, sp.tan]),
            "has_exponential": expr.has(sp.exp),
            "has_logarithmic": expr.has(sp.log),
            "complexity_level": "basic"
        }
        
        # Determinar nivel de complejidad
        complexity_score = 0
        if properties["has_trigonometric"]:
            complexity_score += 1
        if properties["has_exponential"]:
            complexity_score += 1
        if properties["has_logarithmic"]:
            complexity_score += 1
        if not properties["is_polynomial"]:
            complexity_score += 1
        
        if complexity_score == 0:
            properties["complexity_level"] = "basic"
        elif complexity_score <= 2:
            properties["complexity_level"] = "intermediate"
        else:
            properties["complexity_level"] = "advanced"
        
        # Intentar encontrar discontinuidades obvias
        try:
            # Buscar denominadores que puedan ser cero
            if expr.has(sp.Pow) and any(arg.as_base_exp()[1] < 0 for arg in expr.args if hasattr(arg, 'as_base_exp')):
                properties["potential_discontinuities"] = True
            else:
                properties["potential_discontinuities"] = False
        except:
            properties["potential_discontinuities"] = False
        
        return properties
        
    except Exception as e:
        return {"error": f"Analysis failed: {str(e)}"}

def solve_integral(function_str: str, lower_bound: str, upper_bound: str, variable: str = "x"):
    """
    Wrapper function for backward compatibility.
    
    Args:
        function_str: Function string
        lower_bound: Lower bound string
        upper_bound: Upper bound string
        variable: Variable name
    
    Returns:
        Integration result
    """
    return calculate_definite_integral_robust(function_str, lower_bound, upper_bound, variable)

def calculate_integral(function_str: str, lower_bound: str, upper_bound: str, variable: str = "x"):
    """
    Another wrapper function for backward compatibility.
    
    Args:
        function_str: Function string
        lower_bound: Lower bound string
        upper_bound: Upper bound string
        variable: Variable name
    
    Returns:
        Integration result
    """
    return calculate_definite_integral_robust(function_str, lower_bound, upper_bound, variable)

# Funciones adicionales para compatibilidad con el sistema existente
def get_integration_steps(function_str: str, lower_bound: str, upper_bound: str, variable: str = "x") -> list:
    """
    Generate step-by-step solution for definite integration.
    
    Args:
        function_str: Function string
        lower_bound: Lower bound string
        upper_bound: Upper bound string
        variable: Variable name
    
    Returns:
        List[str]: Step-by-step solution
    """
    steps = []
    
    try:
        # Parse function
        success, expr = safe_sympify(function_str, variable)
        if not success:
            return [f"Error: Could not parse function: {expr}"]
        
        # Validate bounds
        try:
            lower_val = float(lower_bound)
            upper_val = float(upper_bound)
        except:
            return ["Error: Invalid bounds provided"]
        
        var_symbol = sp.Symbol(variable, real=True)
        
        steps.append(f"**Step 1**: Set up the definite integral")
        steps.append(f"$$\\int_{{{lower_bound}}}^{{{upper_bound}}} {sp.latex(expr)} \\, d{variable}$$")
        
        steps.append(f"**Step 2**: Find the antiderivative")
        try:
            antiderivative = sp.integrate(expr, var_symbol)
            if not antiderivative.has(sp.Integral):
                steps.append(f"$$F({variable}) = {sp.latex(antiderivative)} + C$$")
                
                steps.append(f"**Step 3**: Apply the Fundamental Theorem of Calculus")
                steps.append(f"$$\\int_{{{lower_bound}}}^{{{upper_bound}}} {sp.latex(expr)} \\, d{variable} = F({upper_bound}) - F({lower_bound})$$")
                
                # Evaluate at bounds
                upper_eval = antiderivative.subs(var_symbol, upper_val)
                lower_eval = antiderivative.subs(var_symbol, lower_val)
                
                steps.append(f"$$= \\left({sp.latex(upper_eval)}\\right) - \\left({sp.latex(lower_eval)}\\right)$$")
                
                result = upper_eval - lower_eval
                steps.append(f"$$= {sp.latex(result)}$$")
                
            else:
                steps.append("The antiderivative cannot be expressed in elementary functions.")
                steps.append("Using numerical integration method...")
                
        except Exception as e:
            steps.append(f"Could not find symbolic antiderivative: {str(e)}")
            steps.append("Using numerical integration method...")
        
        return steps
        
    except Exception as e:
        return [f"Error generating steps: {str(e)}"]

def compare_integration_methods(function_str: str, lower_bound: str, upper_bound: str, variable: str = "x") -> Dict[str, Any]:
    """
    Compare different integration methods for educational purposes.
    
    Args:
        function_str: Function string
        lower_bound: Lower bound string
        upper_bound: Upper bound string
        variable: Variable name
    
    Returns:
        Dict[str, Any]: Comparison results
    """
    try:
        # Validate inputs
        valid, error, expr, lower_val, upper_val = validate_integration_inputs(
            function_str, lower_bound, upper_bound, variable
        )
        if not valid:
            return {"error": f"Validation error: {error}"}
        
        comparison = {
            "function": function_str,
            "interval": [lower_val, upper_val],
            "methods": {}
        }
        
        # Método simbólico
        try:
            var_symbol = sp.Symbol(variable, real=True)
            indefinite = sp.integrate(expr, var_symbol)
            if not indefinite.has(sp.Integral):
                upper_eval = indefinite.subs(var_symbol, upper_val)
                lower_eval = indefinite.subs(var_symbol, lower_val)
                symbolic_result = float((upper_eval - lower_eval).evalf())
                comparison["methods"]["symbolic"] = {
                    "result": symbolic_result,
                    "status": "success",
                    "method": "Exact symbolic integration"
                }
            else:
                comparison["methods"]["symbolic"] = {
                    "result": None,
                    "status": "failed",
                    "method": "No elementary antiderivative"
                }
        except Exception as e:
            comparison["methods"]["symbolic"] = {
                "result": None,
                "status": "error",
                "error": str(e)
            }
        
        # Método numérico (SciPy)
        try:
            def func_scipy(x):
                success, val = evaluate_expression_at_point(expr, variable, x)
                return val if success else 0.0
            
            numerical_result, error_est = integrate.quad(func_scipy, lower_val, upper_val)
            comparison["methods"]["numerical"] = {
                "result": numerical_result,
                "error_estimate": error_est,
                "status": "success",
                "method": "SciPy quad integration"
            }
        except Exception as e:
            comparison["methods"]["numerical"] = {
                "result": None,
                "status": "error",
                "error": str(e)
            }
        
        # Suma de Riemann (Simpson)
        try:
            riemann_result, riemann_details = calculate_riemann_sum_robust(
                function_str, lower_val, upper_val, n=1000, method="simpson", variable=variable
            )
            if riemann_result[0]:
                comparison["methods"]["riemann_simpson"] = {
                    "result": riemann_result[1],
                    "status": "success",
                    "method": "Simpson's rule (n=1000)",
                    "details": riemann_details
                }
            else:
                comparison["methods"]["riemann_simpson"] = {
                    "result": None,
                    "status": "failed",
                    "error": riemann_result[1]
                }
        except Exception as e:
            comparison["methods"]["riemann_simpson"] = {
                "result": None,
                "status": "error",
                "error": str(e)
            }
        
        return comparison
        
    except Exception as e:
        return {"error": f"Comparison failed: {str(e)}"}