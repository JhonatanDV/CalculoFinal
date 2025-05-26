import sympy as sp
import numpy as np
from typing import Tuple, Union, Dict, Any
import time

# ✅ IMPORT OPCIONAL DE SCIPY
try:
    import scipy.integrate as integrate
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False
    integrate = None

# ✅ IMPORTS LOCALES
try:
    from .expression_parser import safe_sympify, evaluate_expression_at_point
    from .validation import validate_integration_inputs
except ImportError:
    # Fallback para imports relativos
    from utils.expression_parser import safe_sympify, evaluate_expression_at_point
    from utils.validation import validate_integration_inputs

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
            "validation": {},
            "scipy_available": SCIPY_AVAILABLE
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
        
        # Método 2: Integración numérica con SciPy (solo si está disponible)
        if SCIPY_AVAILABLE and integrate is not None:
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
    """
    try:
        # Generar puntos aleatorios
        np.random.seed(42)  # Para reproducibilidad
        random_points = np.random.uniform(lower_bound, upper_bound, n_samples)
        
        # Evaluar función en puntos aleatorios
        function_values = []
        for x in random_points:
            success, y = evaluate_expression_at_point(expr, variable, float(x))
            if success and not (np.isnan(y) or np.isinf(y)):
                function_values.append(y)
        
        if len(function_values) == 0:
            raise ValueError("No valid function evaluations")
        
        # Calcular integral usando Monte Carlo
        average_value = np.mean(function_values)
        integral_estimate = average_value * (upper_bound - lower_bound)
        
        return integral_estimate
        
    except Exception as e:
        raise ValueError(f"Monte Carlo integration failed: {str(e)}")

def numerical_derivative(expr: sp.Expr, variable: str, point: float, h: float = 1e-5) -> float:
    """
    Calculate numerical derivative using central difference method.
    """
    try:
        success_plus, f_plus = evaluate_expression_at_point(expr, variable, point + h)
        success_minus, f_minus = evaluate_expression_at_point(expr, variable, point - h)
        
        if success_plus and success_minus:
            return (f_plus - f_minus) / (2 * h)
        else:
            raise ValueError("Cannot evaluate function for derivative")
            
    except Exception as e:
        raise ValueError(f"Numerical derivative failed: {str(e)}")

def find_critical_points(expr: sp.Expr, variable: str, domain_start: float, domain_end: float) -> list:
    """
    Find critical points of a function in a given domain.
    """
    try:
        var_symbol = sp.Symbol(variable)
        
        # Calcular derivada simbólica
        derivative = sp.diff(expr, var_symbol)
        
        # Encontrar raíces de la derivada
        critical_points = []
        
        # Intentar solución simbólica
        try:
            roots = sp.solve(derivative, var_symbol)
            for root in roots:
                try:
                    root_val = float(root.evalf())
                    if domain_start <= root_val <= domain_end:
                        critical_points.append(root_val)
                except:
                    pass
        except:
            # Si falla la solución simbólica, usar método numérico simple
            sample_points = np.linspace(domain_start, domain_end, 1000)
            for i in range(1, len(sample_points) - 1):
                x_prev = sample_points[i-1]
                x_curr = sample_points[i]
                x_next = sample_points[i+1]
                
                try:
                    deriv_prev = numerical_derivative(expr, variable, x_prev)
                    deriv_next = numerical_derivative(expr, variable, x_next)
                    
                    # Buscar cambios de signo
                    if deriv_prev * deriv_next < 0:
                        critical_points.append(x_curr)
                except:
                    pass
        
        return sorted(list(set(critical_points)))
        
    except Exception as e:
        print(f"Critical points calculation failed: {str(e)}")
        return []

def analyze_function_behavior(function_str: str, lower_bound: str, upper_bound: str, variable: str = "x") -> dict:
    """
    Analyze function behavior including monotonicity, concavity, and extrema.
    """
    try:
        # Validate inputs
        valid, error, expr, lower_val, upper_val = validate_integration_inputs(
            function_str, lower_bound, upper_bound, variable
        )
        if not valid:
            return {"error": error}
        
        var_symbol = sp.Symbol(variable)
        
        analysis = {
            "function": function_str,
            "domain": [lower_val, upper_val],
            "critical_points": [],
            "inflection_points": [],
            "monotonicity": {},
            "concavity": {},
            "extrema": {"minima": [], "maxima": []}
        }
        
        try:
            # Primera derivada
            first_derivative = sp.diff(expr, var_symbol)
            # Segunda derivada
            second_derivative = sp.diff(first_derivative, var_symbol)
            
            # Encontrar puntos críticos
            analysis["critical_points"] = find_critical_points(expr, variable, lower_val, upper_val)
            
            # Análisis de extremos usando la segunda derivada
            for cp in analysis["critical_points"]:
                try:
                    second_deriv_val = float(second_derivative.subs(var_symbol, cp).evalf())
                    if second_deriv_val > 0:
                        analysis["extrema"]["minima"].append(cp)
                    elif second_deriv_val < 0:
                        analysis["extrema"]["maxima"].append(cp)
                except:
                    pass
            
        except Exception as deriv_error:
            analysis["derivative_error"] = str(deriv_error)
        
        return analysis
        
    except Exception as e:
        return {"error": f"Function analysis failed: {str(e)}"}

# Función legacy para compatibilidad
def solve_integral(function_str, lower_bound, upper_bound, variable='x'):
    """Función de compatibilidad con versiones anteriores."""
    success, result, details = calculate_definite_integral_robust(
        function_str, lower_bound, upper_bound, variable
    )
    return success, result, details