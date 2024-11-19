import math
import random

def simulated_annealing(objective_function, x_start, initial_temp, cooling_rate, min_temp, max_iterations):
    current_x = x_start
    current_y = objective_function(current_x)
    best_x, best_y = current_x, current_y
    temperature = initial_temp

    for iteration in range(max_iterations):
        if temperature <= min_temp:
            break

        new_x = current_x + random.uniform(-1, 1)
        new_y = objective_function(new_x)

        delta_y = new_y - current_y

        if delta_y < 0 or random.uniform(0, 1) < math.exp(-delta_y / temperature):
            current_x, current_y = new_x, new_y
            if current_y < best_y:
                best_x, best_y = current_x, current_y

        temperature *= cooling_rate

    return best_x, best_y


def objective_function(x):
    return (x - 2)**2 + 1

x_start = random.uniform(-10, 10)
initial_temp = 1000
cooling_rate = 0.95
min_temp = 1e-3
max_iterations = 1000

best_x, best_y = simulated_annealing(objective_function, x_start, initial_temp, cooling_rate, min_temp, max_iterations)
print(f"Best solution found: x = {best_x}, y = {best_y}")
