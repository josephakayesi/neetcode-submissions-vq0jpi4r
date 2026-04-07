class Solution:
    def isValid(self, s: str) -> bool:
        """
        Intuition
        - Keep a map of character pairs
        - Keep a stack for checking if pairs. 
        - Iterate through the given string and for each item check if it has a matching pair
        - After iterating through the string check if the stack is empty or not
        - Empty stack -> valid parenthesis
        - Non-empty stack -> invalid parenthesis

        stack = [  ] 
        s = ([{}])
                  p
        """

        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        
        for char in s:
            if stack and stack[-1] == pairs.get(char):
                stack.pop()
                continue
            
            stack.append(char)

        return not stack