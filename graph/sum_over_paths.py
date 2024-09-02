class TreeNode:
    def __init__(self, data):
        self.__data: int = data
        self.left: TreeNode = None
        self.right: TreeNode = None
    
    def get_data(self) -> int:
        return self.__data

def count_path_with_sum(root: TreeNode, target_sum: int):
    return count_path_with_sum_helper(root, target_sum, 0, {})

def count_path_with_sum_helper(node: TreeNode, target_sum: int, running_sum: int, path_count: dict):
    if node is None:
        return 0
    
    running_sum += node.get_data()
    sum = running_sum - target_sum
    total_paths = path_count.get(sum, 0)
    
    if running_sum == target_sum:
        total_paths += 1
    
    increment_hash_table(path_count, running_sum, 1)
    total_paths += count_path_with_sum_helper(node.left, target_sum, running_sum, path_count)
    total_paths += count_path_with_sum_helper(node.right, target_sum, running_sum, path_count)
    increment_hash_table(path_count, running_sum, -1)
    
    return total_paths

def increment_hash_table(path_count: dict, key: int, delta: int):
    new_count = path_count.get(key, 0) + delta
    if new_count == 0:
        del path_count[key]
    else:
        path_count[key] = new_count

# Test the count_path_with_sum function
#               10
#              /  \
#             5   -3
#           / \    \
#          3   2   11
#         / \   \
#        3  -2   1
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)


target_sum = 8
result = count_path_with_sum(root, target_sum)
print(f"Number of paths with sum {target_sum}: {result}")