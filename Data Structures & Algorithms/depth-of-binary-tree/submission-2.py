# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Intuition - (Thought process)
        - Start at the root node, the max_depth is 1.
        - Use dfs to traverse each node.
        - At each node, increment the curr_max and update the max_depth
        - Continue until you have exhausted all nodes
        """

        max_depth = 0

        def dfs(node, curr_depth):
            nonlocal max_depth

            if node is None:
                return

            max_depth = max(max_depth, curr_depth)

            dfs(node.left, curr_depth + 1)
            dfs(node.right, curr_depth + 1)

        dfs(root, max_depth + 1)

        return max_depth