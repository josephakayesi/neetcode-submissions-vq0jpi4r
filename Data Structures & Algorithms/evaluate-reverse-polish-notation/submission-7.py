class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token not in ["+", "*", "-", "/"]:
                stack.append(int(token))
                continue
            
            second_val = stack.pop()
            first_val = stack.pop()
            
            res = eval(f'{first_val}{token}{second_val}')
            stack.append(int(res))

        return stack.pop()