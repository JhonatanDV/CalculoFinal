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
    Validate integration bounds with very flexible limits for engineering applications.
    
    Args:
        lower_bound (str): Lower bound string
        upper_bound (str): Upper bound string
    
    Returns:
        Tuple[bool, str, float, float]: (is_valid, error_message, lower_float, upper_float)
    """
    # Handle special infinity cases
    try:
        if str(lower_bound).lower().strip() in ['-inf', '-infinity', 'negative infinity']:
            lower_val = -1000000.0  # Use very large finite number for engineering
        else:
            success_lower, result_lower = safe_float_conversion(lower_bound)
            if not success_lower:
                return False, f"Invalid lower bound: {result_lower}", None, None
            lower_val = result_lower
    except Exception as e:
        return False, f"Error processing lower bound: {str(e)}", None, None
    
    try:
        if str(upper_bound).lower().strip() in ['inf', 'infinity', 'positive infinity']:
            upper_val = 1000000.0  # Use very large finite number for engineering
        else:
            success_upper, result_upper = safe_float_conversion(upper_bound)
            if not success_upper:
                return False, f"Invalid upper bound: {result_upper}", None, None
            upper_val = result_upper
    except Exception as e:
        return False, f"Error processing upper bound: {str(e)}", None, None
    
    # Check that lower < upper
    if lower_val >= upper_val:
        return False, f"Lower bound ({lower_val}) must be less than upper bound ({upper_val})", None, None
    
    # CORRECCIÓN: Límites mucho más flexibles para aplicaciones de ingeniería
    interval_size = upper_val - lower_val
    
    # Límites progresivos según el tamaño del intervalo
    if interval_size > 100000000:  # 100 millones
        return False, f"Integration interval is extremely large ({interval_size:.0f} units). Maximum allowed: 100,000,000 units", None, None
    elif interval_size > 50000000:  # 50 millones
        # Permitir pero con advertencia fuerte
        try:
            import streamlit as st
            st.error(f"🚨 Extremely large integration interval ({interval_size:.0f} units). This may cause performance issues.")
        except:
            pass
    elif interval_size > 10000000:  # 10 millones
        # Permitir pero con advertencia
        try:
            import streamlit as st
            st.warning(f"⚠️ Very large integration interval ({interval_size:.0f} units). Computation will be slow.")
        except:
            pass
    elif interval_size > 1000000:  # 1 millón
        # Permitir intervalos grandes con advertencia menor
        try:
            import streamlit as st
            st.info(f"ℹ️ Large integration interval ({interval_size:.0f} units). This may take several moments to compute.")
        except:
            pass
    elif interval_size > 100000:  # 100,000
        try:
            import streamlit as st
            st.info(f"ℹ️ Moderate integration interval ({interval_size:.0f} units).")
        except:
            pass
    
    # Límites absolutos muy flexibles para ingeniería
    if abs(lower_val) > 1000000000 or abs(upper_val) > 1000000000:  # 1 billón
        return False, f"Bounds are too large (absolute value >1,000,000,000). Lower: {lower_val:.0f}, Upper: {upper_val:.0f}", None, None
    
    return True, "", lower_val, upper_val

def validate_subdivisions(n: int) -> Tuple[bool, str]:
    """
    Validate number of subdivisions for Riemann sums with more flexible limits.
    
    Args:
        n (int): Number of subdivisions
    
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    if not isinstance(n, int):
        try:
            n = int(n)
        except:
            return False, "Number of subdivisions must be an integer"
    
    if n <= 0:
        return False, "Number of subdivisions must be positive"
    
    # CORRECCIÓN: Límites más flexibles para subdivisiones
    if n > 100000:
        return False, f"Number of subdivisions is too large ({n:,}). Maximum allowed: 100,000"
    elif n > 50000:
        try:
            import streamlit as st
            st.warning(f"⚠️ Very large number of subdivisions ({n:,}). This will take significant time to compute.")
        except:
            pass
    elif n > 10000:
        try:
            import streamlit as st
            st.info(f"ℹ️ Large number of subdivisions ({n:,}). Computation may take a moment.")
        except:
            pass
    elif n > 1000:
        try:
            import streamlit as st
            st.info(f"ℹ️ High number of subdivisions ({n:,}).")
        except:
            pass
    
    return True, ""

