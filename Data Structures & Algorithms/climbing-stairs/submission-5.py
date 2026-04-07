class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Intuition:
        - Start a the empty problem 
        - You can choose to take 1 step or 2 steps at a time. 
        - For each step you take; 
            calculate the number of ways you can get to the final staircase from that step
        - Return the accumulation of the number of ways you can climb the step 
        """
        memo = {}

        def climb(step):
            if step <= 2:
                return step

            if step in memo:
                return memo[step]

            memo[step] = climb(step - 1) + climb(step - 2)

            return memo[step]

        return climb(n)