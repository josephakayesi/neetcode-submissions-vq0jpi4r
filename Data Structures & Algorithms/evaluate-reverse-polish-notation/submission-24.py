class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Thought process
        - Keep a stack
        - Iterate the tokens and add each number to the stack. 
        - Once you reach an operand. 
        - Evalue the previous two values in the stack
        - Add the result to the stack and  continue iterating the tokens
        - Keep doing this until you reach the end of the tokens list
        - Do the last evaluation
        - Return the top of the stack as the result. 


        tokens = ["1","2","+","3","*","4","-"]

        stack = [5]
        f = 9
        s = 4


        """

        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
                continue

            second = stack.pop()
            first = stack.pop()
            result = None

            if token == "+":
                result = first + second
            
            if token == "-":
                result = first -  second
            
            if token == "*":
                result = first * second
            
            if token == "/":
                result = int(first / second)

            stack.append(result)

        return stack[-1]                    
                    

        