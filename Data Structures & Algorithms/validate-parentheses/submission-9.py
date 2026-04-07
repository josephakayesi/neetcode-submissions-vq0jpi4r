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
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        stack = [] 

        for char in s:
            if stack and pairs.get(char) == stack[-1]:
                stack.pop()
                continue 

            stack.append(char)
        return not stack
            

                 
            
