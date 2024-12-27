from problem_formulation import grid_size, initial_state, goal_state, print_grid_with_path, calculate_cost
import random
import time
from visualisation import visualize_grid_path

ACTIONS = ["north", "south", "west", "east"]

def get_next_state(state, action):
    x, y = state
    if action == "north":
        return (x - 1, y) if x > 0 else state
    elif action == "south":
        return (x + 1, y) if x < grid_size - 1 else state
    elif action == "west":
        return (x, y - 1) if y > 0 else state
    elif action == "east":
        return (x, y + 1) if y < grid_size - 1 else state
    return state

def is_valid_state(state, grid):
    x, y = state
    return 0 <= x < grid_size and 0 <= y < grid_size and grid[x][y] != "X"

def initialize_q_table():
    Q = {}
    for x in range(grid_size):
        for y in range(grid_size):
            for action in ACTIONS:
                Q[((x, y), action)] = 0.0
    return Q

def choose_action(state, Q, epsilon):
    if random.uniform(0, 1) < epsilon:
        return random.choice(ACTIONS)  # Explore
    else:
        # Exploit: Choose action with the highest Q-value
        q_values = {action: Q[(state, action)] for action in ACTIONS}
        return max(q_values, key=q_values.get)

def q_learning_algorithm(grid, alpha=0.1, gamma=0.9, epsilon=0.1, episodes=500):
    Q = initialize_q_table()
    start_time = time.time()

    for episode in range(episodes):
        state = initial_state
        path = []

        while state != goal_state:
            action = choose_action(state, Q, epsilon)
            next_state = get_next_state(state, action)

            if not is_valid_state(next_state, grid):
                reward = -1.0  # Penalty for hitting an obstacle or invalid move
                next_state = state  # Stay in the same state
            elif next_state == goal_state:
                reward = 100.0  # Reward for reaching the goal
            else:
                reward = -1.0  # Step cost

            # Ensure Q-value lookup is numeric
            max_next_q = max(float(Q[(next_state, a)]) for a in ACTIONS)
            current_q_value = Q[(state, action)]  # Current Q-value

            # Debugging output
            print(f"Episode: {episode}, State: {state}, Action: {action}")
            print(f"Reward: {reward}, Max Next Q: {max_next_q}, Current Q: {current_q_value}")
            print(f"Update: alpha * (reward + gamma * max_next_q - current_q_value)")

            # Update Q-value
            Q[(state, action)] += alpha * (reward + gamma * max_next_q - current_q_value)

            path.append(state)
            state = next_state

        # Optional: Decay epsilon over time to reduce exploration
        epsilon = max(0.01, epsilon * 0.99)

        # Visualize the path at the end of each episode (optional)
        visualize_grid_path(grid, path, initial_state, goal_state, f"Q-Learning Episode {episode + 1}")

    # Extract the optimal path
    state = initial_state
    path = []
    while state != goal_state:
        action = max(ACTIONS, key=lambda a: Q[(state, a)])
        path.append(state)
        state = get_next_state(state, action)

    path.append(goal_state)
    end_time = time.time()

    total_cost = calculate_cost(path)
    print("\nPath to goal found:")
    print_grid_with_path(grid, path)
    print("Path taken:", path)
    print(f"Time taken for Q-learning: {end_time - start_time} seconds")
    print(f"Total cost: {total_cost}")

    # Final visualization of the optimal path
    visualize_grid_path(grid, path, initial_state, goal_state, "Optimal Path Found by Q-Learning")

    return path, end_time - start_time, total_cost