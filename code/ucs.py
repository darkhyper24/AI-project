import heapq
from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path

# uniform Cost Search function
def ucs_search(grid):
    # Priority queue for frontier (cost, position, path)
    frontier = [(0, initial_state, [])]
    visited = set()

    while frontier:
        # lowest cost
        cost, position, path = heapq.heappop(frontier)
        x, y = position

        if position in visited:
            continue

        visited.add(position)
        path = path + [position]  
        print_grid_with_path(grid, path)

        # Check if goal state is reached
        if position == goal_state:
            print("\nPath to goal found")
            # print_grid_with_path(grid, path)
            print("Path taken:", path)
            print("Total cost:", cost)
            return path

        # Explore (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for delta_x, delta_y in directions:
            next_x = x + delta_x
            next_y = y + delta_y
            next_position = (next_x, next_y)

            if 0 <= next_x < grid_size and 0 <= next_y < grid_size:
                if next_position not in visited and grid[next_x][next_y] != "X":
                    # cost is 1 for each step
                    heapq.heappush(frontier, (cost + 1, next_position, path))

    print("No path to goal exists.")
    return None
