# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Thought process
        - Keep going down the root and check if any node == root of the subroot. 
        - If the node in root equals subroot root; then there is a potential for them to have the same structure
        - Once we find the same roots at each tree; we recursively run a function to check if its the same tree.
        If we exhaust our recursive call and no subtree is found then return False otherwise True

        Can nodes in a subtree have the same values or are they unique
        """

        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True 

            if not root or not subRoot:
                return False 
            
            if root.val != subRoot.val:
                return False
            
            return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right) 
    
        if not subRoot:
            return True 
        
        if not root:
            return False
        
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)