from problem_formulation import generate_valid_grid,initial_state,goal_state
from ids import ids_algorithm
from ucs import ucs_search,ucs_algorithm
from simulated_annealing import simulated_annealing,SA_algorithm
from greedy_best_euclidean import greedy_best_first_euclidean_algorithm
from greedy_best_manhattan import greedy_best_first_manhattan_algorithm
grid = generate_valid_grid()

print("Generated 5x5 grid with 5 obstacles:")

#ids_algorithm(grid,initial_state,goal_state)
#ucs_algorithm(grid)
#SA_algorithm(grid)
greedy_best_first_euclidean_algorithm(grid,initial_state,goal_state)
greedy_best_first_manhattan_algorithm(grid,initial_state,goal_state)




