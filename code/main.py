from problem_formulation import generate_valid_grid
from ids import ids_search
from ucs import ucs_search

grid = generate_valid_grid()

print("Generated 5x5 grid with 5 obstacles:")


# ids_search(grid)
ucs_search(grid)



