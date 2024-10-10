from typing import List
import heapq

"""
word frequencies: design a method to find the frequency of occurrences of any given word in a book. What if we were running this algorithm multiple times?
"""
print("Exercice 1: Word Frequencies")
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


"""
Intersection    
"""
print("Exercice 2: Intersection")
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        if self.start.x == self.end.x:
            self.slope = float('inf')
            self.y_intercept = float('infg')
        else:
            self.slope = (self.end.y - self.start.y) / (self.end.x - self.start.x)
            self.y_intercept = self.end.y - self.slope * self.end.x
    
    def is_vertical(self):
        return self.slope == float('inf')

    def get_y_from_x(self, x: float):
        if self.is_vertical():
            return float('inf')
        return self.slope * x + self.y_intercept
    
def is_between_helper(start: float, middle: float, end: float):
    if start > end:
        return end <= middle and middle <= start
    else:
        return start <= middle and middle <= end
    
def is_between(start: Point, middle: Point, end: Point):
    return is_between_helper(start.x, middle.x, end.x) and is_between_helper(start.y, middle.y, end.y)

def intersection(start1: Point, end1: Point, start2: Point, end2: Point):
    line1 = Line(start1, end1)
    line2 = Line(start2, end2)
    
    if line1.slope == line2.slope:
        if line1.y_intercept != line2.y_intercept:
            return None
        if is_between(start1, start2, end1):
            return start2
        elif is_between(start1, end2, end1):
            return end2
        elif is_between(start2, start1, end2):
            return start1
        elif is_between(start2, end1, end2):
            return end1
        else:
            return None
        
    x: float = 0.
    if line1.is_vertical() or line2.is_vertical():
        if line1.is_vertical():
            x = start1.x
        else:
            x = start2.x
    else:
        x = (line2.y_intercept - line1.y_intercept) / (line1.slope - line2.slope)

    y = line2.get_y_from_x(x) if line1.is_vertical() else line1.get_y_from_x(x)

    intersection = Point(x, y)
    if is_between(start1, intersection, end1) and is_between(start2, intersection, end2):
        return intersection

    return None

intersection_point = intersection(Point(0, 0), Point(1, 1), Point(0, 1), Point(1, 0))

print(intersection_point.x, intersection_point.y) # 0.5, 0.5

"""
Exercice 3: smallest difference
"""
print("Exercice 3: Smallest Difference")

def find_smallest_difference(array1: List[int], array2: List[int]):
    if array1 is None or array2 is None or len(array1) == 0 or len(array2) == 0:
        return -1
    array1.sort()
    array2.sort()
    i = 0
    j = 0
    smallest_difference = float('inf')
    while i < len(array1) and j < len(array2):
        difference = abs(array1[i] - array2[j])
        if difference < smallest_difference:
            smallest_difference = difference
        if array1[i] < array2[j]:
            i += 1
        else:
            j += 1
    return smallest_difference

print(find_smallest_difference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8])) # 3


"""
Exercice 4: get max
"""
print("Exercice 4: Get Max")
def flip(bit: int):
    return 1 ^ bit

def sign(a: int):
    return flip((a >> 31) & 0x1)

def get_max(a: int, b: int):
    c: int = a - b
    sa: int = sign(a)
    sb: int = sign(b)
    sc: int = sign(c)
    use_sign_of_a: int = sa ^ sb
    use_sign_of_c: int = flip(sa ^ sb)
    k = use_sign_of_a * sa + use_sign_of_c * sc
    q = flip(k)
    return a * k + b * q

print(get_max(15, 20)) # 20

"""
Exercice 5: Diving board
"""
print("Exercice 5: Diving Board")

def get_all_lengths(k: int, shorter: int, longer: int):
    lengths: set = set()
    visited: set = set()
    get_all_lengths_helper(k, 0, shorter, longer, lengths, visited)
    return lengths

def get_all_lengths_helper(k: int, total: int, shorter: int, longer: int, lengths: set, visited: set):
    if k == 0:
        lengths.add(total)
        return
    key: str = str(k) + " " + str(total)
    if key in visited:
        return
    get_all_lengths_helper(k - 1, total + shorter, shorter, longer, lengths, visited)
    get_all_lengths_helper(k - 1, total + longer, shorter, longer, lengths, visited)
    visited.add(key)

print(get_all_lengths(3, 2, 3)) # {6, 7, 8, 9}-


"""
Exeruce 6: master mind
"""
print("Exercice 6: Master Mind")

class Result:
    def __init__(self):
        self.hits = 0
        self.pseudo_hits = 0

    def to_string(self):
        return "Hits: " + str(self.hits) + ", Pseudo Hits: " + str(self.pseudo_hits)
    

