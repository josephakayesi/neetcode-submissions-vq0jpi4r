# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Intuition:
        - Left children are less than their parent(root) and right children are greater than thier parent. 
        - Start at the root
        - If both nodes on right; traverse right
        - If both nodes on left; traverse left
        - If nodes on either side; traverse left and right. 
    
        Solution
        - If p and q on either side of the tree; return root
        - If p and q on either side; then we need to traverse that subtree and return the ancestor
        - You do not need to worry about finding the nodes; rather; we worry about its position given the BST invariant. 
        - This avoids search traversals. 

        Edge cases:
        - If the tree is empty -> None
        - p != q


        """
        current = root

        while current:
            # On left side
             # On either sides
            # if (p.val < current.val and q.val > current.val) or (q.val < current.val and p.val > current.val):
            #     return current 

            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current


           
        





        