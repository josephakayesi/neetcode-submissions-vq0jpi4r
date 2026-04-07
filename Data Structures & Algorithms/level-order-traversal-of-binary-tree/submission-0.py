# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def __init__(self):
        self.res = defaultdict(list)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Intuition
        - Traverse the entire tree. 
        - Keep track of the current level. 
        - At each level append value to res at index
        """
        def visit(node, depth):
            if not node:
                return 
            
            if self.res[depth]:
                self.res[depth].append(node.val) 
            else:
                self.res[depth] = [node.val]
            
            visit(node.left, depth + 1)
            visit(node.right, depth + 1)

        visit(root, 0)
        print(self.res)
        v = []
        for key in self.res:
            print(key)
            v.append(self.res[key])

        print(v)
        return v