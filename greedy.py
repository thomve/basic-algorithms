
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




def strong_password_checker(password: str) -> int:
    n = len(password)
    
    # Check presence of character types
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    missing_types = 3 - (has_lower + has_upper + has_digit)

    # Count sequences of 3+ repeating characters
    repeats = []
    i = 2
    while i < n:
        if password[i] == password[i - 1] == password[i - 2]:
            length = 2
            while i < n and password[i] == password[i - 1]:
                length += 1
                i += 1
            repeats.append(length)
        else:
            i += 1

    if n < 6:
        # Need to add characters to reach length 6
        return max(missing_types, 6 - n)

    elif n <= 20:
        # Only replacements needed to fix repeats
        replace = sum(length // 3 for length in repeats)
        return max(missing_types, replace)

    else:
        # Too long → must delete some characters
        delete = n - 20
        replace = 0

        # Optimize deletions by targeting repeats
        buckets = [0] * 3
        for length in repeats:
            buckets[length % 3] += 1

        # Delete 1 from sequences with (len % 3 == 0)
        for i in range(3):
            num = buckets[i]
            while delete > 0 and num > 0:
                if i == 0:
                    delete -= 1
                    num -= 1
                    buckets[i] -= 1
                elif i == 1 and delete >= 2:
                    delete -= 2
                    num -= 1
                    buckets[i] -= 1
                elif i == 2 and delete >= 3:
                    delete -= 3
                    num -= 1
                    buckets[i] -= 1
                else:
                    break

        # After deletions, calculate remaining replacements
        total_repeats = sum(buckets[0] + buckets[1] + buckets[2])
        replace = total_repeats

        return (n - 20) + max(missing_types, replace)