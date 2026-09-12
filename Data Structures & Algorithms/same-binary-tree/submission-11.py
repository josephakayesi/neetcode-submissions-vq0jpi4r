# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Thought process
        - Iterate through the tree recursively using dfs
        - At each node check if values are equal.
        - If values equal then continue recursion
        - Otherwise if values are inequal in any case return false.

        Input: p = [1,2,3], q = [1,2,3]

        dfs(1, 1) -> True
            dfs(2, 2) -> True
                dfs(None, None) -> True
                dfs(None, None) -> True
            dfs(3, 3) -> True
                dfs(None, None) -> True
                dfs(None, None) -> True

        """

        stack = [(p, q)]

        while stack:
            p, q = stack.pop()

            if not p and not q:
                continue
                   
            if not p or not q:
                return False

            if p and q and p.val != q.val:
                return False 
            
            stack.append((p.left, q.left))
            stack.append((p.right, q.right))

        return True
            

            
           
            

        # if not p and not q:
        #     return True 

        # if not p or not q:
        #     return False
        
        # if p.val != q.val:
        #     return False
        
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
