import random, time
from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path


def manhattan_distance(state1, state2):
    #Manhattan distance
    return abs(state1[0] - state2[0]) + abs(state1[1] - state2[1])

def generate_random_path():
    directions = ["U", "D", "L", "R"]
    return [random.choice(directions) for _ in range(grid_size * 2)]  

def apply_move(position, move):
    x, y = position
    if move == "U": return (x - 1, y)
    if move == "D": return (x + 1, y)
    if move == "L": return (x, y - 1)
    if move == "R": return (x, y + 1)
    return position

def evaluate_path(path, grid):
    #fitness
    position = initial_state
    visited = set([initial_state])
    path_length = 0

    for move in path:
        next_position = apply_move(position, move)
        if 0 <= next_position[0] < grid_size and 0 <= next_position[1] < grid_size:
            if grid[next_position[0]][next_position[1]] == "X":
                break  #obstacle
            position = next_position
            visited.add(position)
            path_length += 1
        else:
            break 

        if position == goal_state:
            return len(path) - path_length + 1

    return manhattan_distance(position, goal_state) + path_length

def initialize_population(population_size):
    return [generate_random_path() for _ in range(population_size)]

def tournament_selection(population, fitnesses, k=3):
    selected = []
    for _ in range(len(population) // 2):  # Half the population
        competitors = random.sample(list(zip(population, fitnesses)), k)
        winner = min(competitors, key=lambda x: x[1])  # Lower fitness
        selected.append(winner[0])
    return selected

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(genome, mutation_rate=0.1):
    directions = ["U", "D", "L", "R"]
    for i in range(len(genome)):
        if random.random() < mutation_rate:
            genome[i] = random.choice(directions)
    return genome

def decode_genome(path):
    position = initial_state
    decoded_path = [position]

    for move in path:
        position = apply_move(position, move)
        if position == goal_state:
            decoded_path.append(position)
            break
        if 0 <= position[0] < grid_size and 0 <= position[1] < grid_size:
            decoded_path.append(position)
        else:
            break  # Out of bounds

    return decoded_path

def genetic_algorithm(grid, population_size=10, generations=50):
    population = initialize_population(population_size)

    for generation in range(generations):
        fitnesses = [evaluate_path(individual, grid) for individual in population]

        # Loops
        print(f"Generation {generation + 1}: Best fitness = {min(fitnesses)}")

        # Checkingif the goal is reached
        best_index = fitnesses.index(min(fitnesses))
        best_individual = population[best_index]
        if evaluate_path(best_individual, grid) == 0:
            print(f"Goal reached in generation {generation + 1}")
            decoded_path = decode_genome(best_individual)
            print_grid_with_path(grid, decoded_path)
            return decoded_path

        # Selection
        selected = tournament_selection(population, fitnesses)

        # Crossover and Mutation
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(selected, 2)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            if len(new_population) < population_size:
                new_population.append(mutate(child2))

        population = new_population

    # no path found
    print("No path found. Visualizing the best attempt:")
    best_index = fitnesses.index(min(fitnesses))
    best_individual = population[best_index]
    decoded_path = decode_genome(best_individual)
    print_grid_with_path(grid, decoded_path)
    return decoded_path


def Gen_algorithm(grid):
    start_time=time.time()
    path = genetic_algorithm(grid)

    if path:
        end_time=time.time()
        print(f"time taken for Genetic Algorithm to find path: {end_time-start_time} seconds")