from collections import deque
from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path,calculate_cost,print_final_path
import time

def bfs_search(grid, start, goal):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    step = 0 
    while queue:
        current, path = queue.popleft()


        step += 1
        print(f"Step {step}: Exploring {current}")
        print_grid_with_path(grid, path)

        if current == goal:
            return path

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if (
                0 <= neighbor[0] < len(grid)
                and 0 <= neighbor[1] < len(grid[0])
                and neighbor not in visited
                and grid[neighbor[0]][neighbor[1]] != "X"
            ):
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

def bfs_algorithm(grid):

    start = initial_state
    goal = goal_state

    start_time=time.time()
    path = bfs_search(grid, start, goal)

    if path:
        end_time=time.time()
        total_time = end_time-start_time
        total_cost = calculate_cost(path)
        print(f"the path cost is: {total_cost}")
        print(f"time taken for the ids algorithm to search for the goal is:{total_time} seconds")
        print(f" Path taken: {path}")
        print_final_path(grid, path)
        return path, total_time, total_cost