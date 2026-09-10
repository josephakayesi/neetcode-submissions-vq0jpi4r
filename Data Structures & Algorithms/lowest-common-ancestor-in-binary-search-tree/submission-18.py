# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Thought process
        - Using the binary search tree invariant (left < root < right and all left < root < all right)
        - We can iteratively check which sides does `p` and `q` sit in the tree; right side or left side
        - If p <= root <= q:
            return current node
        
        - if p < root and q < root:
            visit(root.left)
        
        - If p > root and q > root:
            visit(root.right)

        Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
                       
        Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4

        Input: root = [5,3,8,1,4,7,9,null,2], p = 1, q = 2

        root=[2,1]
        p=2
        q=1

        lca(2, 2, 1)

        """

        if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
            return root
        
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        