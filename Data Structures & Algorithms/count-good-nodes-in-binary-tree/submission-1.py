# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Intuition:
        - Iterate through the tree using DFS. 
        - At each node keep track of the maximum value from the root up until that node. 
        - If the max is greater than the current node's value then increment the good nodes count; otherwise continue. 
        - Do this until you have covered all leaf nodes or until you have exhausted the iteration

        dfs(3, 3):
            dfs(3, 3):
                dfs(4, 3)

                dfs(2, 3)

        3
       /
      3
     / \
    4   2


        """

        good = 0 

        def dfs(node, curr_max):
            nonlocal good 

            if node is None:
                return

            if node.val >= curr_max:
                good += 1 
            
            curr_max = max(curr_max, node.val)
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)

        dfs(root, root.val)

        return good
        