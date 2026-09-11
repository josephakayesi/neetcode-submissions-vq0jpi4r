# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Thought process
        - Recursively run a dfs function on each node. 
        - Note that each node by itself forms a subtree
        - At each node check the height of left and right subtree
        - If difference of left and right is greater than 1 then that subtree is unblanaced.
        - Otherwise it is balanced. 
        - At each node keep track of the height and is_balanced  
        """

        def dfs(root):
            if not root:
                return [0, True] # [height, is_balanced]
        
            left = dfs(root.left)
            right = dfs(root.right)

            is_balanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1
            height = 1 + max(left[0], right[0])

            return [height, is_balanced]
        
        return dfs(root)[1]