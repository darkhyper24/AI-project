from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path
import time
from heapq import heappop, heappush
import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def printallnodesheuristic(goal):
    for i in range(grid_size):
        for j in range(grid_size):
            print(f"Manhattan distance from ({i}, {j}) to goal is {euclidean_distance((i, j), goal)}")

def greedy_best_first_euclidean(grid,start,goal):
    printallnodesheuristic(goal)
    explored = set()
    heuristic = euclidean_distance(start, goal)
    frontier = [(heuristic, start, [start])]
    max_frontier_size = 1

    while frontier:
        _, node, path = heappop(frontier)
        if node == goal:
            return path
        explored.add(node)
        x, y = node
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for delta_x, delta_y in directions:
            next_x, next_y = x + delta_x, y + delta_y
            neighbor = (next_x, next_y)

            if (0 <= next_x < grid_size and 0 <= next_y < grid_size and neighbor not in explored and grid[next_x][next_y] != "X"):

                neighbor_heuristic = euclidean_distance(neighbor, goal)
                explored.add(neighbor)
                new_path = path + [neighbor]
                heappush(frontier, (neighbor_heuristic, neighbor, new_path))
                max_frontier_size = max(max_frontier_size, len(frontier))


                print(f"Exploring {neighbor} with heuristic {neighbor_heuristic}")
                print_grid_with_path(grid, new_path)
                if neighbor == goal:
                    return new_path
    return None


def greedy_best_first_euclidean_algorithm(grid, start, goal):

    start_time=time.time()
    while True:
        path = greedy_best_first_euclidean(grid, start, goal)
        if path:
            end_time=time.time()
            print("\nPath to goal found:")
            print_final_path(grid, path)
            print("Path taken:", path)
            print(f"time taken for the greedy best first search algorithm to search for the goal is:{end_time-start_time} seconds")
            return path

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
