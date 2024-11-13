from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path

# Iterative Deepening Search function
def ids_search(grid):
    depth = 0
    
    while True:
        print(f"\nTrying depth limit: {depth}")
        visited = set()
        path = ids_dfs(grid, initial_state, depth, visited, path=[])
        
        if path:
            print("\nPath to goal found:")
            print_final_path(grid, path)
            print("Path taken:", path)
            return path
        depth += 1

# Depth-Limited DFS helper for IDS that returns the path if goal is reached
def ids_dfs(grid, position, limit, visited, path):
    x, y = position
    path.append(position)

    if position == goal_state:
        return path
    
    if limit <= 0:
        path.pop()
        return None

    visited.add(position)
    print_grid_with_path(grid, path)
    
    # Explore neighbors (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for delta_x, delta_y in directions:
        next_x = x + delta_x
        next_y = y + delta_y
        next_position = (next_x, next_y)
        
        if 0 <= next_x < grid_size and 0 <= next_y < grid_size:
            
            if next_position not in visited and grid[next_x][next_y] != "X":
                result = ids_dfs(grid, next_position, limit - 1, visited, path)
                
                if result:  # If the path is found, return it
                    return result

    # Backtrack
    path.pop()
    visited.remove(position)
    return None

# Print the final path taken to reach the goal
def print_final_path(grid, path):
    display_grid = []
    for row in grid:
        new_row = []
        
        for cell in row:
            new_row.append(cell)
        display_grid.append(new_row)

    for (x, y) in path:
        if display_grid[x][y] == "_":
            display_grid[x][y] = "P"
    
    for row in display_grid:
        print(" ".join(row))
    print("\n")
