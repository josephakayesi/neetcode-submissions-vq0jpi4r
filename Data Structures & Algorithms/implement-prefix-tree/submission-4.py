class TreeNode:
    def __init__(self):
        self.characters = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.characters = TreeNode()


    def insert(self, word: str) -> None:
        current = self.characters

        for char in word:
            if char in current.characters:
                current = current.characters[char]
                continue

            node = TreeNode()
            current.characters[char] = node
                
            current = node
        
        current.isEnd = True


    def search(self, word: str) -> bool:
        current = self.characters 

        for char in word:
            if char not in current.characters:
                return False
            
            current = current.characters[char]

        return current.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        current = self.characters

        for char in prefix:
            if char not in current.characters:
                return False
            
            current = current.characters[char]

        return True