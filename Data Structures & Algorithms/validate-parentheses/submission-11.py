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
            if stack and char in pairs and stack[-1] == pairs[char]:
                stack.pop() 
                continue 
            
            stack.append(char)

        return not stack