class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
                continue 

            second = stack.pop()
            first = stack.pop()

            if token == "+":
                stack.append(first + second)
            elif token == "-":
                stack.append(first - second)
            elif token == "*":
                stack.append(first * second)
            elif token == "/":
                stack.append(int(first / second))
        
        return stack[-1]
            