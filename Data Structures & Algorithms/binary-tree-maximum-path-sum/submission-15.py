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
        # self.res = root.val

        # def dfs(root):
        #     if not root: 
        #         return 0
            
        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     left = max(left, 0)
        #     right = max(right, 0)

        #     self.res = max(self.res, root.val + left + right)

        #     return root.val + max(left, right)

        # dfs(root)
        
        # return self.res
        self.res = root.val

        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            local = node.val + left + right

            self.res = max(self.res, local)

            return node.val + max(left, right)
        
        dfs(root)
        return self.res
            
            