from typing import List, Dict

class Box:
    def __init__(self, width: int, height: int, depth: int):
        self.width = width
        self.height = height
        self.depth = depth

    def can_be_above(self, other: 'Box') -> bool:
        return other is None or (self.width < other.width and self.height < other.height and self.depth < other.depth)

    def __str__(self):
        return f'Box({self.width}, {self.height}, {self.depth})'

    def __repr__(self):
        return str(self)


def create_stack(boxes: List[Box]) -> int:
    return create_stack_helper(boxes, None, 0, {})

def create_stack_helper(boxes: List[Box], bottom: Box, offset: int, memo: Dict[int, int]) -> int:
    if offset >= len(boxes):
        return 0

    # height with this bottom
    new_bottom = boxes[offset]
    height_with_bottom = 0
    if bottom is None or new_bottom.can_be_above(bottom):
        if memo.get(offset) is None:
            memo[offset] = create_stack_helper(boxes, new_bottom, offset + 1, memo)
            memo[offset] += new_bottom.height
        height_with_bottom = memo[offset]

    # without this bottom
    height_without_bottom = create_stack_helper(boxes, bottom, offset + 1, memo)

    return max(height_with_bottom, height_without_bottom)


print(create_stack([Box(1, 1, 1), Box(2, 2, 2), Box(3, 3, 3)]))