def validate_integration_inputs(function_str: str, lower_bound: str, upper_bound: str, variable: str = "x") -> Tuple[bool, str, sp.Expr, float, float]:
    """
    Validate all inputs for integration calculations with improved error handling.
    
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
    
    # CORRECCIÓN: Validación de dominio más flexible
    try:
        domain_valid, domain_error = validate_expression_domain(expr, variable, lower_val, upper_val)
        if not domain_valid:
            # En lugar de fallar completamente, mostrar advertencia y continuar
            try:
                import streamlit as st
                st.warning(f"⚠️ Potential domain issue: {domain_error}")
            except:
                pass
            # Continuar con la validación en lugar de fallar
    except Exception as e:
        # Si la validación del dominio falla, continuar pero advertir
        try:
            import streamlit as st
            st.warning(f"⚠️ Could not fully validate function domain: {str(e)}")
        except:
            pass
    
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
    
    # CORRECCIÓN: Validación de dominio más flexible para ambas funciones
    try:
        domain1_valid, domain1_error = validate_expression_domain(expr1, variable, lower_val, upper_val)
        if not domain1_valid:
            try:
                import streamlit as st
                st.warning(f"⚠️ First function domain issue: {domain1_error}")
            except:
                pass
    except Exception as e:
        try:
            import streamlit as st
            st.warning(f"⚠️ Could not validate first function domain: {str(e)}")
        except:
            pass
    
    try:
        domain2_valid, domain2_error = validate_expression_domain(expr2, variable, lower_val, upper_val)
        if not domain2_valid:
            try:
                import streamlit as st
                st.warning(f"⚠️ Second function domain issue: {domain2_error}")
            except:
                pass
    except Exception as e:
        try:
            import streamlit as st
            st.warning(f"⚠️ Could not validate second function domain: {str(e)}")
        except:
            pass
    
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
                if success and abs(float_val) < 1000000:  # CORRECCIÓN: Rango mucho más amplio
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
                if upper - lower > 0.001:  # CORRECCIÓN: Intervalo mínimo más pequeño
                    suggestions.append((lower, upper))
        
        # CORRECCIÓN: Sugerencias por defecto más variadas y amplias
        if not suggestions:
            suggestions = [
                (-10, 10), (-5, 5), (-2, 2), (0, 10), (-10, 0),
                (-1, 1), (0, 5), (-100, 100), (0, 100), (-50, 50),
                (-1000, 1000), (0, 1000), (-500, 500), (0, 10000), (-1000, 0)
            ]
        
        return suggestions[:10]  # CORRECCIÓN: Retornar más sugerencias
        
    except Exception:
        return [(-10, 10), (-5, 5), (-2, 2), (0, 10), (-1, 1), (-100, 100), (0, 100)]

def validate_engineering_bounds(scenario_type: str, lower_bound: str, upper_bound: str) -> Tuple[bool, str, float, float]:
    """
    Validate bounds specifically for engineering scenarios with very flexible limits.
    
    Args:
        scenario_type (str): Type of engineering scenario
        lower_bound (str): Lower bound string
        upper_bound (str): Upper bound string
    
    Returns:
        Tuple[bool, str, float, float]: (is_valid, error_message, lower_val, upper_val)
    """
    try:
        success_lower, lower_val = safe_float_conversion(lower_bound)
        success_upper, upper_val = safe_float_conversion(upper_bound)
        
        if not success_lower:
            return False, f"Invalid lower bound: {lower_val}", None, None
        if not success_upper:
            return False, f"Invalid upper bound: {upper_val}", None, None
        
        if lower_val >= upper_val:
            return False, "Lower bound must be less than upper bound", None, None
        
        # CORRECCIÓN: Límites mucho más amplios para diferentes escenarios de ingeniería
        scenario_limits = {
            "signal_processing": 1000000000,    # Muy grande para análisis de frecuencia
            "electromagnetic": 500000000,       # Grande para ondas electromagnéticas
            "fluid_dynamics": 100000000,        # Grande para análisis de flujo
            "heat_transfer": 50000000,          # Grande para análisis térmico
            "structural": 10000000,             # Moderado para análisis estructural
            "acoustics": 200000000,             # Grande para análisis acústico
            "vibration": 100000000,             # Grande para análisis de vibraciones
            "control_systems": 50000000,        # Moderado para sistemas de control
            "default": 100000000                # Por defecto muy flexible
        }
        
        max_interval = scenario_limits.get(scenario_type, scenario_limits["default"])
        interval_size = upper_val - lower_val
        
        if interval_size > max_interval:
            # En lugar de fallar, mostrar advertencia y usar límite general
            try:
                import streamlit as st
                st.warning(f"⚠️ Very large interval for {scenario_type} scenario ({interval_size:.0f} units). Using general validation.")
            except:
                pass
            
            # Usar validación general más flexible
            if interval_size > 1000000000:  # 1 billón como límite absoluto
                return False, f"Interval too large even for general engineering ({interval_size:.0f} > 1,000,000,000)", None, None
        
        return True, "", lower_val, upper_val
        
    except Exception as e:
        return False, f"Engineering bounds validation error: {str(e)}", None, None

def validate_extreme_bounds(lower_bound: str, upper_bound: str, allow_extreme: bool = False) -> Tuple[bool, str, float, float]:
    """
    Validate bounds for extreme engineering cases (like signal processing over very long time periods).
    
    Args:
        lower_bound (str): Lower bound string
        upper_bound (str): Upper bound string
        allow_extreme (bool): Whether to allow extremely large intervals
    
    Returns:
        Tuple[bool, str, float, float]: (is_valid, error_message, lower_val, upper_val)
    """
    try:
        success_lower, lower_val = safe_float_conversion(lower_bound)
        success_upper, upper_val = safe_float_conversion(upper_bound)
        
        if not success_lower or not success_upper:
            return False, "Invalid numeric bounds", None, None
        
        if lower_val >= upper_val:
            return False, "Lower bound must be less than upper bound", None, None
        
        interval_size = upper_val - lower_val
        
        if allow_extreme:
            # Para casos extremos, permitir hasta 1 billón
            if interval_size > 1000000000000:  # 1 billón
                return False, f"Interval exceeds extreme limit ({interval_size:.0f} > 1,000,000,000,000)", None, None
            elif interval_size > 100000000:  # 100 millones
                try:
                    import streamlit as st
                    st.warning(f"🔥 Extreme computation ahead: {interval_size:.0f} units. This will take significant time.")
                except:
                    pass
        else:
            # Límites normales más flexibles
            if interval_size > 100000000:
                return False, f"Interval too large for normal computation ({interval_size:.0f} > 100,000,000)", None, None
        
        return True, "", lower_val, upper_val
        
    except Exception as e:
        return False, f"Extreme bounds validation error: {str(e)}", None, None

def validate_plot_bounds(lower_bound: str, upper_bound: str) -> Tuple[bool, str, float, float]:
    """
    Validate bounds specifically for plotting with reduced limits for performance.
    
    Args:
        lower_bound (str): Lower bound string
        upper_bound (str): Upper bound string
    
    Returns:
        Tuple[bool, str, float, float]: (is_valid, error_message, lower_val, upper_val)
    """
    try:
        success_lower, lower_val = safe_float_conversion(lower_bound)
        success_upper, upper_val = safe_float_conversion(upper_bound)
        
        if not success_lower or not success_upper:
            return False, "Invalid numeric bounds for plotting", None, None
        
        if lower_val >= upper_val:
            return False, "Lower bound must be less than upper bound", None, None
        
        interval_size = upper_val - lower_val
        
        # Límites más conservadores para plotting debido a la cantidad de puntos
        if interval_size > 10000000:  # 10 millones para plots
            return False, f"Plotting interval too large ({interval_size:.0f} units). Maximum for plots: 10,000,000", None, None
        elif interval_size > 1000000:  # 1 millón
            try:
                import streamlit as st
                st.warning(f"⚠️ Large plotting interval ({interval_size:.0f} units). Plot generation may be slow.")
            except:
                pass
        elif interval_size > 100000:  # 100,000
            try:
                import streamlit as st
                st.info(f"ℹ️ Moderate plotting interval ({interval_size:.0f} units).")
            except:
                pass
        
        return True, "", lower_val, upper_val
        
    except Exception as e:
        return False, f"Plot bounds validation error: {str(e)}", None, None