import streamlit as st
import plotly.graph_objects as go
import numpy as np
import sympy as sp
from .expression_parser import safe_sympify, evaluate_expression_at_point
from .validation import validate_integration_inputs

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
        
        # Generate x values - CORRECCIÓN: usar array nativo de Python
        x_vals = np.linspace(x_min, x_max, num_points)
        y_vals = []
        
        # Evaluate function at each point
        for i, x in enumerate(x_vals):
            success, y = evaluate_expression_at_point(expr, variable, float(x))
            if success and not (np.isnan(y) or np.isinf(y)):
                y_vals.append(y)
            else:
                y_vals.append(None)  # Use None instead of np.nan for Plotly
        
        # Generate area data
        x_area = np.linspace(lower_val, upper_val, 200)
        y_area = []
        
        for x in x_area:
            success, y = evaluate_expression_at_point(expr, variable, float(x))
            if success and not (np.isnan(y) or np.isinf(y)):
                y_area.append(y)
            else:
                y_area.append(0)
        
        # Create the plot
        fig = go.Figure()
        
        # Plot the function
        fig.add_trace(go.Scatter(
            x=x_vals.tolist(),
            y=y_vals,
            mode='lines',
            name=f'f({variable}) = {function_str}',
            line=dict(color='blue', width=2),
            connectgaps=False
        ))
        
        # Shade the area under the curve
        if len(y_area) > 0:
            fig.add_trace(go.Scatter(
                x=list(x_area) + [upper_val, lower_val],
                y=list(y_area) + [0, 0],
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
        
        # Generate smooth function plot
        x_smooth = np.linspace(x_min, x_max, 1000)
        y_smooth = []
        
        for x in x_smooth:
            success, y = evaluate_expression_at_point(expr, variable, float(x))
            if success and not (np.isnan(y) or np.isinf(y)):
                y_smooth.append(y)
            else:
                y_smooth.append(None)
        
        # Create the plot
        fig = go.Figure()
        
        # Plot the smooth function
        fig.add_trace(go.Scatter(
            x=x_smooth.tolist(),
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