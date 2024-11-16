from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path
from ids import print_final_path

def dfs_search(grid, start, goal):

    stack = [(start, [start])]  # Stack holds tuples of (current_position, path)
    visited = set()

    while stack:
        current, path = stack.pop()  # Pop the top of the stack

        # Skip already visited nodes
        if current in visited:
            continue

        visited.add(current)

        # Visualize current path
        print_grid_with_path(grid, path)

        # Check if goal is reached
        if current == goal:
            print("\nPath to goal found!")
            print("Path:", path)
            return path

        # Explore neighbors (up, down, left, right)
        x, y = current
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for delta_x, delta_y in directions:
            next_x, next_y = x + delta_x, y + delta_y
            next_position = (next_x, next_y)

            # Add to stack if within bounds and not an obstacle
            if 0 <= next_x < grid_size and 0 <= next_y < grid_size and next_position not in visited:
                if grid[next_x][next_y] != "X":  # Avoid obstacles
                    stack.append((next_position, path + [next_position]))

    print("\nNo path to goal found!")
    return None


def dfs_algorithm(grid):
    
    start = initial_state
    goal = goal_state

    print("Running Depth-First Search (DFS)...")
    path = dfs_search(grid, start, goal)

    if path:
        print("Final Path Found:")
        print_final_path(grid, path)
    else:
        print("No path found!")
