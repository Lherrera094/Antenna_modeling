import plotly.graph_objects as go
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QVBoxLayout, QWidget


def plot_antenna(sections, parent_widget):
    """
    Plot all sections of the antenna in an interactive 3D graph using Plotly.
    """
    # Create a Plotly figure
    fig = go.Figure()

    # Add each section to the plot
    for section_name, coordinates in sections.items():
        x = [coord[0] for coord in coordinates]
        y = [coord[1] for coord in coordinates]
        z = [coord[2] for coord in coordinates]
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode = 'markers',
                      marker = dict(
                          size=2,
                          color = "navy",
                          opacity=0.8
                      ),
            name=section_name
        ))

    # Update layout for better visualization
    fig.update_layout(
        title = "Antenna Geometry",
        scene=dict(
            xaxis_title="X (grid points)",
            yaxis_title="Y (grid points)",
            zaxis_title="Z (grid points)",
        ),
        margin=dict(l=0, r=0, b=0, t=0),
    )

    fig.show()