BREAKING_POINT: int = 46
COUNT_DROP: int = 0

def drop(floor: int):
    global COUNT_DROP
    COUNT_DROP = COUNT_DROP + 1
    return floor >= BREAKING_POINT

def find_breaking_point(floors: int):
    # interval n is defined by n(n+1) / 2 = floors
    interval: int = 14 # supposing floors = 100
    previous_floor: int = 0
    egg1: int = interval
    while not drop(egg1) and egg1 <= floors:
        interval -= 1
        previous_floor = egg1
        egg1 += interval
    egg2: int = previous_floor + 1
    while egg2 < egg1 and egg2 <= floors and not drop(egg2):
        egg2 += 1
    return egg2 if egg2 <= floors else -1

floors: int = 100
print(find_breaking_point(floors))