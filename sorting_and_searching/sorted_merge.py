from typing import List


def merge(a: List[int], b: List[int], count_a: int, count_b: int):
    index_a = count_a - 1
    index_b = count_b - 1
    index_merged = count_a + count_b - 1

    while index_b >= 0:
        if index_a >= 0 and a[index_a] > b[index_b]:
            a[index_merged] = a[index_a]
            index_a -= 1
        else:
            a[index_merged] = b[index_b]
            index_b -= 1
        index_merged -= 1
    
    return a

print(merge([1, 3, 5, 7, 0, 0, 0, 0], [2, 4, 6, 8], 4, 4)) # [1, 2, 3, 4, 5, 6, 7, 8]