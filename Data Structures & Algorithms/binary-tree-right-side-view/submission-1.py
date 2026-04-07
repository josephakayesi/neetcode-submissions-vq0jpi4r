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
        Intuition:
        - Traverse the tree; row level. 
        - At each leve; we need to know all nodes that make up that level. That outermost node becomes the right side view. 

        """
        if root is None:
            return [] 

        q = deque([root])
        res = []

        while q:
            right = None 
            q_len = len(q)

            for i in range(q_len):
                node = q.popleft() 

                if node:
                    right = node 
                    q.append(node.left)
                    q.append(node.right)

            if right:
                res.append(right.val)
        return res

            