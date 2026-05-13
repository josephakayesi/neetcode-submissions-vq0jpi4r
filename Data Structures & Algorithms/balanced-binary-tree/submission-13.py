# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        - Traverse the tree using dfs. 
        - At each node I want to know two things; 
            - 1. is my left and right subtree balanced; 
            - 2. heights of left and right subtrees
        - If subtrees at each node is balanced then return up to parent; otherwise return False

        True Example
        dfs(1): -> [T, 3]
            dfs(2): -> [T, 1]

            dfs(3): -> [T, 2]
                dfs(4): -> [T, 1]
                dfs(None): -> [T, 0]



        False example
        dfs(1): -> [F, 4]
            dfs(2): -> [T, 1]

            dfs(3): -> [F, 3]
                dfs(4): -> [T, 2]
                    dfs(5): -> [T, 1]
                    dfs(None): -> [T, 0]

                dfs(None) -> [T, 0]
        """

        def dfs(root):
            if not root:
                return [True, 0] # [balanced, height]
            
            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            height = 1 + max(left[1], right[1])

            return [balanced, height]

        return dfs(root)[0]

