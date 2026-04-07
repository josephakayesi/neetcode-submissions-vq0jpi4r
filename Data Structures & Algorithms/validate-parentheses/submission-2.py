class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if stack and char in pairs and pairs[char] == stack[-1]:
                stack.pop() 
                continue
            
            stack.append(char)

        return not stack