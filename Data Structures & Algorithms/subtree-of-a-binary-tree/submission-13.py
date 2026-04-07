# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        - Start at the root
        - Iteratively check if any nodes in the root equal the subRoot; 
        - Check if the subtree in the root is same tree as the subRoot. 

        """

        def isSametree(node, subRoot):
            if not node and not subRoot:
                return True 
            
            if node and subRoot and node.val == subRoot.val:
                return (isSametree(node.left, subRoot.left) and 
                        isSametree(node.right, subRoot.right))
            
            return False

        if not root and not subRoot:
            return True 
        
        if not root:
            return False 
        
        # Always check all three: current node match, left subtree, right subtree
        return (isSametree(root, subRoot) or
                self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))


