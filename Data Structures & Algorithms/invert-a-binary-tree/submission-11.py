# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Thought process
        - I start at the root; 
        - I traverse my tree from the root down to each leaf. 
        - At each level I invert the nodes at the level
        - I do this operation down the tree
        - I return the inverted tree via the root.
        """

        if not root:
            return

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root