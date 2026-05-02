"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 

        root = Node(node.val)

        old_to_new = {}
        old_to_new[node] = root

        def clone(node):
            if node in old_to_new:
                # Can append neighbors here??
                return old_to_new[node]

            new_node = Node(node.val)
            old_to_new[node] = new_node

            for nei in node.neighbors:
                new_node.neighbors.append(clone(nei))

            return new_node
            



        for nei in node.neighbors:
            cloned = clone(nei)
            root.neighbors.append(cloned)

        return root
