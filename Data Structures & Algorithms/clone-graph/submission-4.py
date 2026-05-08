"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


        Node(1) {
            val = 1
            neighbors = Node(2) {
                    val = 2,
                    neighbors = Node(1), Node(3)
                    }
        }

        old_to_new = {
            0Node(1) = Node(1)->neighbors[Node(2)],
            0Node(2) = Node(2)->neighors[Node(1), Node(3)],
            0Node(2) = Node(3)->neighbors[Node(2)]
            }
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 

        old_to_new = { }
        
        def clone(node):
            if node in old_to_new:
                return old_to_new[node]
            
            new_node = Node(node.val)
            old_to_new[node] = new_node

            for nei in node.neighbors:
                new_node.neighbors.append(clone(nei))

            return new_node

        return clone(node)


        
        