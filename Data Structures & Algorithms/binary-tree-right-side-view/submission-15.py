# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Thought process
        - Recursively iterate through the binary tree using bfs
        - Store the nodes at that level in a queue
        - Also store the length of the number of nodes at each level. 
        - The length informs of how many times to iterate through the queue for that level. 
        - For each queue iteration; popleft the element and append the children starting from left child to the right child to the queue for the next iteration
        - Once I exit the queue iteration for that level; the last element that I popped out is my right most node. 
        - Add the right most node to my results.
        - Once queue is empty return results

        Input: root = [1,2,3,null,4,null,5]
        Output: [1,3,5] 

        q = []

        right = 5
        res = [1, 3, 5]
        
        """

        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            length = len(q)
            right = None

            for _ in range(length):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                
                right = node
            
            res.append(right.val)
        return res
                
