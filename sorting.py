import random
import time


def bubble_sort(arr):
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def merge_sort(arr):
    """
    Time complexity: O(n logn)
    Space complexity: O(logn)
    """
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    """
    Time complexity: O(n logn)
    Space complexity: O(logn)
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Time complexity: O(n logn)
    Space complexity: O(1)
    """
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


def monitor_sorting_algorithm(algorithm, arr):
    start_time = time.time()
    sorted_arr = algorithm(arr.copy())
    end_time = time.time()
    execution_time = end_time - start_time
    return sorted_arr, execution_time


arr_size = 1000
random_arr = [random.randint(0, 1000) for _ in range(arr_size)]

sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort
}

for algorithm_name, algorithm_func in sorting_algorithms.items():
    sorted_arr, execution_time = monitor_sorting_algorithm(algorithm_func, random_arr)
    print(f"{algorithm_name}: Execution Time - {execution_time:.6f} seconds")