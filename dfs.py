from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path
from ids import print_final_path

def dfs_search(grid, start, goal):

    stack = [(start, [start])] 
    visited = set()

    while stack:
        current, path = stack.pop()  
        
        if current in visited:
            continue

        visited.add(current)

        print_grid_with_path(grid, path)

        if current == goal:
            print("\n path to goal found")
            print("path:", path)
            return path

        x, y = current
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for delta_x, delta_y in directions:
            next_x, next_y = x + delta_x, y + delta_y
            next_position = (next_x, next_y)

            if 0 <= next_x < grid_size and 0 <= next_y < grid_size and next_position not in visited:
                if grid[next_x][next_y] != "X": 
                    stack.append((next_position, path + [next_position]))

    print("\nNo path to goal found!")
    return None


def dfs_algorithm(grid):
    
    start = initial_state
    goal = goal_state

    print("running DFS")
    path = dfs_search(grid, start, goal)

    if path:
        print("final path found is:")
        print_final_path(grid, path)
    else:
        print("no path found")
