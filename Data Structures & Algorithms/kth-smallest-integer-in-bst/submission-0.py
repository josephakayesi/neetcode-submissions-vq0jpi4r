# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        intuition; 
        - keep a maxheap;
        - iterate trhough the tree and add items to the max heap. 
        - once the iteration is done; check for the kth smallest value


        root = [2,1,3], k = 1

        res = [1] 


        """
        res = []

        def bfs(root):
            nonlocal res 

            if not root:
                return 

            heapq.heappush(res, -root.val)

            bfs(root.left)
            bfs(root.right)
        
        bfs(root)

        while len(res) > k:
            heapq.heappop(res)
        
        return -res[0]
        