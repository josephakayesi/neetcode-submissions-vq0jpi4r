# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Thought process 
        - To find if a linked list contains a cycle we keep two pointers `slow` and `fast`
        - Walk the `slow` pointer by one step and the `fast` pointer by two steps. 
        - Keep walking the linked list whiles `fast` is not None
        - If there is a cycle; then `slow` will eventually catch up `fast` pointer. 

                    f
                    s
        1 > 2 > 3 > 4 
            ^  <    |

            f 
            s
            1 > 2
        """

        if not head:
            return False 
        
        slow = fast = head 

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next 

            if slow == fast:
                return True
        
        return False
