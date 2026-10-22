# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Thought process
        - We will need to first of all reverse the first k elements. 
        - Then reverse the next k eements in that order. 
        - If remaining elements are not up to k then we leave as-is
        - We need two main things:
            - Check if the upcoming elements are up to k
            - Reverse those elements and then move to the next k elements.
            - Keep doing that until we have reached the end of the linked list
        - Reverse linkedlist using standard algorithm
            - Start with a prev and current node. 
            - Keep reference of currents node next node. 
            - Point current node to previous node
            - Then set previous node to current node and then current node to the previous current next node. 
        - Once full reversed and that loop exits. 
        - Connect previous node to the revious current next nodes because it will holding that reference.
        - Similarly conitnue to next elements. 
        - So before we do a reversal we need to check if the next elements are up to k.
        - That will be the stopping condition; if not up to k then we have reached our base case
        """

        # def evaluate(start):
        #     prev = None
        #     current = start 
        #     count = 0

        #     # Cheks if the `x` nodes are up to `k`
        #     def _can_reverse(node):
        #         count = 0
                
        #         while node:
        #             count += 1 
        #             node = node.next

        #             if count == k:
        #                 return [start, True]

        #         return [None, False]     

        #     start, can_reverse = _can_reverse(current)
        #     if not can_reverse:
        #         return start
            
        #     nxt = None
        #     while count != k:
        #         nxt = current.next 
        #         current.next = prev
        #         prev = current
        #         current = nxt

        #         count += 1
            
        #     start.next = start
        #     evaluate(nxt)
        
        # return evaluate(head)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr