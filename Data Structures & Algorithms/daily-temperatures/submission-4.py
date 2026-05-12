class Solution:
    """
    temperatures = [30,38,30,36,35,40,28]
                                      ^
    stack = [(5, 40), (6, 28)]

    res = [1, 4, 1, 2, 1, 0, 0]
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [(0, temperatures[0])] # [(i, temp)]

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stack_i, stack_t = stack.pop() 
                res[stack_i] = i - stack_i
            stack.append((i, temp))
        
        return res
