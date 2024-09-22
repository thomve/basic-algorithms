from typing import List


def search(listy: List[int], value: int):
    index: int = 1
    while listy[index] != -1 and listy[index] < value:
        index *= 2
    return binary_search(listy, value, index // 2, index)

def binary_search(listy: List[int], value: int, low: int, high: int):
    while low <= high:
        mid = (low + high) // 2
        middle = listy[mid]
        if middle > value or middle == -1:
            high = mid - 1
        elif middle < value:
            low = mid + 1
        else:
            return mid
    return -1

listy = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
value_to_search = 15
result = search(listy, value_to_search)
print(f"Index of {value_to_search} in listy: {result}")