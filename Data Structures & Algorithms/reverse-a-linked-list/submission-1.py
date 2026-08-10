# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Thought process
        - Start by creating a dummy head
        - Keep track of the current node as well as the next node
        - Iterate through the linked list whilst updating the 
        
        head = None 

        0 1 2 3
        p c  

        1 -> 0
        curr = 0
        nxt = 1

        nxt = curr.next
        temp = nxt.next 
        nxt.next = curr
        curr = nxt

        """
        if not head:
            return None 
        
        prev, curr = None, head 

        while curr:
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt
        return prev
        
