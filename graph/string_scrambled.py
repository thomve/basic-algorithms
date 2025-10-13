def is_scramble(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False

    memo = {}

    def dfs(a, b):
        if (a, b) in memo:
            return memo[(a, b)]
        if a == b:
            memo[(a, b)] = True
            return True
        if sorted(a) != sorted(b):
            memo[(a, b)] = False
            return False

        n = len(a)
        for i in range(1, n):
            # Case 1: No swap
            if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                memo[(a, b)] = True
                return True
            # Case 2: Swap
            if dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i]):
                memo[(a, b)] = True
                return True

        memo[(a, b)] = False
        return False

    return dfs(s1, s2)
