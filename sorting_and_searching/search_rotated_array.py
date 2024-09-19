from typing import List


def search(a: List[int], target: int):
    return search_helper(a, 0, len(a) - 1, target)

def search_helper(a: List[int], left: int, right: int, target: int):
    if right < left:
        return -1
    mid = (left + right) // 2
    if target == a[mid]:
        return mid
    
    if a[left] < a[mid]:
        if a[left] <= target < a[mid]:
            return search_helper(a, left, mid - 1, target)
        else:
            return search_helper(a, mid + 1, right, target)
    elif a[mid] < a[right]:
        if a[mid] < target <= a[right]:
            return search_helper(a, mid + 1, right, target)
        else:
            return search_helper(a, left, mid - 1, target)
    else:
        location = -1
        if a[left] == a[mid]:
            location = search_helper(a, mid + 1, right, target)
        if location == -1 and a[mid] == a[right]:
            location = search_helper(a, left, mid - 1, target)
        return location
    
print(search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5)) # 8