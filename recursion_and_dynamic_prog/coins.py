from typing import List

def make_change(amount: int, denoms: List[int]):
    return make_change_helper(amount, denoms, 0, {})

def make_change_helper(amount: int, denoms: List[int], index: int, memo: dict):
    if amount == 0:
        return 1
    if index >= len(denoms):
        return 0
    if (amount, index) in memo:
        return memo[(amount, index)]
    denom_amount = denoms[index]
    ways = 0
    i = 0
    while i * denom_amount <= amount:
        amount_remaining = amount - i * denom_amount
        ways += make_change_helper(amount_remaining, denoms, index + 1, memo)
        i += 1
    memo[(amount, index)] = ways
    return ways

print(make_change(100, [25, 10, 5, 1])) # 242