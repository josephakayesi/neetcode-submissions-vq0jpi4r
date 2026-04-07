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
        Intution
        - Keep a hash set that maps the old node to the new node. 
        - Backfill the each node with its neighbor
        - Return the root of the cloned node
        """

        old_to_new = {}

        def clone(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
        
        if not node:
            return None 

        return clone(node)