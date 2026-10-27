class Solution:
    def isValid(self, s: str) -> bool:
        """
        Thought process
        - Keep a hash map of character matching pairs
        - Also keep a stack to check matching pairs. 
        - Iterate through the characters in the string and push them to the stack. 
        - Before pushing, check if the incoming character matches top of stack
        - If matches, pop stack and continue
        - If not, push incoming character onto stack
        - Keep doing this until end of `s`
        - If the stack is empty then it means valid paranthesis otherwise invalid

        stack = [ ] 

        [ ]
          c

        s = "([{}])"
                 c  
        """

        pairs = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for character in s:
            if stack and pairs.get(character) == stack[-1]:
                stack.pop()
                continue 
            
            stack.append(character)
        
        return not stack