from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path
from ids import print_final_path
import random

def heuristic(state, goal):

    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


def hill_climb_search(grid, start, goal):

    current = start
    path = [current]

    while current != goal:
        x, y = current
        neighbors = [
            (x + dx, y + dy)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if 0 <= x + dx < grid_size and 0 <= y + dy < grid_size and grid[x + dx][y + dy] != "X"
        ]

        if not neighbors:
            print("\nNo more valid moves!")
            return None

        next_state = min(neighbors, key=lambda n: heuristic(n, goal))

        if heuristic(next_state, goal) >= heuristic(current, goal):
            print("\n stuck at a local minimum")
            return None

        current = next_state
        path.append(current)

        print_grid_with_path(grid, path)

    print("\n path to goal found")
    return path


def hill_climb_algorithm(grid):

    print("running hill climbing search")
    path = hill_climb_search(grid, initial_state, goal_state)

    if path:
        print("final path found is:")
        print_final_path(grid, path)
    else:
        print("no path found")
