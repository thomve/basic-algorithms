from typing import List

def get_path(maze: List[List[int]]) -> List[List[int]]:
    if maze is None or len(maze) == 0:
        return None
    path = []
    failed_points = set()
    if get_path_helper(maze, len(maze) - 1, len(maze[0]) - 1, path, failed_points):
        return path
    return None

def get_path_helper(maze: List[List[int]], row: int, col: int, path: List[List[int]], failed_points: set) -> bool:
    if col < 0 or row < 0 or maze[row][col] == 1:
        return False
    point = [row, col]
    if point in failed_points:
        return False
    is_at_origin = row == 0 and col == 0
    if is_at_origin or get_path_helper(maze, row, col - 1, path, failed_points) or get_path_helper(maze, row - 1, col, path, failed_points):
        path.append(point)
        return True
    failed_points.add(point)
    return False