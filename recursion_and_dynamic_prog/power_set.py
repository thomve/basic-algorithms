from typing import List

def get_subsets(set: List[int]) -> List[List[int]]:
    all_subsets = []
    max: int = 1 << len(set)
    for i in range(max):
        subset = convert_int_to_set(i, set)
        all_subsets.append(subset)
    return all_subsets

def convert_int_to_set(x: int, set: List[int]) -> List[int]:
    subset = []
    index = 0
    k = x
    while k > 0:
        if k & 1 == 1:
            subset.append(set[index])
        k >>= 1
        index += 1
    return subset

print(get_subsets([1, 2, 3])) # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]