from typing import List

def check_duplicates(array: List[int]):
    bitset = Bitset(32000)
    for i in array:
        if bitset.get(i - 1):
            print(i)
        else:
            bitset.set(i - 1)

class Bitset:
    def __init__(self, size: int):
        self.bitset = [0] * (size // 32 + 1)
    
    def get(self, index: int) -> bool:
        word_number = index // 32
        bit_number = index % 32
        return (self.bitset[word_number] & (1 << bit_number)) != 0
    
    def set(self, index: int):
        word_number = index // 32
        bit_number = index % 32
        self.bitset[word_number] |= 1 << bit_number

print(check_duplicates([1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 10])) # 4, 10