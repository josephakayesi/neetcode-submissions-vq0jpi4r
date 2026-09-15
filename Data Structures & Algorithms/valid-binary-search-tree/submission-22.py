# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Thought process
        - Three rules for binary search tree are found in description:
        - To ensure the binary search tree invaiant; we need to traverse the tree and check if the invariant holds at every node. 
        - We can traverse using dfs
        - We need to keep the bst invariant for the entire tree as well as each subtree locally. 
        - First we check at every node; if locally the bst invariant is kept i.e left < node < right
        - Secondly we check if the invariant holds in respect to the entire tree. We do this by passing down both the max node down the path and the min node down the path and ensuring that all nodes are within these bounds as well from the perspective of the entire tree
        - Keep going until we exhaust the traversal then we return True if no invariant failed at each node. 

        pathMin = 2
        pathMax = 2

        dfs(2, float('inf'), float('-inf')) -> True
            dfs(1, 2, 2) -> True
                dfs(None, 1, 3) -> True
                dfs(None, 1, 3) -> True


            dfs(3, 2, 2) -> True
                dfs(None, 2, 3) -> True
                dfs(None, 2, 3) -> True

            dfs(5, float('inf'), float('-inf))
                dfs(4, 5, 5) -> True
                    dfs(None, 4, 5) -> True
                    dfs(None, 4, 5) -> True
                dfs(6, 5, 5)
                    dfs()




                    5
            4               6
                        3       7

        """

        # def dfs(root, pathMin, pathMax):
        #     if not root:
        #         return True
            
        #     if root.left:
        #         if not (root.left.val < root.val and root.left.val < pathMin):
        #             return False
            
        #     if root.right:
        #        if not (root.right.val > root.val and root.right.val > pathMax):
        #             return False 
            
        #     pathMin = min(pathMin, root.val)
        #     pathMax = max(pathMax, root.val)

        #     return dfs(root.left, pathMin, pathMax) and dfs(root.right, pathMin, pathMax)

        # return dfs(root, float('inf'), float('-inf'))

        def dfs(node, low, high):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False 
            
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root, float('-inf'), float('inf'))





