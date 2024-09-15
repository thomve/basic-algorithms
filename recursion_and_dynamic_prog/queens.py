from typing import List
import unittest


GRID_SIZE: int = 8

def place_queens(row: int, columns: List[int], results: List[List[int]]):
    if row == GRID_SIZE:
        results.append(columns.copy())
    else:
        for col in range(GRID_SIZE):
            if check_valid(columns, row, col):
                columns[row] = col
                place_queens(row + 1, columns, results)

def check_valid(columns: List[int], row1: int, col1: int):
    for row2 in range(row1):
        col2 = columns[row2]
        if col1 == col2:
            return False
        col_distance = abs(col2 - col1)
        row_distance = row1 - row2
        if col_distance == row_distance:
            return False
    return True


class TestQueens(unittest.TestCase):
    def test_place_queens(self):
        results = []
        place_queens(0, [-1] * 8, results)
        self.assertEqual(len(results), 92)
        for solution in results:
            self.assertTrue(self.is_valid_solution(solution))

    def is_valid_solution(self, solution):
        for row1 in range(len(solution)):
            for row2 in range(row1 + 1, len(solution)):
                col1 = solution[row1]
                col2 = solution[row2]
                if col1 == col2:
                    return False
                if abs(col1 - col2) == abs(row1 - row2):
                    return False
        return True

if __name__ == '__main__':
    unittest.main()