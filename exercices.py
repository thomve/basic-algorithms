from typing import List


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