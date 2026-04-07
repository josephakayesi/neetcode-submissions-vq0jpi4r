# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Placeholder node to simplify edge cases
        tail = dummy

        # Pointers to traverse both lists
        p1, p2 = list1, list2

        # Merge until one list runs out
        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next  # advance merged list pointer

        # Append the remaining nodes (if any)
        tail.next = p1 or p2

        return dummy.next   