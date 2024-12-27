import plotly.graph_objects as go
import numpy as np

def visualize_grid_path(grid, path, start, goal, title):
    grid_size = len(grid)
    fig = go.Figure()

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == "X":
                fig.add_shape(type="rect", x0=j, y0=grid_size - i - 1, x1=j+1, y1=grid_size - i, fillcolor="red", line=dict(color="red"))

    fig.add_shape(type="rect", x0=start[1], y0=grid_size - start[0] - 1, x1=start[1]+1, y1=grid_size - start[0], fillcolor="blue", line=dict(color="blue"))
    fig.add_shape(type="rect", x0=goal[1], y0=grid_size - goal[0] - 1, x1=goal[1]+1, y1=grid_size - goal[0], fillcolor="green", line=dict(color="green"))

    for (x, y) in path:
        if (x, y) != start and (x, y) != goal:
            fig.add_shape(type="rect", x0=y, y0=grid_size - x - 1, x1=y+1, y1=grid_size - x, fillcolor="yellow", line=dict(color="yellow"))

    fig.update_layout(title=title, xaxis=dict(tickmode='array', tickvals=list(range(grid_size+1))), yaxis=dict(tickmode='array', tickvals=list(range(grid_size+1))), showlegend=False)
    fig.show()