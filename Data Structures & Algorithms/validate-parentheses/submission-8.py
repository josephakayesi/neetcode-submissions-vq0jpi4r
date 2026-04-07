"""
Intuition
- We need keep a dictionary of valid paranthesis
- Keep a stack to match parathesis
- Iterate through the string; adding characters to the stack. 
- Before we add a new item; we check top of stack and find if its a match with the new character to be added
- If it matches:
    - we pop
- If it doesn't match
    - we add to the queue
- At the end we check if our stack is empty

stack = [] 
s = "([{}])" 
"""

class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        stack = [] 

        for char in s:
            if stack:
                top = stack[-1]

                if top in matches and matches[top] == char:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        return not stack
            

                 
            
