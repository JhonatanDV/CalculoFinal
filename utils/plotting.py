import streamlit as st
import plotly.graph_objects as go
import numpy as np
import sympy as sp
from utils.expression_parser import safe_sympify, evaluate_expression_at_point
from utils.validation import validate_integration_inputs

def safe_convert_numpy_to_python(value):
    """
    Convertir valores NumPy a tipos nativos de Python de manera segura.
    """
    try:
        if hasattr(value, 'item'):
            # NumPy array con un elemento
            return value.item()
        elif isinstance(value, (np.floating, np.integer)):
            # Tipos escalares NumPy
            return float(value) if isinstance(value, np.floating) else int(value)
        elif isinstance(value, np.ndarray):
            # Array NumPy, tomar primer elemento
            return float(value.flat[0]) if value.size > 0 else 0.0
        else:
            # Ya es tipo Python nativo
            return float(value)
    except Exception:
        # En caso de error, retornar valor por defecto
        return float(value) if isinstance(value, (int, float)) else 0.0

def plot_integral(function_str: str, lower_bound: str, upper_bound: str, variable: str = "x", num_points: int = 1000):
    """
    Plot a function and highlight the area under the curve for definite integration.
    """
    try:
        # Validate inputs
        valid, error, expr, lower_val, upper_val = validate_integration_inputs(
            function_str, lower_bound, upper_bound, variable
        )
        if not valid:
            st.error(f"Plotting error: {error}")
            return
        
        # Create plotting range
        plot_range = upper_val - lower_val
        extension = max(plot_range * 0.2, 1.0)
        x_min = lower_val - extension
        x_max = upper_val + extension
        
        # Generate x values con conversión segura
        x_vals_numpy = np.linspace(x_min, x_max, num_points)
        x_vals = [safe_convert_numpy_to_python(x) for x in x_vals_numpy]
        y_vals = []
        
        # Evaluate function at each point
        for x in x_vals:
            success, y = evaluate_expression_at_point(expr, variable, x)
            if success and not (np.isnan(y) or np.isinf(y)):
                y_vals.append(y)
            else:
                y_vals.append(None)  # Use None instead of np.nan for Plotly
        
        # Generate area data
        x_area_numpy = np.linspace(lower_val, upper_val, 200)
        x_area = [safe_convert_numpy_to_python(x) for x in x_area_numpy]
        y_area = []
        
        for x in x_area:
            success, y = evaluate_expression_at_point(expr, variable, x)
            if success and not (np.isnan(y) or np.isinf(y)):
                y_area.append(y)
            else:
                y_area.append(0)
        
        # Create the plot
        fig = go.Figure()
        
        # Plot the function
        fig.add_trace(go.Scatter(
            x=x_vals,
            y=y_vals,
            mode='lines',
            name=f'f({variable}) = {function_str}',
            line=dict(color='blue', width=2),
            connectgaps=False
        ))
        
        # Shade the area under the curve
        if len(y_area) > 0:
            fig.add_trace(go.Scatter(
                x=x_area + [upper_val, lower_val],
                y=y_area + [0, 0],
                fill='toself',
                fillcolor='rgba(0, 100, 255, 0.3)',
                line=dict(color='rgba(255,255,255,0)'),
                name='Integration Area',
                hoverinfo='skip'
            ))
        
        # Add vertical lines at bounds
        fig.add_vline(x=lower_val, line_dash="dash", line_color="red", 
                     annotation_text=f"{variable}={lower_val}")
        fig.add_vline(x=upper_val, line_dash="dash", line_color="red", 
                     annotation_text=f"{variable}={upper_val}")
        
        # Customize layout
        fig.update_layout(
            title=f'Definite Integral: ∫[{lower_val}, {upper_val}] {function_str} d{variable}',
            xaxis_title=variable,
            yaxis_title=f'f({variable})',
            showlegend=True,
            hovermode='x unified',
            template='plotly_white',
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error creating plot: {str(e)}")
        
        # Debug info
        with st.expander("🔍 Debug Information"):
            st.code(f"""
Function: {function_str}
Variable: {variable}
Lower bound: {lower_bound}
Upper bound: {upper_bound}
Error: {str(e)}
            """)

def plot_riemann_sum(function_str: str, lower_bound: float, upper_bound: float, 
                    n: int, method: str = "left", variable: str = "x"):
    """Plot Riemann sum rectangles with the function."""
    try:
        # Parse function
        success, expr = safe_sympify(function_str, variable)
        if not success:
            st.error(f"Error parsing function: {expr}")
            return
        
        # Calculate delta x
        delta_x = (upper_bound - lower_bound) / n
        
        # Create plotting range
        plot_range = upper_bound - lower_bound
        extension = max(plot_range * 0.1, 0.5)
        x_min = lower_bound - extension
        x_max = upper_bound + extension
        
        # Generate smooth function plot con conversión segura
        x_smooth_numpy = np.linspace(x_min, x_max, 1000)
        x_smooth = [safe_convert_numpy_to_python(x) for x in x_smooth_numpy]
        y_smooth = []
        
        for x in x_smooth:
            success, y = evaluate_expression_at_point(expr, variable, x)
            if success and not (np.isnan(y) or np.isinf(y)):
                y_smooth.append(y)
            else:
                y_smooth.append(None)
        
        # Create the plot
        fig = go.Figure()
        
        # Plot the smooth function
        fig.add_trace(go.Scatter(
            x=x_smooth,
            y=y_smooth,
            mode='lines',
            name=f'f({variable}) = {function_str}',
            line=dict(color='blue', width=3),
            connectgaps=False
        ))
        
        # Calculate and plot rectangles
        riemann_sum = 0
        for i in range(n):
            x_left = lower_bound + i * delta_x
            x_right = lower_bound + (i + 1) * delta_x
            
            # Determine sample point
            if method == "left":
                sample_point = x_left
            elif method == "right":
                sample_point = x_right
            else:  # midpoint
                sample_point = (x_left + x_right) / 2
            
            # Convertir sample_point a tipo Python nativo
            sample_point = safe_convert_numpy_to_python(sample_point)
            
            # Evaluate function
            success, function_value = evaluate_expression_at_point(expr, variable, sample_point)
            if success and not (np.isnan(function_value) or np.isinf(function_value)):
                riemann_sum += function_value * delta_x
                
                # Draw rectangle
                fig.add_shape(
                    type="rect",
                    x0=x_left, y0=0,
                    x1=x_right, y1=function_value,
                    line=dict(color="red", width=1),
                    fillcolor="rgba(255, 0, 0, 0.3)",
                )
                
                # Add sample point (only show legend for first one)
                fig.add_trace(go.Scatter(
                    x=[sample_point],
                    y=[function_value],
                    mode='markers',
                    name='Sample points' if i == 0 else '',
                    marker=dict(color='red', size=6),
                    showlegend=(i == 0),
                    hovertemplate=f'{variable} = {sample_point:.4f}<br>f({variable}) = {function_value:.4f}<extra></extra>'
                ))
        
        # Add vertical lines at bounds
        fig.add_vline(x=lower_bound, line_dash="dash", line_color="green")
        fig.add_vline(x=upper_bound, line_dash="dash", line_color="green")
        
        # Customize layout
        fig.update_layout(
            title=f'Riemann Sum ({method.title()}): n={n}, Sum ≈ {riemann_sum:.6f}',
            xaxis_title=variable,
            yaxis_title=f'f({variable})',
            showlegend=True,
            hovermode='x unified',
            template='plotly_white',
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error creating Riemann sum plot: {str(e)}")

def plot_area_between_curves(func1_str: str, func2_str: str, lower_bound: str, 
                           upper_bound: str, variable: str = "x", num_points: int = 1000):
    """
    Plot two functions and highlight the area between them.
    """
    try:
        # Parse both functions
        success1, expr1 = safe_sympify(func1_str, variable)
        success2, expr2 = safe_sympify(func2_str, variable)
        
        if not success1:
            st.error(f"Error parsing first function: {expr1}")
            return
        if not success2:
            st.error(f"Error parsing second function: {expr2}")
            return
        
        # Parse bounds
        try:
            lower_val = float(lower_bound)
            upper_val = float(upper_bound)
        except ValueError:
            st.error("Invalid bounds - must be numeric values")
            return
        
        # Create plotting range
        plot_range = upper_val - lower_val
        extension = max(plot_range * 0.2, 1.0)
        x_min = lower_val - extension
        x_max = upper_val + extension
        
        # Generate x values con conversión segura
        x_vals_numpy = np.linspace(x_min, x_max, num_points)
        x_vals = [safe_convert_numpy_to_python(x) for x in x_vals_numpy]
        y1_vals = []
        y2_vals = []
        
        # Evaluate both functions
        for x in x_vals:
            success1, y1 = evaluate_expression_at_point(expr1, variable, x)
            success2, y2 = evaluate_expression_at_point(expr2, variable, x)
            
            y1_vals.append(y1 if success1 and not (np.isnan(y1) or np.isinf(y1)) else None)
            y2_vals.append(y2 if success2 and not (np.isnan(y2) or np.isinf(y2)) else None)
        
        # Generate values for shaded area (between bounds only)
        x_area_numpy = np.linspace(lower_val, upper_val, 200)
        x_area = [safe_convert_numpy_to_python(x) for x in x_area_numpy]
        y1_area = []
        y2_area = []
        
        for x in x_area:
            success1, y1 = evaluate_expression_at_point(expr1, variable, x)
            success2, y2 = evaluate_expression_at_point(expr2, variable, x)
            
            y1_area.append(y1 if success1 and not (np.isnan(y1) or np.isinf(y1)) else 0)
            y2_area.append(y2 if success2 and not (np.isnan(y2) or np.isinf(y2)) else 0)
        
        # Create the plot
        fig = go.Figure()
        
        # Plot first function
        fig.add_trace(go.Scatter(
            x=x_vals,
            y=y1_vals,
            mode='lines',
            name=f'f₁({variable}) = {func1_str}',
            line=dict(color='blue', width=2),
            connectgaps=False
        ))
        
        # Plot second function
        fig.add_trace(go.Scatter(
            x=x_vals,
            y=y2_vals,
            mode='lines',
            name=f'f₂({variable}) = {func2_str}',
            line=dict(color='red', width=2),
            connectgaps=False
        ))
        
        # Shade the area between curves
        if len(y1_area) > 0 and len(y2_area) > 0:
            fig.add_trace(go.Scatter(
                x=x_area,
                y=y1_area,
                mode='lines',
                line=dict(width=0),
                showlegend=False,
                hoverinfo='skip'
            ))
            
            fig.add_trace(go.Scatter(
                x=x_area,
                y=y2_area,
                mode='lines',
                line=dict(width=0),
                fill='tonexty',
                fillcolor='rgba(100, 255, 100, 0.3)',
                name='Area Between Curves',
                hoverinfo='skip'
            ))
        
        # Add vertical lines at bounds
        fig.add_vline(x=lower_val, line_dash="dash", line_color="green", 
                     annotation_text=f"{variable}={lower_val}")
        fig.add_vline(x=upper_val, line_dash="dash", line_color="green", 
                     annotation_text=f"{variable}={upper_val}")
        
        # Customize layout
        fig.update_layout(
            title=f'Area Between Curves: [{lower_val}, {upper_val}]',
            xaxis_title=variable,
            yaxis_title=f'f({variable})',
            showlegend=True,
            hovermode='x unified',
            template='plotly_white',
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error creating area plot: {str(e)}")

def create_comparison_plot(function_str: str, lower_bound: str, upper_bound: str, 
                         variable: str = "x", methods: list = None):
    """
    Create a comparison plot showing different integration methods.
    """
    if methods is None:
        methods = ["symbolic", "riemann_left", "riemann_right", "riemann_midpoint"]
    
    try:
        # Validate inputs
        valid, error, expr, lower_val, upper_val = validate_integration_inputs(
            function_str, lower_bound, upper_bound, variable
        )
        if not valid:
            st.error(f"Comparison plot error: {error}")
            return
        
        # Create subplots for comparison
        from plotly.subplots import make_subplots
        
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Original Function', 'Left Riemann', 'Right Riemann', 'Midpoint Riemann'),
            vertical_spacing=0.12,
            horizontal_spacing=0.1
        )
        
        # Generate x values
        x_vals_numpy = np.linspace(lower_val, upper_val, 200)
        x_vals = [safe_convert_numpy_to_python(x) for x in x_vals_numpy]
        y_vals = []
        
        for x in x_vals:
            success, y = evaluate_expression_at_point(expr, variable, x)
            if success and not (np.isnan(y) or np.isinf(y)):
                y_vals.append(y)
            else:
                y_vals.append(0)
        
        # Plot original function in all subplots
        for row in range(1, 3):
            for col in range(1, 3):
                fig.add_trace(
                    go.Scatter(x=x_vals, y=y_vals, mode='lines', 
                             name=f'f({variable})' if row == 1 and col == 1 else '',
                             line=dict(color='blue', width=2),
                             showlegend=(row == 1 and col == 1)),
                    row=row, col=col
                )
        
        # Add area under curve to first subplot
        fig.add_trace(
            go.Scatter(
                x=x_vals + [upper_val, lower_val],
                y=y_vals + [0, 0],
                fill='toself',
                fillcolor='rgba(0, 100, 255, 0.3)',
                line=dict(color='rgba(255,255,255,0)'),
                name='Integration Area',
                showlegend=True
            ),
            row=1, col=1
        )
        
        # Add Riemann rectangles to other subplots
        n = 20  # Number of rectangles
        delta_x = (upper_val - lower_val) / n
        
        methods_positions = [(1, 2, "left"), (2, 1, "right"), (2, 2, "midpoint")]
        
        for row, col, method in methods_positions:
            for i in range(n):
                x_left = lower_val + i * delta_x
                x_right = lower_val + (i + 1) * delta_x
                
                if method == "left":
                    sample_point = x_left
                elif method == "right":
                    sample_point = x_right
                else:  # midpoint
                    sample_point = (x_left + x_right) / 2
                
                success, function_value = evaluate_expression_at_point(expr, variable, sample_point)
                if success and not (np.isnan(function_value) or np.isinf(function_value)):
                    fig.add_shape(
                        type="rect",
                        x0=x_left, y0=0,
                        x1=x_right, y1=function_value,
                        line=dict(color="red", width=1),
                        fillcolor="rgba(255, 0, 0, 0.3)",
                        row=row, col=col
                    )
        
        fig.update_layout(
            title=f'Integration Methods Comparison: f({variable}) = {function_str}',
            height=600,
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error creating comparison plot: {str(e)}")

def plot_volume_3d(function_str: str, lower_bound: str, upper_bound: str, variable: str = "x"):
    """Visualizar sólido de revolución en 3D."""
    try:
        # Validar inputs
        valid, error, expr, lower_val, upper_val = validate_integration_inputs(
            function_str, lower_bound, upper_bound, variable
        )
        if not valid:
            st.error(f"Error en visualización 3D: {error}")
            return
        
        # Generar datos para revolución
        t_vals = np.linspace(lower_val, upper_val, 100)
        r_vals = []
        
        for t in t_vals:
            success, r = evaluate_expression_at_point(expr, variable, t)
            if success and not (np.isnan(r) or np.isinf(r)) and r >= 0:
                r_vals.append(abs(r))  # Radio debe ser positivo
            else:
                r_vals.append(0.1)  # Valor mínimo para evitar errores
        
        # Crear superficie de revolución
        theta = np.linspace(0, 2*np.pi, 50)
        T, THETA = np.meshgrid(t_vals, theta)
        R = np.array([r_vals] * len(theta))
        
        # Coordenadas cartesianas
        X = R * np.cos(THETA)
        Y = R * np.sin(THETA) 
        Z = T
        
        # Crear figura 3D
        fig = go.Figure(data=[
            go.Surface(
                x=X, y=Y, z=Z,
                colorscale='Viridis',
                opacity=0.8,
                name='Sólido de Revolución'
            )
        ])
        
        # Agregar curva original
        fig.add_trace(go.Scatter3d(
            x=r_vals, y=[0]*len(r_vals), z=t_vals,
            mode='lines',
            line=dict(color='red', width=8),
            name=f'f({variable}) = {function_str}'
        ))
        
        # Configurar layout
        fig.update_layout(
            title=f'🔄 Sólido de Revolución: f({variable}) = {function_str}',
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y', 
                zaxis_title=variable,
                camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
            ),
            width=800,
            height=600
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Información adicional
        st.info(f"""
        **🎯 Interpretación 3D:**
        - **Eje de revolución:** {variable} (vertical)
        - **Radio:** f({variable}) = {function_str}
        - **Intervalo:** [{lower_val}, {upper_val}]
        - **Vista:** Sólido generado al rotar la curva alrededor del eje {variable}
        """)
        
    except Exception as e:
        st.error(f"Error en visualización 3D: {str(e)}")
        # Fallback a visualización 2D
        plot_integral(function_str, lower_bound, upper_bound, variable)

def plot_3d_comparison(function_str: str, lower_bound: str, upper_bound: str, variable: str = "x"):
    """Comparar función 2D vs sólido 3D."""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📈 Función Original (2D)")
        plot_integral(function_str, lower_bound, upper_bound, variable)
    
    with col2:
        st.markdown("#### 🔄 Sólido de Revolución (3D)")
        plot_volume_3d(function_str, lower_bound, upper_bound, variable)

def plot_interactive_slider(function_str: str, variable: str = "x"):
    """
    Create an interactive plot with sliders for bounds.
    """
    try:
        # Parse function
        success, expr = safe_sympify(function_str, variable)
        if not success:
            st.error(f"Error parsing function: {expr}")
            return
        
        # Create sliders for bounds
        col1, col2 = st.columns(2)
        with col1:
            lower_val = st.slider("Lower bound", -10.0, 10.0, 0.0, 0.1, key="interactive_lower")
        with col2:
            upper_val = st.slider("Upper bound", -10.0, 10.0, 5.0, 0.1, key="interactive_upper")
        
        if lower_val >= upper_val:
            st.warning("Lower bound must be less than upper bound")
            return
        
        # Plot with current bounds
        plot_integral(function_str, str(lower_val), str(upper_val), variable)
        
        # Calculate and display integral
        from utils.calculator import calculate_definite_integral_robust
        success, result, details = calculate_definite_integral_robust(
            function_str, str(lower_val), str(upper_val), variable
        )
        
        if success:
            st.metric("Integral Value", f"{result:.6f}")
        else:
            st.error(f"Integration error: {result}")
        
    except Exception as e:
        st.error(f"Error creating interactive plot: {str(e)}")

def export_plot_data(function_str: str, lower_bound: str, upper_bound: str, variable: str = "x"):
    """
    Export plot data for external use.
    """
    try:
        # Validate inputs
        valid, error, expr, lower_val, upper_val = validate_integration_inputs(
            function_str, lower_bound, upper_bound, variable
        )
        if not valid:
            st.error(f"Export error: {error}")
            return None
        
        # Generate data points
        num_points = 1000
        x_vals_numpy = np.linspace(lower_val, upper_val, num_points)
        x_vals = [safe_convert_numpy_to_python(x) for x in x_vals_numpy]
        y_vals = []
        
        for x in x_vals:
            success, y = evaluate_expression_at_point(expr, variable, x)
            if success and not (np.isnan(y) or np.isinf(y)):
                y_vals.append(y)
            else:
                y_vals.append(None)
        
        # Create DataFrame
        import pandas as pd
        df = pd.DataFrame({
            variable: x_vals,
            f'f({variable})': y_vals
        })
        
        return df
        
    except Exception as e:
        st.error(f"Error exporting data: {str(e)}")
        return None