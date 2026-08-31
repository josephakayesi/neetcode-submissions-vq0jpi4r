class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Thought process
        - Keep a stack to hold all temperatures.
        # - Also keep a running minimum for the lowest temperature. 
        - Iterate through the temperatures list. 
        - For each temperature check if the top of the stack. 
        - If the incoming temperature is less than top of stack; append to the stack. 
        - Otherwise if incoming temperature is greater than top of stack; then trace backwards and evaluate the number of days before a warmer temperature
        - Return the result

        temperatures = [30,38,30,36,35,40,28]
                                          ^
        stack = [(40, 5), (28, 6)]

        result = [1, 4, 1, 2, 1, 0, 0]
        """
        result = [0] * len(temperatures)
        stack = [] # [(temp, i)]

        for (i, temp) in enumerate(temperatures):
            if stack:
                while stack and stack[-1][0] < temp:
                    stack_t, stack_i = stack.pop()
                    result[stack_i] = i - stack_i 

            stack.append((temp, i))
        return result
