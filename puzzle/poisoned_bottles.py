from typing import List

class Bottle:
    def __init__(self, id: int):
        self.id = id
        self.poisoned = False
    
    def set_as_poisoned(self):
        self.poisoned = True
    
class TestStrip:
    days_to_results: int = 7

    def __init__(self, id: int):
        self.id = id
        self.drops_by_day = []
    
    def size_drops_for_day(self, day: int) -> int:
        while len(self.drops_by_day) <= day:
            self.drops_by_day.append([])
    
    def has_poison(self, bottles: List[Bottle]) -> bool:
        for bottle in bottles:
            if bottle.poisoned:
                return True
        return False

    def add_drop_on_day(self, day: int, bottle: Bottle):
        self.size_drops_for_day(day)
        drops = self.drops_by_day[day]
        drops.append(bottle)

    def is_positive_on_day(self, day: int) -> bool:
        test_day = day - self.days_to_results
        if test_day < 0 or test_day >= len(self.drops_by_day):
            return False
        for d in range(test_day):
            bottles = self.drops_by_day[d]
            if self.has_poison(bottles):
                return True
        return False

def find_poisoned_bootle(bottles: List[Bottle], strips: List[TestStrip]) -> int:
    run_tests(bottles, strips)
    positive = get_positive_on_day(strips, 7)
    return set_bits(positive)

def run_tests(bottles: List[Bottle], test_strips: List[TestStrip]):
    for bottle in bottles:
        id = bottle.id
        bit_index = 0
        while id > 0:
            if id & 1 == 1:
                test_strips[bit_index].add_drop_on_day(0, bottle)
            bit_index += 1
            id >>= 1

def get_positive_on_day(test_strips: List[TestStrip], day: int) -> int:
    positive: list = []
    for strip in test_strips:
        id = strip.id
        if strip.is_positive_on_day(day):
            positive.append(id)
    return positive

def set_bits(positive: List[int]) -> int:
    id: int = 0
    for bit_index in positive:
        id |= 1 << bit_index
    return id