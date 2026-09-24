from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        """
        Thought process
        - Iterate through the binary tree using bfs
        - At each level; add the nodes. 
        - Iterate through the queue for the length of that level and pop each element
        - The last in the queue is the right side view
        """
        if not root:
            return [] 
            
        q = deque([root])
        res = []

        while q:
            length = len(q)
            node = None 

            for _ in range(length):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

            if node:
                res.append(node.val)
        return res

