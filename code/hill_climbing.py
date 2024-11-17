from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path, calculate_cost, print_final_path
import time
import math


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def hill_climbing(grid, start, goal):
    current = start
    path = [current]

    while current != goal:
        x, y = current
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []

        for delta_x, delta_y in directions:
            next_x = x + delta_x
            next_y = y + delta_y
            neighbor = (next_x, next_y)

            if (0 <= next_x < grid_size and 0 <= next_y < grid_size and grid[next_x][next_y] != "X"):
                neighbors.append(neighbor)

        if not neighbors:
            print("No valid moves available. Hill climbing failed.")
            return None

        current = min(neighbors, key=lambda n: manhattan_distance(n, goal))

        if current in path:
            print("Stuck in a loop. Hill climbing failed.")
            return None

        path.append(current)
        print(f"Current Node: {current}, Heuristic: {manhattan_distance(current, goal)}")
        print_grid_with_path(grid, path)

    return path


def hill_climbing_algorithm(grid, start, goal):
    start_time = time.time()
    path = hill_climbing(grid, start, goal)
    end_time = time.time()
    total_time = end_time - start_time
    if path:
        total_cost = calculate_cost(path)
        print("\nPath to goal found:")
        print_final_path(grid, path)
        print("Path taken:", path)
        print(f"time taken for the hill climbing algorithm to search for the goal is: {total_time} seconds")
        print(f"the cost is: {total_cost}")
        return path, total_time, total_cost
    else:
        return path,total_time,0
