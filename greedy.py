
def activity_selection(start, finish):
    n = len(start)
    activities = []
    activities.append(0)
    j = 0
    for i in range(1, n):
        if start[i] >= finish[j]:
            activities.append(i)
            j = i
    return activities

start_times = [1, 3, 3, 2, 5, 2]
finish_times = [2, 4, 1, 5, 2, 9]
print(activity_selection(start_times, finish_times))


def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    knapsack = []

    for value, weight in items:
        if capacity == 0:
            break
        elif weight <= capacity:
            knapsack.append((value, weight))
            total_value += value
            capacity -= weight
        else:
            fraction = capacity / weight
            knapsack.append((value * fraction, weight * fraction))
            total_value += value * fraction
            capacity = 0

    return total_value, knapsack

items = [(60, 10), (100, 20), (120, 30)]  # Format: (value, weight)
capacity = 50
max_value, selected_items = fractional_knapsack(items, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
