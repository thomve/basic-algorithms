def get_permutations(s: str):
    if s is None:
        return None
    permutations = []
    if len(s) == 0:
        permutations.append("")
        return permutations
    first = s[0]
    remainder = s[1:]
    words = get_permutations(remainder)
    for word in words:
        for j in range(len(word) + 1):
            permutations.append(insert_char_at(word, first, j))
    return permutations


def insert_char_at(word: str, c: str, i: int) -> str:
    start = word[:i]
    end = word[i:]
    return start + c + end

print(get_permutations("abc")) # ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']