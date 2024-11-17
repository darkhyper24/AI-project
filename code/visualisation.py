import matplotlib.pyplot as plt
import numpy as np


def visualize_grid_path(grid, path, start, goal, title):
    grid_size = len(grid)
    fig, nx = plt.subplots(figsize=(6, 6))
    
    nx.set_xlim(0, grid_size)
    nx.set_ylim(0, grid_size)
    nx.set_xticks(np.arange(0, grid_size + 1, 1))
    nx.set_yticks(np.arange(0, grid_size + 1, 1))
    nx.set_aspect('equal')

    nx.add_patch(plt.Rectangle((start[1], grid_size - start[0] - 1), 1, 1, color='blue'))
    nx.add_patch(plt.Rectangle((goal[1], grid_size - goal[0] - 1), 1, 1, color='green'))

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == "X":
                nx.add_patch(plt.Rectangle((j, grid_size - i - 1), 1, 1, color='red'))
    
    for (x, y) in path:
        if (x, y) != start and (x, y) != goal:
            nx.add_patch(plt.Rectangle((y, grid_size - x - 1), 1, 1, color='yellow'))

    plt.title(title)
    plt.show()