from typing import Dict


def count_eval(s: str, result: bool, memo: Dict[str, int]) -> int:
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1 if bool(int(s)) == result else 0
    if memo.get(s) is not None:
        return memo[s]

    ways = 0
    for i in range(1, len(s), 2):
        c = s[i]
        left = s[:i]
        right = s[i + 1:]
        left_true = count_eval(left, True, memo)
        left_false = count_eval(left, False, memo)
        right_true = count_eval(right, True, memo)
        right_false = count_eval(right, False, memo)
        total: int = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        if c == "^":
            total_true = left_true * right_false + left_false * right_true
        elif c == "&":
            total_true = left_true * right_true
        elif c == "|":
            total_true = left_true * right_true + left_false * right_true + left_true * right_false
        
        sub_ways = total_true if result else (total - total_true)
        ways = ways + sub_ways
    
    memo[s] = ways