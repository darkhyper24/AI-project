import math
import random
import time
from problem_formulation import initial_state, goal_state, print_grid_with_path,calculate_cost,print_final_path
from visualisation import visualize_grid_path

def get_neighbors(grid, state):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    neighbors = []
    x=state[0]
    y=state[1]
    for delta_x, delta_y in directions:
        next_x = x + delta_x
        next_y = y + delta_y
        if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] != "X":
            neighbors.append((next_x, next_y))
    return neighbors


def calculate_cost(path):
    return len(path)

def simplify_path(path):

    optimized_path = []
    for state in path:
        if state not in optimized_path:
            optimized_path.append(state)
    return optimized_path

def simulated_annealing(grid, max_steps=1000, initial_temperature=100, cooling_rate=0.95):
    current_state = initial_state
    path = [current_state]
    visited = set([current_state])
    temperature = initial_temperature
    goal_reached = False

    for step in range(max_steps):
        temperature *= cooling_rate

        if step % 10 == 0 or current_state != path[-1]:
            print(f"Step {step + 1}, Temperature: {temperature:.2f}")
            print_grid_with_path(grid, path)

        if temperature < 1e-3:
            break

        if not goal_reached and current_state == goal_state:
            goal_reached = True
            path = simplify_path(path)

        neighbors = get_neighbors(grid, current_state)

        if goal_reached:
            
            neighbors = [n for n in neighbors if n not in path]
            if not neighbors:
                break
            next_state = random.choice(neighbors)
            new_path = path + [next_state]
            new_path = simplify_path(new_path)
            if calculate_cost(new_path) < calculate_cost(path):
                path = new_path
        else:

            valid_neighbors = [state for state in neighbors if state not in visited]
            if not valid_neighbors:
                continue
            next_state = random.choice(valid_neighbors)
            current_state = next_state
            path.append(current_state)
            visited.add(current_state) 

    if goal_reached:
        print("Path to goal found using Simulated Annealing:\n")
        print_final_path(grid,path)
        print(f"path to reach goal: {path}")
        return path
    
    else:
        print("Goal not reached.")
        print(f"path that didn't reach the goal{path}")
        print_grid_with_path(grid,path)
        return None

def SA_algorithm(grid):
    start_time=time.time()
    path = simulated_annealing(grid)
    end_time=time.time()
    total_time = end_time-start_time
    if path:
        total_cost = calculate_cost(path)
        print(f"time taken for simulated annealing to find path: {total_time} seconds\n")
        print(f"the path cost is : {total_cost}\n")
        visualize_grid_path(grid, path, initial_state, goal_state, "Simulated Annealing")
        return path, total_time, total_cost
    
    else:
        print(f"time taken for simulated annealing without finding path: {total_time} seconds\n")
        return path, total_time, 0