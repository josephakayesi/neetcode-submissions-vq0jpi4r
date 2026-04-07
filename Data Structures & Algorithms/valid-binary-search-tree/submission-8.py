# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Intution:
        - Iterate through the tree level order.
        - At each node; check the following:
            - node.val > node.left
            - node.val < node.right 
        - If it violates the above condition return False; otherwise return true at the end of iteration. 
        - Use a bfs 

        5
       / \
      4   6
         / \
        3   7

        dfs(5):
            dfs(4)

            dfs(6)

        """

        def dfs(node, left, right):
            if not node:
                return True 

            if left is not None and node.val <= left:
                return False
        
            
            if right is not None and node.val >= right:
                return False
        
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, None, None)

        
        