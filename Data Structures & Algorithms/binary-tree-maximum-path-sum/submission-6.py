# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        THought process
        - Traverse the entire tree using dfs. 
        - At each node; check the maximum  that can be formed at that node and update the running maximum
        - At the last call from the root; we return what is maximim. 

        maxPathSum = 35
        total = 10
        left = -5
        right = -inf

        dfs(-15)
            dfs(10) -> 10
            dfs(20) -> 35
                dfs(15) -> 15
                    dfs(-5) -> -5
                    dfs(None) -> -inf
                dfs(5) -> 5

        
        """
        self.max_path_sum = root.val

        def dfs(node):
            if not node:
                return float('-inf')

            left = dfs(node.left)
            right = dfs(node.right)

            total = node.val + left + right

            curr = max(node.val, node.val + max(left, right))
            self.max_path_sum = max(self.max_path_sum, total, curr)

            return curr
        
        dfs(root)
        return self.max_path_sum
            
            