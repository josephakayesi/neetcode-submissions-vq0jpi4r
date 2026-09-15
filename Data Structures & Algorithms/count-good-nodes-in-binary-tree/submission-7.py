# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Thought process
        - For node x; is there a value from the root to that node that contains a value greater than the x
        - If there contains a value then it is a bad node otherwise if there contains no value then it is a good node. 
        - Walk the tree down every path from the root to every other node. 
        - Whilst walking the path keep track of the current maximum value on that path. 
        - Compare the current maximum value for that path with the current node. 
        - If the node x is greater than the current maximum on that path then that node x is consisdered good; increment the good nodes counter
        - Walk all paths until you reach the leaves;
        - Once exhausted; return the good odes counter as the result. 
        - Walk the tree using dfs 


        Input: root = [2,1,1,3,null,1,5]
        Output: 3

        good = 3

        dfs(2, 2)
            dfs(1, 2)
                dfs(3, 2)
                dfs(None, 2)
            dfs(1, 2)
                dfs(1, 2)
                dfs(5, 2)

        stack = [1]
        pathMax = 
        good = 1

        node = 1

        """


        # pathMax = root.val
        # stack = [(root, pathMax)]
        # good = 0

        # while stack:
        #     (node, pathMax) = stack.pop()

        #     if node.val >= pathMax:
        #         good += 1

        #     pathMax = max(pathMax, node.val)

        #     if node.left:
        #         stack.append((node.left, pathMax))

        #     if node.right:
        #         stack.append((node.right, pathMax))

        # return good

        self.good = 0

        def dfs(root, path_max):
            if not root: 
                return 
            
            if root.val >= path_max:
                self.good += 1

            path_max = max(path_max, root.val)
            
            dfs(root.left, path_max)
            dfs(root.right, path_max)
        
        dfs(root, root.val)

        return self.good


