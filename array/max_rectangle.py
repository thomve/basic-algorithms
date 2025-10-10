from typing import List



def maximum_rectangle(matrix: List[List[str]]):
    """
    Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
    """
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for row in matrix:
        for i in range(cols):
            heights[i] = heights[i] + 1 if row[i] == '1' or row[i] == 1 else 0

        stack = []
        for i in range(cols + 1):
            curr_height = heights[i] if i < cols else 0
            while stack and curr_height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

    return max_area