import heapq
from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path,calculate_cost,print_final_path
import time
from visualisation import visualize_grid_path
def ucs_search(grid):

    frontier = [(0, initial_state, [])]
    visited = set()

    while frontier:

        cost, position, path = heapq.heappop(frontier)
        x, y = position

        if position in visited:
            continue

        visited.add(position)
        path = path + [position]
        print_grid_with_path(grid, path)


        if position == goal_state:
            print("\nPath to goal found\n")

            return path


        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for delta_x, delta_y in directions:
            next_x = x + delta_x
            next_y = y + delta_y
            next_position = (next_x, next_y)

            if 0 <= next_x < grid_size and 0 <= next_y < grid_size:
                if next_position not in visited and grid[next_x][next_y] != "X":

                    heapq.heappush(frontier, (cost + 1, next_position, path))

    return None

def ucs_algorithm(grid):
    start_time=time.time()
    path = ucs_search(grid)
    end_time=time.time()
    total_time=end_time-start_time
    total_cost=calculate_cost(path)
    print("final path to goal:\n")
    print_final_path(grid,path)
    print(f"time taken for ucs to reach goal is: {total_time}")
    print(f"path cost is: {total_cost}")
    visualize_grid_path(grid, path, initial_state, goal_state, "UCS")
    return path,total_time,total_cost