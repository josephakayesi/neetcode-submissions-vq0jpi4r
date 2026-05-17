# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    - In order traversal of a valid BST results in an ordered list of the trees nodes.
    - This property makes it easy to code out the solution and find the result. 
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = [] 

        def dfs(node):
            if not node:
                return 

            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)
        
        smallest = None 

        dfs(root)
        
        return nodes[k - 1]
        