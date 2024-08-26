class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def is_palindrome(head: ListNode) -> bool:
    slow = head
    fast = head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()
        if slow.value != top:
            return False
        slow = slow.next

    return True

head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))

print("This is a palindrome", is_palindrome(head))


def is_palindrome_recurse(head: ListNode) -> bool:
    def check_palindrome(current: ListNode) -> bool:
        nonlocal front_pointer
        if current is not None:
            if not check_palindrome(current.next):
                return False
            if current.value != front_pointer.value:
                return False
            front_pointer = front_pointer.next
        return True

    front_pointer = head
    return check_palindrome(head)

print("This is a palindrome (recursive)", is_palindrome_recurse(head))
