"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
Questions: 
- What is a deep copy? (Deep copy vs shallow copy)

Thought process:
- Iterate through the original list
- For each node in the list; create a new `ListNode()` with val; a next pointer and then random pointer (Do not point but copy)

"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {}
        
        cur = head 
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next

        cur = head 
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy.get(cur.next, None)
            copy.random = oldToCopy.get(cur.random, None)
            cur = cur.next
        
        return oldToCopy.get(head, None)