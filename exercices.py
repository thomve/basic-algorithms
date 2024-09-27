from typing import List


"""
word frequencies: design a method to find the frequency of occurrences of any given word in a book. What if we were running this algorithm multiple times?
"""
def setup_dictionnary(book: List[str]):
    table = {}
    for word in book:
        word = word.lower()
        if not word in table:
            table[word] = 0
        table[word] += 1
    return table

def get_frequency(table, word: str):
    if table is None or word is None:
        return -1
    word = word.lower()
    if word in table:
        return table[word]
    return 0

test_dict = setup_dictionnary(["hello", "world", "hello", "world", "world"])

print(test_dict)
print(get_frequency(test_dict, "hello"))