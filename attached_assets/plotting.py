import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import sympy as sp
from utils.calculator import safe_sympify, safe_float_conversion, evaluate_expression
from assets.translations import get_text

def create_function_data(func_str: str, x_min: float, x_max: float, 
                        variable: str = "x", num_points: int = 1000):
    """
    Create x and y data for plotting a function.
    """
    try:
        x_data = np.linspace(x_min, x_max, num_points)
        y_data = []
        
        for x_val in x_data:
            try:
                y_val = evaluate_expression(func_str, x_val, variable)
                y_data.append(y_val)
            except:
                y_data.append(np.nan)
        
        return x_data, np.array(y_data)
    except Exception as e:
        st.error(f"{get_text('error_creating_plot_data')}: {str(e)}")
        return np.array([]), np.array([])

def plot_function(func_str: str, x_min: float = -10, x_max: float = 10, 
                 variable: str = "x", title: str = None):
    """
    Plot a mathematical function using Plotly.
    """
    try:
        # Create data
        x_data, y_data = create_function_data(func_str, x_min, x_max, variable)
        
        if len(x_data) == 0:
            return
        
        # Create the plot
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=x_data,
            y=y_data,
            mode='lines',
            name=f'f({variable}) = {func_str}',
            line=dict(color='blue', width=2)
        ))
        
        # Update layout
        plot_title = title or f"{get_text('graph_of')} f({variable}) = {func_str}"
        fig.update_layout(
            title=plot_title,
            xaxis_title=variable,
            yaxis_title=f'f({variable})',
            showlegend=True,
            hovermode='x unified',
            template='plotly_white'
        )
        
        # Add grid
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"{get_text('error_plotting_function')}: {str(e)}")

def plot_integral(func_str: str, lower_bound: str, upper_bound: str, 
                 variable: str = "x", title: str = None):
    """
    Plot a function with shaded area representing the definite integral.
    """
    try:
        # Convert bounds
        a = safe_float_conversion(lower_bound)
        b = safe_float_conversion(upper_bound)
        
        # Extend range for better visualization
        x_min = min(a - 2, -10)
        x_max = max(b + 2, 10)
        
        # Create function data
        x_data, y_data = create_function_data(func_str, x_min, x_max, variable)
        
        if len(x_data) == 0:
            return
        
        # Create data for shaded area
        x_fill = np.linspace(a, b, 200)
        y_fill = []
        for x_val in x_fill:
            try:
                y_val = evaluate_expression(func_str, x_val, variable)
                y_fill.append(y_val)
            except:
                y_fill.append(0)
        
        # Create the plot
        fig = go.Figure()
        
        # Add function curve
        fig.add_trace(go.Scatter(
            x=x_data,
            y=y_data,
            mode='lines',
            name=f'f({variable}) = {func_str}',
            line=dict(color='blue', width=2)
        ))
        
        # Add shaded area
        fig.add_trace(go.Scatter(
            x=x_fill,
            y=y_fill,
            fill='tozeroy',
            fillcolor='rgba(0, 100, 200, 0.3)',
            line=dict(color='rgba(0,0,0,0)'),
            name=f'{get_text("area_under_curve")} [{a}, {b}]',
            hovertemplate=f'{variable}: %{{x}}<br>f({variable}): %{{y}}<extra></extra>'
        ))
        
        # Add vertical lines at bounds
        y_min, y_max = min(y_data), max(y_data)
        fig.add_vline(x=a, line_dash="dash", line_color="red", 
                     annotation_text=f"{variable} = {a}")
        fig.add_vline(x=b, line_dash="dash", line_color="red", 
                     annotation_text=f"{variable} = {b}")
        
        # Update layout
        plot_title = title or f"{get_text('definite_integral')} ∫[{a}, {b}] {func_str} d{variable}"
        fig.update_layout(
            title=plot_title,
            xaxis_title=variable,
            yaxis_title=f'f({variable})',
            showlegend=True,
            hovermode='x unified',
            template='plotly_white'
        )
        
        # Add grid
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"{get_text('error_plotting_integral')}: {str(e)}")

