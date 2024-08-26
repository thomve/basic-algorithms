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
