class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        n = len(temps)
        result = [0] * n
        stack = [] # (temp, index)

        for i, t in enumerate(temps):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                result[stack_i] = i - stack_i

            stack.append((t, i))

        return result
        