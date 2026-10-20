# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Thought process

        Naive Approach
        - Iterate through each linkedlist and form a string or array
        - Reverse the string and convert to a number and add
        - Create a linkedList with the sum


         1 2 3
         4 5 6
         5 7 9
        """

        # s1 = ''
        # s2 = ''

        # curr = l1
        # while curr:
        #     s1 += str(curr.val)
        #     curr = curr.next
        
        # curr = l2
        # while curr:
        #     s2 += str(curr.val)
        #     curr = curr.next 

        # total = int(s1[::-1]) + int(s2[::-1])


        # dummy = curr = ListNode()
        # for digit in str(total)[::-1]:
        #     curr.next = ListNode(int(digit))
        #     curr = curr.next

        # return dummy.next

        dummy = curr = ListNode()
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            carry, digit = divmod(carry, 10)
            curr.next = ListNode(digit)
            curr = curr.next

        return dummy.next
        