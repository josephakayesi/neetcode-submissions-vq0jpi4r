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
        Thought process
        - First we need to traverse our entire tree using dfs or any traversal and keep track of each nodes value. We can store the node values in a minHeap
        - After traversal; we return the kth smallest value

        dfs(4):
            dfs(3)
                dfs(2)

            dfs(5)
        
        minHeap = [2, 3, 4, 5]

        Input: root = [4,3,5,2,null], k = 4
        Output: 5
        """
        minHeap = []
        res = None

        def dfs(node):
            if not node:
                return 
            
            heapq.heappush(minHeap, node.val)

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        for _ in range(k):
            res = heapq.heappop(minHeap)
        
        return res
        


        