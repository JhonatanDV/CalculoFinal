import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import sympy as sp
from plotly.subplots import make_subplots
from .expression_parser import safe_sympify, evaluate_expression_at_point
from .validation import validate_integration_inputs, validate_two_functions

def plot_integral(function_str: str, lower_bound: str, upper_bound: str, variable: str = "x", num_points: int = 1000):
    """
    Plot a function and highlight the area under the curve for definite integration.
    
    Args:
        function_str (str): Function to plot
        lower_bound (str): Lower bound of integration
        upper_bound (str): Upper bound of integration
        variable (str): Variable name
        num_points (int): Number of points for plotting
    """
    try:
        # Validate inputs
        valid, error, expr, lower_val, upper_val = validate_integration_inputs(
            function_str, lower_bound, upper_bound, variable
        )
        if not valid:
            st.error(f"Plotting error: {error}")
            return
        
        # Create plotting range (extend beyond bounds for context)
        plot_range = upper_val - lower_val
        extension = max(plot_range * 0.2, 1.0)
        x_min = lower_val - extension
        x_max = upper_val + extension
        
        # Generate x values for the full function
        x_vals = np.linspace(x_min, x_max, num_points)
        y_vals = []
        
        # Evaluate function at each point
        for x in x_vals:
            success, y = evaluate_expression_at_point(expr, variable, x)
            if success:
                y_vals.append(y)
            else:
                y_vals.append(np.nan)
        
        # Generate x values for the shaded area (integration region)
        x_area = np.linspace(lower_val, upper_val, max(100, num_points // 10))
        y_area = []
        
        for x in x_area:
            success, y = evaluate_expression_at_point(expr, variable, x)
            if success:
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
            line=dict(color='blue', width=2)
        ))
        
        # Shade the area under the curve
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
        y_range = [min(y_vals) if y_vals else -1, max(y_vals) if y_vals else 1]
        y_extension = (y_range[1] - y_range[0]) * 0.1
        
        fig.add_shape(
            type="line",
            x0=lower_val, y0=y_range[0] - y_extension,
            x1=lower_val, y1=y_range[1] + y_extension,
            line=dict(color="red", width=2, dash="dash"),
        )
        
        fig.add_shape(
            type="line",
            x0=upper_val, y0=y_range[0] - y_extension,
            x1=upper_val, y1=y_range[1] + y_extension,
            line=dict(color="red", width=2, dash="dash"),
        )
        
        # Add bound labels
        fig.add_annotation(
            x=lower_val, y=y_range[0] - y_extension,
            text=f"{variable} = {lower_val}",
            showarrow=True,
            arrowhead=2,
            arrowcolor="red"
        )
        
        fig.add_annotation(
            x=upper_val, y=y_range[0] - y_extension,
            text=f"{variable} = {upper_val}",
            showarrow=True,
            arrowhead=2,
            arrowcolor="red"
        )
        
        # Customize layout
        fig.update_layout(
            title=f'Definite Integral: ∫[{lower_val}, {upper_val}] {function_str} d{variable}',
            xaxis_title=variable,
            yaxis_title=f'f({variable})',
            showlegend=True,
            hovermode='x unified',
            template='plotly_white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error creating plot: {str(e)}")

def plot_riemann_sum(function_str: str, lower_bound: float, upper_bound: float, 
                    n: int, method: str = "left", variable: str = "x"):
    """
    Plot Riemann sum rectangles with the function.
    
    Args:
        function_str (str): Function to plot
        lower_bound (float): Lower bound
        upper_bound (float): Upper bound
        n (int): Number of subdivisions
        method (str): Method ('left', 'right', 'midpoint')
        variable (str): Variable name
    """
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
        
        # Generate x values for smooth function plot
        x_smooth = np.linspace(x_min, x_max, 1000)
        y_smooth = []
        
        for x in x_smooth:
            success, y = evaluate_expression_at_point(expr, variable, x)
            if success:
                y_smooth.append(y)
            else:
                y_smooth.append(np.nan)
        
        # Create the plot
        fig = go.Figure()
        
        # Plot the smooth function
        fig.add_trace(go.Scatter(
            x=x_smooth,
            y=y_smooth,
            mode='lines',
            name=f'f({variable}) = {function_str}',
            line=dict(color='blue', width=3)
        ))
        
        # Calculate and plot rectangles
        sample_points = []
        function_values = []
        
        for i in range(n):
            x_left = lower_bound + i * delta_x
            x_right = lower_bound + (i + 1) * delta_x
            
            # Determine sample point based on method
            if method == "left":
                sample_point = x_left
            elif method == "right":
                sample_point = x_right
            elif method == "midpoint":
                sample_point = (x_left + x_right) / 2
            
            sample_points.append(sample_point)
            
            # Evaluate function at sample point
            success, function_value = evaluate_expression_at_point(expr, variable, sample_point)
            if success:
                function_values.append(function_value)
                
                # Draw rectangle
                fig.add_shape(
                    type="rect",
                    x0=x_left, y0=0,
                    x1=x_right, y1=function_value,
                    line=dict(color="red", width=1),
                    fillcolor="rgba(255, 0, 0, 0.3)",
                )
                
                # Add sample point
                fig.add_trace(go.Scatter(
                    x=[sample_point],
                    y=[function_value],
                    mode='markers',
                    name=f'Sample point {i+1}' if i == 0 else '',
                    marker=dict(color='red', size=8),
                    showlegend=(i == 0),
                    hovertemplate=f'{variable} = {sample_point:.4f}<br>f({variable}) = {function_value:.4f}<extra></extra>'
                ))
            else:
                function_values.append(0)
        
        # Add vertical lines at bounds
        y_range = [min(y_smooth) if y_smooth else -1, max(y_smooth) if y_smooth else 1]
        
        fig.add_shape(
            type="line",
            x0=lower_bound, y0=0,
            x1=lower_bound, y1=y_range[1],
            line=dict(color="green", width=2, dash="dash"),
        )
        
        fig.add_shape(
            type="line",
            x0=upper_bound, y0=0,
            x1=upper_bound, y1=y_range[1],
            line=dict(color="green", width=2, dash="dash"),
        )
        
        # Calculate Riemann sum
        riemann_sum = sum(val * delta_x for val in function_values)
        
        # Customize layout
        fig.update_layout(
            title=f'Riemann Sum ({method.title()} Method): n = {n}, R_n = {riemann_sum:.6f}',
            xaxis_title=variable,
            yaxis_title=f'f({variable})',
            showlegend=True,
            hovermode='x unified',
            template='plotly_white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error creating Riemann sum plot: {str(e)}")

def plot_area_between_curves(func1_str: str, func2_str: str, lower_bound: str, 
                           upper_bound: str, variable: str = "x", num_points: int = 1000):
    """
    Plot two functions and highlight the area between them.
    
    Args:
        func1_str (str): First function
        func2_str (str): Second function
        lower_bound (str): Lower bound
        upper_bound (str): Upper bound
        variable (str): Variable name
        num_points (int): Number of points for plotting
    """
    try:
        # Validate inputs
        valid, error, expr1, expr2, lower_val, upper_val = validate_two_functions(
            func1_str, func2_str, lower_bound, upper_bound, variable
        )
        if not valid:
            st.error(f"Plotting error: {error}")
            return
        
        # Create plotting range
        plot_range = upper_val - lower_val
        extension = max(plot_range * 0.2, 1.0)
        x_min = lower_val - extension
        x_max = upper_val + extension
        
        # Generate x values
        x_vals = np.linspace(x_min, x_max, num_points)
        y1_vals = []
        y2_vals = []
        
        # Evaluate both functions
        for x in x_vals:
            success1, y1 = evaluate_expression_at_point(expr1, variable, x)
            success2, y2 = evaluate_expression_at_point(expr2, variable, x)
            
            y1_vals.append(y1 if success1 else np.nan)
            y2_vals.append(y2 if success2 else np.nan)
        
        # Generate values for shaded area (between bounds only)
        x_area = np.linspace(lower_val, upper_val, max(100, num_points // 10))
        y1_area = []
        y2_area = []
        
        for x in x_area:
            success1, y1 = evaluate_expression_at_point(expr1, variable, x)
            success2, y2 = evaluate_expression_at_point(expr2, variable, x)
            
            y1_area.append(y1 if success1 else 0)
            y2_area.append(y2 if success2 else 0)
        
        # Create the plot
        fig = go.Figure()
        
        # Plot first function
        fig.add_trace(go.Scatter(
            x=x_vals,
            y=y1_vals,
            mode='lines',
            name=f'f₁({variable}) = {func1_str}',
            line=dict(color='blue', width=2)
        ))
        
        # Plot second function
        fig.add_trace(go.Scatter(
            x=x_vals,
            y=y2_vals,
            mode='lines',
            name=f'f₂({variable}) = {func2_str}',
            line=dict(color='red', width=2)
        ))
        
        # Shade the area between curves
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
        y_range = [min(min(y1_vals), min(y2_vals)), max(max(y1_vals), max(y2_vals))]
        y_extension = (y_range[1] - y_range[0]) * 0.1
        
        fig.add_shape(
            type="line",
            x0=lower_val, y0=y_range[0] - y_extension,
            x1=lower_val, y1=y_range[1] + y_extension,
            line=dict(color="green", width=2, dash="dash"),
        )
        
        fig.add_shape(
            type="line",
            x0=upper_val, y0=y_range[0] - y_extension,
            x1=upper_val, y1=y_range[1] + y_extension,
            line=dict(color="green", width=2, dash="dash"),
        )
        
        # Add bound labels
        fig.add_annotation(
            x=lower_val, y=y_range[0] - y_extension,
            text=f"{variable} = {lower_val}",
            showarrow=True,
            arrowhead=2,
            arrowcolor="green"
        )
        
        fig.add_annotation(
            x=upper_val, y=y_range[0] - y_extension,
            text=f"{variable} = {upper_val}",
            showarrow=True,
            arrowhead=2,
            arrowcolor="green"
        )
        
        # Customize layout
        fig.update_layout(
            title=f'Area Between Curves on [{lower_val}, {upper_val}]',
            xaxis_title=variable,
            yaxis_title=f'f({variable})',
            showlegend=True,
            hovermode='x unified',
            template='plotly_white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error creating area plot: {str(e)}")

def plot_function_comparison(functions: list, labels: list, x_range: tuple = (-10, 10), variable: str = "x"):
    """
    Plot multiple functions for comparison.
    
    Args:
        functions (list): List of function strings
        labels (list): List of labels for the functions
        x_range (tuple): Range for x-axis
        variable (str): Variable name
    """
    try:
        fig = go.Figure()
        colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']
        
        x_vals = np.linspace(x_range[0], x_range[1], 1000)
        
        for i, (func_str, label) in enumerate(zip(functions, labels)):
            success, expr = safe_sympify(func_str, variable)
            if success:
                y_vals = []
                for x in x_vals:
                    success_eval, y = evaluate_expression_at_point(expr, variable, x)
                    y_vals.append(y if success_eval else np.nan)
                
                fig.add_trace(go.Scatter(
                    x=x_vals,
                    y=y_vals,
                    mode='lines',
                    name=label,
                    line=dict(color=colors[i % len(colors)], width=2)
                ))
        
        fig.update_layout(
            title='Function Comparison',
            xaxis_title=variable,
            yaxis_title=f'f({variable})',
            showlegend=True,
            hovermode='x unified',
            template='plotly_white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error creating comparison plot: {str(e)}")
