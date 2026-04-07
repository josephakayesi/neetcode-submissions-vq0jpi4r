# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def __init__(self):
        self.res = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Intuition
        - Traverse the entire tree. 
        - Keep track of the current level. 
        - At each level append value to res at index
        """
        def visit(node, depth):
            if not node:
                return None
            
            if len(self.res) == depth:
                self.res.append([])
            
            self.res[depth].append(node.val)
            visit(node.left, depth + 1)
            visit(node.right, depth + 1)

        visit(root, 0)
        
        return self.res