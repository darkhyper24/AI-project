from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path,calculate_cost,print_final_path
import time


def depth_limited_search(grid, start, goal, limit):
    stack = [(start, 0, [])]  
    visited = set()           

    while stack:
        current,depth,path=stack.pop()


        if current in visited:
            continue

        visited.add(current)
        path = path + [current]


        print_grid_with_path(grid, path)

        if current == goal:
            return path

        if depth < limit:
            x, y = current
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for delta_x, delta_y in directions:
                next_x = x + delta_x
                next_y = y + delta_y
                next_position = (next_x, next_y)

                if (0 <= next_x < grid_size and 0 <= next_y < grid_size and next_position not in visited and grid[next_x][next_y] != "X"):
                    stack.append((next_position, depth + 1, path))

    return None




def ids_algorithm(grid, start, goal):

    depth = 0
    start_time=time.time()
    while True:
        print(f"\nTrying depth limit: {depth}")
        path = depth_limited_search(grid, start, goal, depth)

        if path:
            end_time=time.time()
            total_time = end_time-start_time
            total_cost = calculate_cost(path)
            print("\nPath to goal found:")
            print_final_path(grid, path)
            print("Path taken: ", path)
            print(f"time taken for the ids algorithm to search for the goal is:{total_time} seconds")
            print(f"the cost is : {total_cost}")
            return path, total_time, total_cost
        depth += 1
        
