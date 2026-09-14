# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Thought process
        - Iterate through the binary tree using bfs
        - We keep a queue and add the root to the queue
        - Start traversing from the root while queue is not empty
            - At each node; iterate the length of the queue and pop the elements into a sublist
            - Before popping element; append its children to the queue.
            - After iterating length of queue, append sublist into result. 
            - Keep doing until queue is empty

        Input: root = [1,2,3,4,5,6,7]
        Output: [[1],[2,3],[4,5,6,7]]

        q = []

        sublist = [4, 5, 6, 7]
        res = [[1], [2, 3], [4, 5, 6, 7]] 
        """

        if not root:
            return []
            
        q = deque([root])
        res = []
        
        while q:
            length = len(q)
            sublist = []

            for _ in range(length):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                sublist.append(node.val)

            res.append(sublist)
        return res