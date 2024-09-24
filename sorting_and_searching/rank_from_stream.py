class RankNode:
    def __init__(self, data):
        self.data = data
        self.left_size = 0
        self.left = None
        self.right = None

    def insert(self, data):
        if data <= self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = RankNode(data)
            self.left_size += 1
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = RankNode(data)

    def get_rank(self, data):
        if data == self.data:
            return self.left_size
        elif data < self.data:
            if self.left:
                return self.left.get_rank(data)
            else:
                return -1
        else:
            right_rank = -1 if self.right is None else self.right.get_rank(data)
            if right_rank == -1:
                return -1
            return self.left_size + 1 + right_rank

root: RankNode = None

def track(number: int):
    global root
    if root is None:
        root = RankNode(number)
    else:
        root.insert(number)

def get_rank_of_number(number: int):
    global root
    return root.get_rank(number)

track(5)
track(1)
track(4)
track(4)
track(5)
track(9)
track(7)
track(13)
track(3)

print(get_rank_of_number(1))  # Output: 0
print(get_rank_of_number(3))  # Output: 1
print(get_rank_of_number(4))  # Output: 3
print(get_rank_of_number(13))  # Output: 6