def code_helper(char: str):
    if char == 'B':
        return 0
    if char == 'G':
        return 1
    if char == 'R':
        return 2
    if char == 'Y':
        return 3
    return -1

MAX_COLORS = 4

def estimate(guess: str, solution: str):
    if len(guess) != len(solution):
        return None

    result = Result()
    frequencies = [0] * MAX_COLORS
    for i in range(len(guess)):
        if guess[i] == solution[i]:
            result.hits += 1
        else:
            code = code_helper(guess[i])
            frequencies[code] += 1

    for i in range(len(guess)):
        code = code_helper(guess[i])
        if code >= 0 and frequencies[code] > 0 and guess[i] != solution[i]:
            result.pseudo_hits += 1
            frequencies[code] -= 1
    return result

print(estimate("GGRR", "RGBY").to_string())


"""
Exercice 7: Pattern matching
"""
print("Exercice 7: Pattern Matching")

def does_match(pattern: str, value: str):
    if len(pattern) == 0:
        return len(value) == 0
    main_char = pattern[0]
    alt_char = 'B' if main_char == 'A' else 'A'
    size = len(value)
    count_main = count_of(pattern, main_char)
    count_alt = len(pattern) - count_main
    first_alt = pattern.find(alt_char)
    max_main_size = size // count_main
    for main_size in range(max_main_size):
        remaining_length = size - main_size * count_main
        first: str = value[:main_size]
        if count_alt == 0 or remaining_length % count_alt == 0:
            alt_index = first_alt * main_size
            alt_size = 0 if count_alt == 0 else remaining_length // count_alt
            second = "" if count_alt == 0 else value[alt_index: alt_index + alt_size]
            candidate = build_from_pattern(pattern, first, second)
            if candidate == value:
                return True
    return False
            
def build_from_pattern(pattern: str, main: str, alt: str):
    main_char = pattern[0]
    result = ""
    for c in pattern:
        if c == main_char:
            result += main
        else:
            result += alt
    return result

def count_of(pattern: str, c: str):
    count: int = 0
    for i in range(len(pattern)):
        if pattern[i] == c:
            count += 1
    return count

print(does_match("ABBA", "catdogdogcat")) # True
print(does_match("ABAB", "catdogdogcat")) # True


"""
Exercice 8: Sum swap
"""
print("Exercice 8: Sum Swap")
def find_swap_values(array1: List[int], array2: List[int]):
    target: int = get_target(array1, array2)
    if target is None:
        return None
    return find_difference(array1, array2, target)

def get_target(array1: List[int], array2: List[int]):
    sum1: int = sum(array1)
    sum2: int = sum(array2)
    if (sum1 - sum2) % 2 != 0:
        return None
    return (sum1 - sum2) // 2

def find_difference(array1: List[int], array2: List[int], target: int):
    contents2 = get_content(array2)
    for one in array1:
        two = one - target
        if two in contents2:
            return one, two

def get_content(array: List[int]):
    seta = set()
    for a in array:
        seta.add(a)
    return seta

print(find_swap_values([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]))


"""
Exercice 9: add without plus
"""
print("Exercice 9: Add without plus")
def add(a: int, b: int):
    if b == 0:
        return a
    sum = a ^ b
    carry = (a & b) << 1
    return add(sum, carry)

print(add(5, 3)) # 8

"""
Exercice 10: shuffle
"""
from random import randint
print("Exercice 10: Shuffle")
def shuffle(cards: List[int], i: int):
    if i == 0:
        return cards
    shuffle(cards, i - 1)
    k = randint(0, i)
    temp  = cards[k]
    cards[k] = cards[i]
    cards[i] = temp

    return cards

print(shuffle([1, 2, 3, 4, 5], 4))

"""
Exercice 11: Random set
"""
print("Exercice 11: Random Set")

def random_set(original: List[int], m: int, i: int):
    if i+1 < m:
        return None
    elif i+1 == m:
        return original[:m]
    else:
        _set = random_set(original, m, i-1)
        rand = randint(0, i)
        if rand < m:
            _set[rand] = original[i]
        return _set

print(random_set([1, 2, 3, 4, 5], 3, 4))

"""
Exercice 12: Letters & numbers
"""
print("Exercice 12: Letters & Numbers")

def compute_delta_arrays(array: List[str]):
    deltas = []
    delta = 0
    for i in range(len(array)):
        if array[i].isdigit():
            delta -= 1
        else:
            delta += 1
        deltas.append(delta)
    return deltas

