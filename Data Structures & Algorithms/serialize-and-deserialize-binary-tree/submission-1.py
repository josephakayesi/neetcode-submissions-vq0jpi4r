# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    """
    Thought process
    - Traverse the tree in inorder
    - Form a serialized string delimited by # for example. 
    - Send the serialized string over the desrialize. 
    - Deserialize the string into an array in inorder. 
    - Create a new tre from the inorder traversal 
    - For each node:
        - left = 2i + 1
        - right = 2i + 2
    - For the tree and return
    - Let ~ represent a None node

    Input: root = [1, 2, 3, null, null, 4, 5]
                   0  1  2    3     4   5  6
                              i

                   l = 7
                   r = 8

            root -> 1:
                    left -> 2
                            left -> null
                            right -> null
                    right -> 3
                             left -> 4
                             right -> 5   
    """

    def dfs(self, root, preorder):
        if not root:
            preorder.append('None')
            return
        
        preorder.append(str(root.val))
        self.dfs(root.left, preorder)
        self.dfs(root.right, preorder)
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = []
        self.dfs(root, preorder)
        return '#'.join(preorder)
        

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split('#')
        self.index = 0 

        def dfs():
            if values[self.index] == 'None':
                self.index += 1
                return None 
            
            node = TreeNode(int(values[self.index]))
            self.index += 1
            node.left = dfs() 
            node.right = dfs()
            return node

        return dfs()

            




