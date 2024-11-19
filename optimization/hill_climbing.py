import random

def hill_climbing(objective_function, x_start, step_size, max_iterations):
    current_x = x_start
    current_y = objective_function(current_x)

    for iteration in range(max_iterations):
        step = random.uniform(-step_size, step_size)
        new_x = current_x + step
        new_y = objective_function(new_x)

        if new_y > current_y:
            current_x, current_y = new_x, new_y
            print(f"Iteration {iteration + 1}: Found better solution: x = {current_x}, y = {current_y}")

    return current_x, current_y

def objective_function(x):
    return -(x**2) + 9

x_start = random.uniform(-10, 10)
step_size = 0.1
max_iterations = 500

best_x, best_y = hill_climbing(objective_function, x_start, step_size, max_iterations)
print(f"Best solution found: x = {best_x}, y = {best_y}")
