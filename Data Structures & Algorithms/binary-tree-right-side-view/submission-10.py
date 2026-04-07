# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        
        q = deque()
        q.append(root)
        res = []

        if not root:
            return []

        while q:
            n = len(q)
            right = None 

            for i in range(n):
                right = q.popleft() 
                    
                if right is not None:
                    right.left and q.append(right.left)
                    right.right and q.append(right.right)

            res.append(right.val)

        return res


