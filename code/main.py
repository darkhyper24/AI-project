from problem_formulation import generate_valid_grid
from ids import ids_search

grid = generate_valid_grid()

print("Generated 3x3 grid with obstacles:")


ids_search(grid)




