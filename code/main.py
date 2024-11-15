from problem_formulation import generate_valid_grid,initial_state,goal_state
from ids import ids_algorithm

grid = generate_valid_grid()

print("Generated 5x5 grid with 5 obstacles:")

ids_algorithm(grid,initial_state,goal_state)






