# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Constraints
        - Left child is smaller than root.
        - Right child is always larger than root
        
        Thought process
        - Keep the root as the current
        - While current_root exists:
            - q > curr and p > curr:
                - curr = curr.right (all nodes in right subtree)
            - q < curr and p < curr:
                - curr = curr.left (all nodes in left subtree)
            - else:
                return curr 
        """

        curr = root 

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right 
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left 
            else: 
                return curr