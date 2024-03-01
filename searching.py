import random 
import time

def linear_search(arr, target):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """
    Time complexity: O(logn)
    Space complexity: O(1)
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def interpolation_search(arr, target):
    """
    Time complexity: O(log logn) but can degrade to O(n) in the worst case
    Space complexity: O(1)
    """
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        mid = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr_size = 1000
random_arr = [random.randint(0, 1000) for _ in range(arr_size)]


sorting_algorithms = {
    "linear_search": linear_search,
    "binary_search": binary_search,
    "interpolation_search": interpolation_search,
}

def monitor_searching_algorithm(algorithm, arr, target):
    start_time = time.time()
    idx = algorithm(arr.copy(), target)
    end_time = time.time()
    execution_time = end_time - start_time
    return idx, execution_time

for algorithm_name, algorithm_func in sorting_algorithms.items():
    idx, execution_time = monitor_searching_algorithm(algorithm_func, random_arr, 20)
    print(f"{algorithm_name}: Execution Time - {execution_time:.6f} seconds")
    if idx != -1:
        print(f"Found value at idx {idx}")


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hashed_key = self._hash(key)
        for pair in self.table[hashed_key]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[hashed_key].append([key, value])

    def search(self, key):
        hashed_key = self._hash(key)
        for pair in self.table[hashed_key]:
            if pair[0] == key:
                return pair[1]
        return None


hash_table = HashTable(10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 7)
print("hash table search for apple:", hash_table.search("apple"))
print("hash table search for banana:", hash_table.search("banana"))


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

# Prefix tree
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word


trie = Trie()
words = ["apple", "banana", "app"]
for word in words:
    trie.insert(word)
print("Trie search for apple:", trie.search("apple"))
print("Trie search for app:", trie.search("app"))
print("Trie search for orange:", trie.search("orange"))


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Binary search tree
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if not node:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return node

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if not node:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)


bst = BST()
keys = [5, 3, 7, 1, 4, 6, 8]
for key in keys:
    bst.insert(key)
print("BST search for number 3", bst.search(3))
print("BST search for number 10", bst.search(10))