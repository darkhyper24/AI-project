import random
from collections import deque

grid_size = 5
initial_state = (0, 0)
goal_state = (4,4)
num_of_obstacle = 5  

def create_grid():
    
    grid = []
    
    for _ in range(grid_size):
        row = []
        for _ in range(grid_size):
            row.append("_")
        grid.append(row)
        
    grid[0][0] = "S" 
    grid[grid_size-1][grid_size-1] = "G"
           
    return grid

def place_obstacles(grid):
    
    obstacles = 0
    
    while obstacles < num_of_obstacle:
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - 1)
        
        if (x, y) not in [initial_state, goal_state] and grid[x][y] == "_":
            grid[x][y] = "X"
            obstacles += 1

# Check if there is a path from start to goal using BFS
def has_path(grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([initial_state])
    visited = set([initial_state])

    while queue:
        x, y = queue.popleft()
        if (x, y) == goal_state:
            return True
        
        for delta_x, delta_y in directions:
            next_x = x + delta_x 
            next_y = y + delta_y
            
            if 0 <= next_x < grid_size and 0 <= next_y < grid_size and (next_x, next_y) not in visited:
                if grid[next_x][next_y] != "X":
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y))
    return False
#x for obstacles s for start g for goal _ for free cells
def print_grid_with_path(grid, path=[]):
    symbols = {"_": "_", "X": "X", "S": "S", "G": "G"}
    display_grid = []
    for row in grid:
        new_row = []
        for cell in row:
            new_row.append(symbols[cell])
        display_grid.append(new_row)
    
    for (x, y) in path:
        if display_grid[x][y] == "_":
            display_grid[x][y] = "O"  
    
    for row in display_grid:
        print(" ".join(row))
    print("\n")

# Generate a valid grid with obstacles and ensure path existence
def generate_valid_grid():
    while True:
        grid = create_grid()
        place_obstacles(grid)
        
        if has_path(grid):
            return grid

def calculate_cost(path):
    return len(path)-1

        
        
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
