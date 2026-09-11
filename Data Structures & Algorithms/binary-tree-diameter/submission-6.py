# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Thought process
        - At every node we need to find the maximum path for the left and right subtrees
            - Use a dfs to recurse all nodes. 
            - At the leaf node we return
            - Calculate the length of the path at each node and find the max
        - Calculate the maximum path (1 + max(left, right)) at each node and return it to its parent.
        - Return the diameter as the result. 

        Input: root = [1,null,2,3,4,5]

        dfs(1):
            dfs(None) -> 0
            dfs(2) -> 3
                dfs(3) -> 2
                    dfs(5)
                        dfs(None) -> 0
                        dfs(None) -> 0
                    dfs(None) -> 0
                dfs(4) -> 1
                    dfs(None) -> 0
                    dfs(None) -> 0


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

        