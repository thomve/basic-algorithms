from typing import List

def count_ways(n: int) -> int:
    memo = [-1] * (n + 1)
    return count_ways_memo(n, memo)

def count_ways_memo(n: int, memo: List[int]) -> int:
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = count_ways_memo(n - 1, memo) + count_ways_memo(n - 2, memo) + count_ways_memo(n - 3, memo)
        return memo[n]