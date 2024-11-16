
from collections import deque
from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path
from ids import print_final_path

def bfs_search(grid, start, goal):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        for x, y in directions:
            neighbor = (current[0] + x, current[1] + y)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and \
               neighbor not in visited and grid[neighbor[0]][neighbor[1]] != "X":
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

def bfs_algorithm(grid):
    start = initial_state
    goal = goal_state

    print("running BFS")
    path = bfs_search(grid, start, goal)
    
    if path:
        print("Shortest Path Found:")
        print_final_path(grid, path)  
        print_grid_with_path(grid, path)  
        return path
    else:
        print("no path found")
        return None
