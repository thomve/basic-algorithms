
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

