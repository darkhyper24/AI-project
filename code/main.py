from problem_formulation import generate_valid_grid
from ids import ids_search
from ucs import ucs_search, ucs_algorithm
from genetic import genetic_algorithm, Gen_algorithm

grid = generate_valid_grid()

print("Generated 5x5 grid with 5 obstacles:")


# ids_search(grid)
ucs_algorithm(grid)

# Gen_algorithm(grid)


