import math
import random
import time
from problem_formulation import initial_state, goal_state, print_grid_with_path,calculate_cost,print_final_path

def get_neighbors(grid, state):
    """
    Get valid neighbors of a state in the grid.
    :param grid: The grid with obstacles.
    :param state: Current state (x, y).
    :return: List of valid neighbors.
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    neighbors = []
    for dx, dy in directions:
        nx, ny = state[0] + dx, state[1] + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "X":
            neighbors.append((nx, ny))
    return neighbors


def calculate_cost(path):
    """
    Calculate the cost of a path.
    :param path: List of states representing the path.
    :return: Cost of the path (length).
    """
    return len(path)


def simplify_path(path):
    """
    Simplify a path by removing cycles.
    :param path: List of states representing the path.
    :return: Simplified path without cycles.
    """
    optimized_path = []
    for state in path:
        if state not in optimized_path:
            optimized_path.append(state)
    return optimized_path


def simulated_annealing(grid, max_steps=1000, initial_temperature=100, cooling_rate=0.95, delay=0.5):
    current_state = initial_state
    path = [current_state]
    visited = set([current_state])
    temperature = initial_temperature
    goal_reached = False

    for step in range(max_steps):
        temperature *= cooling_rate
        # Visualization
        if step % 10 == 0 or current_state != path[-1]:
            print(f"Step {step + 1}, Temperature: {temperature:.2f}")
            print_grid_with_path(grid, path)

        # Stop if temperature is too low
        if temperature < 1e-3:
            break

        # Check if goal is reached
        if not goal_reached and current_state == goal_state:
            goal_reached = True
            path = simplify_path(path)  # Simplify immediately upon reaching goal

        # Get neighbors and select the next state
        neighbors = get_neighbors(grid, current_state)

        if goal_reached:
            # Post-goal: Explore for optimization
            neighbors = [n for n in neighbors if n not in path]
            if not neighbors:
                break
            next_state = random.choice(neighbors)
            new_path = path + [next_state]
            new_path = simplify_path(new_path)
            if calculate_cost(new_path) < calculate_cost(path):  # Accept only better paths
                path = new_path
        else:
            # Pre-goal: Regular exploration
            valid_neighbors = [state for state in neighbors if state not in visited]
            if not valid_neighbors:
                continue
            next_state = random.choice(valid_neighbors)
            current_state = next_state
            path.append(current_state)
            visited.add(current_state)



    # Final visualization
    print("Final Grid with Optimized Path:")
    print_grid_with_path(grid, path)

    if goal_reached:
        print(f"Optimized path: {path}")
        return path
    else:
        return None




def SA_algorithm(grid):
    start_time=time.time()
    path = simulated_annealing(grid,delay=0.5)

    if path:
        end_time=time.time()
        total_time = end_time-start_time
        total_cost = calculate_cost(path)
        print("Path to goal found using Simulated Annealing:")
        print_final_path(grid, path)
        print(f"time taken for simulated annealing to find path: {total_time} seconds")
        print(f"the cost is : {total_cost}")
        return path, total_time, total_cost
    else:
        print("Goal not reached.")
        return path, 0, 0