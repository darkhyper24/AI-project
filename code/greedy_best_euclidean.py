from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path,calculate_cost,print_final_path
import time
import heapq
import math
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from visualisation import visualize_grid_path

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def printallnodesheuristic(goal):
    for i in range(grid_size):
        for j in range(grid_size):
            print(f"Euclidean distance from ({i}, {j}) to goal is {euclidean_distance((i, j), goal)}")

def greedy_best_first_euclidean(grid,start,goal):
    printallnodesheuristic(goal)
    explored = set()
    heuristic = euclidean_distance(start, goal)
    frontier = [(heuristic, start, [start])]

    while frontier:
        _, node, path = heapq.heappop(frontier)
        if node == goal:
            return path
        explored.add(node)
        x, y = node
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for delta_x, delta_y in directions:
            next_x = x + delta_x
            next_y = y + delta_y
            neighbor = (next_x, next_y)

            if (0 <= next_x < grid_size and 0 <= next_y < grid_size and neighbor not in explored and grid[next_x][next_y] != "X"):

                neighbor_heuristic = euclidean_distance(neighbor, goal) #calculate the heuristic for the neighbor
                explored.add(neighbor)
                new_path = path + [neighbor]        #update path to return it later
                heapq.heappush(frontier, (neighbor_heuristic, neighbor, new_path))        #push into frontier


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
            total_time = end_time-start_time
            total_cost = calculate_cost(path)
            print("\nPath to goal found:")
            print_final_path(grid, path)
            print("Path taken:", path)
            print(f"time taken for the greedy best first search algorithm using euclidean to search for the goal is:{total_time} seconds")
            print(f"the cost is : {total_cost}")
            visualize_grid_path(grid, path, start, goal, "Greedy Best First Euclidean")
            return path, total_time, total_cost

