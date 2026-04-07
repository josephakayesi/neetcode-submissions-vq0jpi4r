# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = {}
        level = 0 

        def dfs(node, level):
            if not node:
                return 
            
            # if level not in levels:
            #     levels[level] = [] 
            
            # levels[level].append(node.val)

            levels.setdefault(level, []).append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        
        return list(levels.values())

        