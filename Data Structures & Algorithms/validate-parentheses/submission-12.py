class Solution:
    """
    s = "([{}])"
               ^
    
    stack = [     ]
    """
    def isValid(self, s: str) -> bool:
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