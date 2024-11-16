from tabulate import tabulate
from greedy_best_euclidean import greedy_best_first_euclidean_algorithm
from greedy_best_manhattan import greedy_best_first_manhattan_algorithm
from AStar import AStar_algorithm
from bfs import bfs_algorithm
from ids import ids_algorithm
from ucs import ucs_algorithm
from simulated_annealing import SA_algorithm
from problem_formulation import generate_valid_grid,initial_state,goal_state,print_grid_with_path,calculate_cost,print_final_path
grid = generate_valid_grid()
print("Generated 5x5 grid with 5 obstacles:")


path, total_time, total_cost = ids_algorithm(grid,initial_state,goal_state)
ids_performance = (path,total_time, total_cost)
path, total_time, total_cost = SA_algorithm(grid)
SA_performance = (path,total_time, total_cost)
path, total_time, total_cost = greedy_best_first_euclidean_algorithm(grid,initial_state,goal_state)
greedy_best_first_euclidean_performance = (path,total_time, total_cost)
path, total_time, total_cost = greedy_best_first_manhattan_algorithm(grid,initial_state,goal_state)
greedy_best_first_manhattan_performance = (path,total_time, total_cost)
path, total_time, total_cost = AStar_algorithm(grid)
AStar_performance = (path,total_time, total_cost)
path, total_time, total_cost = ucs_algorithm(grid)
ucs_performance = (path,total_time, total_cost)
path, total_time, total_cost = bfs_algorithm(grid)
bfs_performance = (path,total_time, total_cost)


all_performances = [bfs_performance, ids_performance,ucs_performance,greedy_best_first_euclidean_performance, greedy_best_first_manhattan_performance, AStar_performance , SA_performance]
def print_all_performances(all_performances):
    headers = ["Algorithm", "Path Taken", "Time Taken (s)", "Total Cost"]
    table_data = []
    algorithms = [
        "Breadth First Search (BFS)",
        "Iterative Deepening Search (IDS)",
        "Uniform Cost Search (UCS)",
        "Greedy Best First (Euclidean)",
        "Greedy Best First (Manhattan)",
        "A* Search" ,
        "Simulated Annealing"

    ]
    
    for i, performance in enumerate(all_performances):
        path, total_time, total_cost = performance
        table_data.append([algorithms[i], path, round(total_time, 4), total_cost])
    print("\nAlgorithm Performance Table:")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


print_all_performances(all_performances)