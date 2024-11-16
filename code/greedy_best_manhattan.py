from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path,calculate_cost,print_final_path
import time
from heapq import heappop, heappush

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def printallnodesheuristic(goal):
    for i in range(grid_size):
        for j in range(grid_size):
            print(f"Manhattan distance from ({i}, {j}) to goal is {manhattan_distance((i, j), goal)}")

def greedy_best_first(grid,start,goal):
    printallnodesheuristic(goal)
    explored = set()
    heuristic = manhattan_distance(start, goal)
    frontier = [(heuristic, start, [start])]

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

                neighbor_heuristic = manhattan_distance(neighbor, goal)
                explored.add(neighbor)
                new_path = path + [neighbor]
                heappush(frontier, (neighbor_heuristic, neighbor, new_path))
                print(f"Exploring {neighbor} with heuristic {neighbor_heuristic}")
                print_grid_with_path(grid, new_path)
                if neighbor == goal:
                    return new_path
    return None


def greedy_best_first_manhattan_algorithm(grid, start, goal):

    start_time=time.time()
    while True:
        path = greedy_best_first(grid, start, goal)
        if path:
            end_time=time.time()
            total_time = end_time-start_time
            total_cost = calculate_cost(path)
            print("\nPath to goal found:")
            print_final_path(grid, path)
            print("Path taken:", path)
            print(f"time taken for the greedy best first search algorithm to search for the goal is:{total_time} seconds")
            print(f"the cost is : {total_cost}")
            return path, total_time, total_cost
