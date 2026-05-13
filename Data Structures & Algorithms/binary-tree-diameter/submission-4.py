# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Intuition
        - For each node calculate the max length of the left and right subtree
        - Each node is a converging point.
        - Start at the root. 
        - Find the max path on left and right subtree
        - At each node; when you return to your parent; choose the max between paths of children
        - Return the sum of left and right path

        longest = 3
        
        dfs(1):
            dfs(None) -> 0:
            dfs(2) -> 3:
                dfs(3) -> 2:
                    dfs(5) -> 1
                    dfs(None)-> 0

                dfs(4) -> 1:

        """

        self.longest = 0

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            self.longest = max(self.longest, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        
        return self.longest
        