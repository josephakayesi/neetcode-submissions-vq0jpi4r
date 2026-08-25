# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Thought process
        - First keep two pointers walking the the distinct lists.
        - At each node; compare the two values. 
        - Update the next pointer of the lesser value to pointer the node of the larger list. 
        - Keep going until you reach the end of either one of the list
        - Update the next pointer of your current node to the node of the remaining list after walking
        - Return the head of the new list

        1 > 2 > 3
                   p1

        1 > 3 > 5
            p2

            d
        0 > 1 > 1 > 2 > 3 > 3 > 5
                        c
        """

        dummy = ListNode(0)
        curr = dummy

        p1 = list1
        p2 = list2 

        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                curr = curr.next
                p1 = p1.next
                continue 

            curr.next = p2
            curr = curr.next
            p2 = p2.next

        curr.next = p1 if p1 else p2
        return dummy.next
        