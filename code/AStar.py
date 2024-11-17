from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path,calculate_cost
import time
import heapq
from ids import print_final_path
from visualisation import visualize_grid_path


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def printallnodesheuristic(goal):
    for i in range(grid_size):
        for j in range(grid_size):
            print(f"Manhattan distance from ({i}, {j}) to goal is {manhattan_distance((i, j), goal)}")

def a_star_search(grid):
    heuristic = manhattan_distance
    frontier = [(0 + heuristic(initial_state, goal_state), 0, initial_state, [])] #we add 0 here for the extra cost for function f(n) = g(n) + h(n)
    visited = set()

    while frontier:
        f_value, g_value, position, path = heapq.heappop(frontier)
        x, y = position

        if position in visited:
            continue

        visited.add(position) #add node to explored
        path = path + [position]

        if position == goal_state:
            print("\nPath to goal found\n")
            print("Path taken:", path)
            print("Total cost:", g_value)
            print("\n")
            return path

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for delta_x, delta_y in directions:
            next_x = x + delta_x
            next_y = y + delta_y
            next_position = (next_x, next_y)

            if 0 <= next_x < grid_size and 0 <= next_y < grid_size:                   #checks if neighbor x and y are within the grid aka from 0,4
                if next_position not in visited and grid[next_x][next_y] != "X":      #checks if the neighbor is not visited and is not an obstacle
                    g_next = g_value + 1                                              #we calculate g(n) by adding the cost of the current node to the cost of the neighbor
                    h_next = heuristic(next_position, goal_state)
                    f_next = g_next + h_next                                          #this is the function f(n) = g(n) + h(n)
                    print(f"Neighbor: {next_position}, g(n): {g_next}, h(n): {h_next}, f(n): {f_next}")
                    print_grid_with_path(grid, path)
                    heapq.heappush(frontier, (f_next, g_next, next_position, path))

    return None

def AStar_algorithm(grid):
    start_time=time.time()
    while True:
        path = a_star_search(grid)
        if path:
            end_time=time.time()
            total_time = end_time-start_time
            total_cost = calculate_cost(path)
            print("\nPath to goal found:")
            print_final_path(grid, path)
            print("Path taken:", path)
            print(f"time taken for the A* algorithm to search for the goal is:{total_time} seconds")
            print(f"the cost is : {total_cost}")
            visualize_grid_path(grid, path, initial_state, goal_state, "A*")
            return path, total_time, total_cost