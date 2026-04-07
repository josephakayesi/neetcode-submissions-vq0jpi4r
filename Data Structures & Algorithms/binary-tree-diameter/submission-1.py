# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Thought process:
        - Start at the root (diameter = 0)
        - We find the diameter at each subtree:
            - At each node pass the current diameter down the tree. 
            - When we find the max depth at each node; we update the diameter.
        - dfs(node, res):
            if not node:
                return 0
                
            left = dfs(node.left, res+1)
            right = dfs(node.right, res+1)

            res  = max(res, left, right)

        dfs(node, 0)

        return res
        """ 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Thought process:
        - Start at the root (diameter = 0)
        - We find the diameter at each subtree:
            - At each node pass the current diameter down the tree. 
            - When we find the max depth at each node; we update the diameter.
        - dfs(node, res):
            if not node:
                return 0
                
            left = dfs(node.left, res+1)
            right = dfs(node.right, res+1)

            res  = max(res, left, right)

        dfs(node, 0)

        return res
        """ 
        self.max_diameter = 0

        def get_height(node):
            if not node:
                return 0
            
            # Recursively find the height of left and right subtrees
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # The diameter at the current node is the sum of left and right heights
            # Update our global maximum if this path is longer
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return the height of this node to the parent
            # (1 for the current node + the max of its children)
            return 1 + max(left_height, right_height)

        get_height(root)
        return self.max_diameter


    """
    max_diameter = 3

    get_height(1):
        - get_height(None) -> 0
        - get_height(2) -> 3
            - get_height(3) -> 2
                - get_height(5) -> 1
        - get_height(4) -> 1
    """



