def plot_riemann_sum(func_str: str, lower_bound: float, upper_bound: float, 
                    n: int, method: str = "left", variable: str = "x"):
    """
    Plot a function with Riemann sum rectangles.
    """
    try:
        a, b = lower_bound, upper_bound
        delta_x = (b - a) / n
        
        # Create function data for smooth curve
        x_min = min(a - 1, -10)
        x_max = max(b + 1, 10)
        x_data, y_data = create_function_data(func_str, x_min, x_max, variable)
        
        if len(x_data) == 0:
            return
        
        # Create the plot
        fig = go.Figure()
        
        # Add function curve
        fig.add_trace(go.Scatter(
            x=x_data,
            y=y_data,
            mode='lines',
            name=f'f({variable}) = {func_str}',
            line=dict(color='blue', width=2)
        ))
        
        # Add Riemann rectangles
        for i in range(n):
            x_left = a + i * delta_x
            x_right = a + (i + 1) * delta_x
            
            # Determine height based on method
            if method == "left":
                x_sample = x_left
            elif method == "right":
                x_sample = x_right
            else:  # midpoint
                x_sample = (x_left + x_right) / 2
            
            try:
                height = evaluate_expression(func_str, x_sample, variable)
            except:
                height = 0
            
            # Add rectangle
            fig.add_shape(
                type="rect",
                x0=x_left, y0=0, x1=x_right, y1=height,
                line=dict(color="red", width=1),
                fillcolor="rgba(255, 0, 0, 0.2)"
            )
            
            # Add sample point
            fig.add_trace(go.Scatter(
                x=[x_sample],
                y=[height],
                mode='markers',
                marker=dict(color='red', size=6),
                name=f'{get_text("sample_point")} {i+1}' if i == 0 else "",
                showlegend=i == 0,
                hovertemplate=f'{variable}: %{{x}}<br>f({variable}): %{{y}}<extra></extra>'
            ))
        
        # Update layout
        method_text = get_text(f"method_{method}")
        plot_title = f"{get_text('riemann_sum')} ({method_text}, n={n})"
        fig.update_layout(
            title=plot_title,
            xaxis_title=variable,
            yaxis_title=f'f({variable})',
            showlegend=True,
            hovermode='closest',
            template='plotly_white'
        )
        
        # Add grid
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"{get_text('error_plotting_riemann')}: {str(e)}")

def plot_area_between_curves(func1_str: str, func2_str: str, 
                           lower_bound: float, upper_bound: float, 
                           variable: str = "x", title: str = None):
    """
    Plot two functions with shaded area between them.
    """
    try:
        a, b = lower_bound, upper_bound
        
        # Extend range for better visualization
        x_min = min(a - 2, -10)
        x_max = max(b + 2, 10)
        
        # Create function data
        x_data, y1_data = create_function_data(func1_str, x_min, x_max, variable)
        _, y2_data = create_function_data(func2_str, x_min, x_max, variable)
        
        if len(x_data) == 0:
            return
        
        # Create data for shaded area
        x_fill = np.linspace(a, b, 200)
        y1_fill, y2_fill = [], []
        
        for x_val in x_fill:
            try:
                y1_val = evaluate_expression(func1_str, x_val, variable)
                y2_val = evaluate_expression(func2_str, x_val, variable)
                y1_fill.append(y1_val)
                y2_fill.append(y2_val)
            except:
                y1_fill.append(0)
                y2_fill.append(0)
        
        # Create the plot
        fig = go.Figure()
        
        # Add first function
        fig.add_trace(go.Scatter(
            x=x_data,
            y=y1_data,
            mode='lines',
            name=f'f₁({variable}) = {func1_str}',
            line=dict(color='blue', width=2)
        ))
        
        # Add second function
        fig.add_trace(go.Scatter(
            x=x_data,
            y=y2_data,
            mode='lines',
            name=f'f₂({variable}) = {func2_str}',
            line=dict(color='green', width=2)
        ))
        
        # Add shaded area between curves
        fig.add_trace(go.Scatter(
            x=x_fill + x_fill[::-1],
            y=y1_fill + y2_fill[::-1],
            fill='toself',
            fillcolor='rgba(255, 165, 0, 0.3)',
            line=dict(color='rgba(0,0,0,0)'),
            name=f'{get_text("area_between_curves")} [{a}, {b}]',
            hoverinfo='skip'
        ))
        
        # Add vertical lines at bounds
        fig.add_vline(x=a, line_dash="dash", line_color="red", 
                     annotation_text=f"{variable} = {a}")
        fig.add_vline(x=b, line_dash="dash", line_color="red", 
                     annotation_text=f"{variable} = {b}")
        
        # Update layout
        plot_title = title or f"{get_text('area_between_curves')} [{a}, {b}]"
        fig.update_layout(
            title=plot_title,
            xaxis_title=variable,
            yaxis_title=f'f({variable})',
            showlegend=True,
            hovermode='x unified',
            template='plotly_white'
        )
        
        # Add grid
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"{get_text('error_plotting_area')}: {str(e)}")
