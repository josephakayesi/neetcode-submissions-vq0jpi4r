# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Thought process
        - Keep two pointers, prev and curr
        - `prev` will be None at first
        - `curr` will be point to head
        - Walk the list whilst curr is not None
        - Keep temporary variable to hold the curr.next as we walk
        - Set curr.next to prev
        - Update prev to curr and curr to the temporary variable holding curr original next node. 

        head = 0 -> 1 -> 2 -> 3 -> None 

        
     <- 0 <- 1 <- 2 <- 3  None 
                       p     c
        
        head = 3 -> 2 -> 2 -> 0 -> None

                             n
      <-0 <- 1 <- 2 <- 3 -> None 
                             c
                       p

        """
        prev = None
        curr = head 

        while curr is not None:
            nxt = curr.next 
            curr.next = prev
            prev = curr 
            curr = nxt 
        
        return prev