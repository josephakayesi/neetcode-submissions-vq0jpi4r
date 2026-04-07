# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        BST
        1. Values on the left subtree are smaller than the root
        2. Values on the right subtree are larger than the root.

        i = 1
        left = 2^i + 1 # 3
        right = 2^i + 2 # 4

        left = 2^i + 1
        left - 1 = 2^i

        parent = (i - 1) // 2


        p = {1, 0}
        q = {}
        [
            [5], 
            [3, 8], => {1, 0}
            [1, 4, 7, 9], => {2, 0}
            [2]]

        Tree = [5,3,8,1,4,7,9,null,2]


        Thought process
        1. 
        """

        curr = root 

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr


"""

"""










        