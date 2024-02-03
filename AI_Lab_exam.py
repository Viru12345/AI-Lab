from collections import deque

def get_possible_moves(state):
    """Generate all possible next states from the current state."""
    capacities = (12, 8, 5)  # Max capacities of the containers
    moves = []
    for i in range(3):
        for j in range(3):
            if i != j:
                # Calculate the amount to transfer
                transfer_amount = min(state[i], capacities[j] - state[j])
                if transfer_amount > 0:
                    new_state = list(state)
                    new_state[i] -= transfer_amount
                    new_state[j] += transfer_amount
                    moves.append(tuple(new_state))
    return moves

def bfs(start, goal):
    """Perform BFS to find the path from start to goal."""
    queue = deque([(start, [start])])  # Queue of (state, path) tuples
    seen = set([start])

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal:
            return path  # Return the path to reach the goal

        for next_state in get_possible_moves(current_state):
            if next_state not in seen:
                queue.append((next_state, path + [next_state]))
                seen.add(next_state)
    return None  # If no path is found

# Define the start and goal states
start_state = (12, 0, 0)
goal_state = (6, 6, 0)

# Find the path using BFS
path = bfs(start_state, goal_state)

# Print the path from start to goal
if path:
    for step in path:
        print(step)
else:
    print("No path found.")