def find_longest_match(deltas: List[str]):
    map = {0: -1}
    max = [0, 0]
    for i in range(len(deltas)):
        if not deltas[i] in map:
            map[deltas[i]] = i
        else:
            match = map[deltas[i]]
            distance = i - match
            longest = max[1] - max[0]
            if distance > longest:
                max = [match, i]
    return max

def extract(array: List[str], start: int, end: int):
    sub_array = [0] * (end - start)
    for i in range(start, end):
        sub_array[i - start] = array[i]
    return sub_array

def find_longest_subarray(array: List[str]):
    deltas = compute_delta_arrays(array)
    match = find_longest_match(deltas)
    return extract(array, match[0] + 1, match[1])


print(find_longest_subarray(["a", "1", "2", "b", "c", "d", "e", "f", "5", "6", "7", "g"]))

"""
Exercice 13: Majority element
"""
print("Exercice 13: Majority Element")

def get_candidate(array: List[int]):
    majority = 0
    count = 0
    for n in array:
        if count == 0:
            majority = n
        if n == majority:
            count += 1
        else:
            count -= 1
    return majority

def validate(array: List[int], majority: int):
    count = 0
    for n in array:
        if n == majority:
            count += 1
    return count > len(array) // 2

def get_majority_element(array: List[int]):
    candidate = get_candidate(array)
    return candidate if validate(array, candidate) else None

print(get_majority_element([1, 2, 5, 9, 5, 9, 5, 5, 5])) # 5


"""
Exercice 14: Smallest K
"""
print("Exercice 14: Smallest K")

def find_smallest_k(arr, k):
    if k >= len(arr):
        return sorted(arr)

    max_heap = [-arr[i] for i in range(k)]
    heapq.heapify(max_heap)

    for i in range(k, len(arr)):
        if -arr[i] > max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -arr[i])

    smallest_k = [-heapq.heappop(max_heap) for _ in range(len(max_heap))]

    return smallest_k[::-1]
    

print(find_smallest_k([10, 2, 3, 13, 6, 7, 8, 9], 5))

"""
Exercice 15: The Masseuse
"""
print("Exercice 15: The Masseuse")

def max_minutes(massages: List[int]):
    memo = [-1] * len(massages)
    return max_minutes_helper(massages, 0, memo)

def max_minutes_helper(massages: List[int], index: int, memo: List[int]):
    if index >= len(massages):
        return 0
    if memo[index] == -1:
        best_with = massages[index] + max_minutes_helper(massages, index + 2, memo)
        best_without = max_minutes_helper(massages, index + 1, memo)
        memo[index] = max(best_with, best_without)
    return memo[index]

print(max_minutes([30, 15, 60, 75, 45, 15, 15, 45])) # 180


"""
Exercice 16: Volume of histogram
"""
print("Exercice 16: Volume of histogram")

def compute_volume(histogram: List[int]):
    left_maxes = [0] * len(histogram)
    left_max = 0
    for i in range(len(histogram)):
        left_max = max(left_max, histogram[i])
        left_maxes[i] = left_max
    sum = 0
    right_max = 0
    for i in range(len(histogram) - 1, -1, -1):
        right_max = max(right_max, histogram[i])
        second_tallest = min(right_max, left_maxes[i])
        if second_tallest > histogram[i]:
            sum += second_tallest - histogram[i]
    return sum

print(compute_volume([0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0])) # 26

"""
Exercice 17: Max submatrix
"""
print("Exercice 17: Max submatrix")

class SubMatrix:
    def __init__(self, r1: int, r2: int, c1: int, c2: int, sum: int):
        self.r1 = r1
        self.r2 = r2
        self.c1 = c1
        self.c2 = c2
        self.sum = sum

def getMaxMatrix(matrix: List[List[int]]):
    rowCount = len(matrix)
    colCount = len(matrix[0])
    best = None
    for rowStart in range(rowCount):
        partialSum = [0] * colCount
        for rowEnd in range(rowStart, rowCount):
            for i in range(colCount):
                partialSum[i] += matrix[rowEnd][i]
            best = max_sum_subarray(partialSum, best, rowStart, rowEnd)
    return best

def max_sum_subarray(partialSum: List[int], best: SubMatrix, rowStart: int, rowEnd: int):
    colCount = len(partialSum)
    sum = 0
    start = 0
    best_sub = None
    for i in range(colCount):
        sum += partialSum[i]
        if sum < 0:
            sum = 0
            start = i + 1
        elif best_sub is None or sum > best_sub.sum:
            best_sub = SubMatrix(rowStart, rowEnd, start, i, sum)
    if best is None or best_sub.sum > best.sum:
        return best_sub
    return best

print(getMaxMatrix([[9, -8, 1, 3, -2], [-3, 7, 6, -2, 4], [6, -4, -4, 8, -7]]).sum) # 19
