# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Thought process
        - First find the midpoint of the list
        - Rotate the midpoint to the tail of the list such that:
            - All values on the left half point towrds the mid
            - And all values on the right half also point towards the mid 
            - List will look like this (0 > 1 > 2 > 3 < 4 < 5 < 6)
        - Iterate starting from both ends of the list. 
        - Update left pointer to point to right pointer and move pointers by one. 
        - Do this while not left.next or right.next
        """

        if not head:
            return 
        
        # find the midpoint of the list
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next 
        
        prev = None
        curr = slow 

        while curr:
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt
        
        # reorder the list
        right, left = head, prev

        while right and left:
            right_next, left_next = right.next, left.next  
            
            right.next = left 
            right = right_next
            left.next = right_next
            left = left_next