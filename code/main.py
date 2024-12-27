from tabulate import tabulate
from greedy_best_euclidean import greedy_best_first_euclidean_algorithm
from greedy_best_manhattan import greedy_best_first_manhattan_algorithm
from AStar import AStar_algorithm
from AStarEuclidean import AStar_algorithm_Euclidean
from bfs import bfs_algorithm
from q_learning_algorithm import q_learning_algorithm
from ids import ids_algorithm
from ucs import ucs_algorithm
from dfs import dfs_algorithm
from hill_climbing import hill_climbing_algorithm
from simulated_annealing import SA_algorithm
from genetic import Gen_algorithm
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

path, total_time, total_cost = AStar_algorithm_Euclidean(grid)
AStar_performance_Euclidean = (path,total_time, total_cost)

path, total_time, total_cost = ucs_algorithm(grid)
ucs_performance = (path,total_time, total_cost)

path, total_time, total_cost = bfs_algorithm(grid)
bfs_performance = (path,total_time, total_cost)

path, total_time,total_cost = dfs_algorithm(grid,initial_state,goal_state)
dfs_performance=(path,total_time,total_cost)

path, total_time,total_cost = hill_climbing_algorithm(grid,initial_state,goal_state)
hill_climbing_performance=(path,total_time,total_cost)

path, total_time, total_cost = Gen_algorithm(grid)
Gen_performance = (path,total_time,total_cost)

path, total_time, total_cost = q_learning_algorithm(grid)
q_learning_performance = (path, total_time, total_cost)

all_performances = [bfs_performance,dfs_performance, ids_performance,ucs_performance,greedy_best_first_euclidean_performance, greedy_best_first_manhattan_performance, AStar_performance , AStar_performance_Euclidean, hill_climbing_performance, SA_performance, Gen_performance, q_learning_performance]
def print_all_performances(all_performances):
    headers = ["Algorithm", "Path Taken", "Time Taken (s)", "Total Cost"]
    table_data = []
    algorithms = [
        "Breadth First Search (BFS)",
        "Depth First Search (DFS)",
        "Iterative Deepening Search (IDS)",
        "Uniform Cost Search (UCS)",
        "Greedy Best First (Euclidean)",
        "Greedy Best First (Manhattan)",
        "A* Search",
        "A* Search (Euclidean)",
        "hill climbing search",
        "Simulated Annealing",
        "Genetic Algorithm",
        "Q-Learning"
    ]
    
    for i, performance in enumerate(all_performances):
        path, total_time, total_cost = performance
        
        if path is None:
            path_str = "No Path Found"
        else:

            path_str = "\n".join([str(path[j:j+5]) for j in range(0, len(path), 5)])
        table_data.append([algorithms[i], path_str, round(total_time, 4) if total_time else "N/A", total_cost if total_cost else "N/A"])
    
    print("\nAlgorithm Performance Table:")
    print(tabulate(table_data, headers=headers, tablefmt="grid", maxcolwidths=[20, 50, 20, 15]))


print_all_performances(all_performances)