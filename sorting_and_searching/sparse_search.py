from typing import List

def search(strings: List[str], string: str, first: int, last: int):
    if first > last:
        return -1
    mid = (first + last) // 2

    if strings[mid] == "":
        left = mid - 1
        right = mid + 1

        while True:
            if left < first and right > last:
                return -1
            elif right <= last and strings[right] != "":
                mid = right
                break
            elif left >= first and strings[left] != "":
                mid = left
                break
            right += 1
            left -= 1
    
    if string == strings[mid]:
        return mid
    elif strings[mid] < string:
        return search(strings, string, mid + 1, last)
    else:
        return search(strings, string, first, mid - 1)


def search_strings(strings: List[str], string: str):
    if strings == None or string == None or string == "":
        return -1
    return search(strings, string, 0, len(strings) - 1)

print(search_strings(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "ball")) # 4