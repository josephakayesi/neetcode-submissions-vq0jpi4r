"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Thought process

        - We are given the adjacency list (1-indexed)
        - To deep clone this graph we need to first of all store our nodes in a dictionary {old -> new}
        - Iterate through our ajacency list and the neighbours of each old node; and add the old nodes neighbors to the new nodes neighbors. 
        - We can decide to return the first new node from our old node to new node mapping. 

        Consider adding a visited node so we dont not loop infinitely

        adjList = [
            1: [2],
            2: [1,3],
            3: [2]
        ]

        old_to_new = {
            _Node(1): Node(1) -> neighbors = [Node(2)]
            _Node(2): Node(2) -> neighbors = [Node(1), Node(3)]
            _Node(3): Node(3) -> neighbors = [Node(2)]
        }

        dfs(1):
            dfs(2): < 
                dfs(1) < 
                dfs(3): <
                    dfs(2): <


        """
        
        visited = set() 

        if not node:
            return 

        old_to_new = {}

        
        def dfs(node):    
            if node in old_to_new:
                return 

            old_to_new[node] = Node(node.val)
            
            for neighbor in node.neighbors:
                dfs(neighbor)
                old_to_new[node].neighbors.append(old_to_new[neighbor])

        dfs(node)

        return old_to_new[node]
        
        