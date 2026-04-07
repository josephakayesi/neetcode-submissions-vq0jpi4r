# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        - Start at the root; 
        - At each node -> find the diameter 
        - Since the predecessor only has one path to the longest child; 
            we find the max between the left child and the right child at the predecessor 

        - Set the maximum_diameter at each node 
        - Return the maximum_diameter
        """

        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.max_diameter = max(self.max_diameter, left + right)

            return 1 + max(left, right)
            
        
        dfs(root)
        return self.max_diameter