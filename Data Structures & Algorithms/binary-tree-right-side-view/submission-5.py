# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Intuition
        - Iterate through the tree in BFS
        - Keep a queue that you insert nodes starting from the left to the right. 
        - At each level of the tree
        - Iterate through the the queue by the queue length. 
            - Whilst iterating ensure to insert the child node for each node in the queue. 
        - Once the iterating over the length is done; the very last node that was popped out of the queue becomes the right side view node. 
        - Insert that into your result and then exit the inner loop since the intial queue length will have been completed. 
        - Continue this while the queue is not empty

        queue = []
        res = [1, 3, 5]
        right_node = 5
        queue_length = 2
        """

        if not root:
            return [] 

        queue = deque([root])
        res = [] 

        while queue:
            right_node = None 
            queue_length = len(queue)

            for i in range(queue_length):
                right_node = queue.popleft() 
                if right_node.left:
                    queue.append(right_node.left)

                if right_node.right:
                    queue.append(right_node.right)

            if right_node:
                res.append(right_node.val)

        return res