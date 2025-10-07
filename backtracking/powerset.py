from typing import List

def find_powerset(nums: List[int]):
    res = []
    subset = []

    # backtracking
    def dfs(start):
        res.append(subset[:])

        for i in range(start, len(nums)):
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

    dfs(0)
    return res