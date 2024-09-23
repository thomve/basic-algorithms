class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return f"({self.row}, {self.col})"
    
    def in_bounds(self, matrix):
        return 0 <= self.row < len(matrix) and 0 <= self.col < len(matrix[0])
    
    def is_before(self, p):
        return self.row <= p.row and self.col <= p.col
    
    def clone(self):
        return Coordinate(self.row, self.col)
    
    def set_to_average(self, min: 'Coordinate', max: 'Coordinate'):
        self.row = (min.row + max.row) // 2
        self.col = (min.col + max.col) // 2
    
def find_element(matrix, origin, dest, x):
    if not origin.in_bounds(matrix) or not dest.in_bounds(matrix):
        return None
    if matrix[origin.row][origin.col] == x:
        return origin
    elif not origin.is_before(dest):
        return None
    
    start = origin.clone()
    diag_dist = min(dest.row - origin.row, dest.col - origin.col)
    end = Coordinate(start.row + diag_dist, start.col + diag_dist)
    p = Coordinate(0, 0)
    while start.is_before(end) and p != end:
        p.set_to_average(start, end)
        if x > matrix[p.row][p.col]:
            start.row = p.row + 1
            start.col = p.col + 1
        else:
            end.row = end.row - 1
            end.col = end.col - 1
    
    return partition_and_search(matrix, origin, dest, start, x)

def partition_and_search(matrix, origin, dest, pivot, x):
    lower_left_origin = Coordinate(pivot.row, origin.col)
    lower_left_dest = Coordinate(dest.row, pivot.col - 1)
    upper_right_origin = Coordinate(origin.row, pivot.col)
    upper_right_dest = Coordinate(pivot.row - 1, dest.col)

    lower_left = find_element(matrix, lower_left_origin, lower_left_dest, x)

    if lower_left is None:
        return find_element(matrix, upper_right_origin, upper_right_dest, x)

    return lower_left

def find_element_in_matrix(matrix, x):
    origin = Coordinate(0, 0)
    dest = Coordinate(len(matrix) - 1, len(matrix[0]) - 1)
    return find_element(matrix, origin, dest, x)

print(find_element_in_matrix([[15, 20, 40, 85], [20, 35, 80, 95], [30, 55, 95, 105], [40, 80, 100, 120]], 55)) # (2, 1)