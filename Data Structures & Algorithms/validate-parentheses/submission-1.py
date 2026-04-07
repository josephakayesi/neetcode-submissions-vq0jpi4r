class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if stack and pairs.get(char) == stack[-1]:
                stack.pop() 
                continue
            
            stack.append(char)

        return not stack