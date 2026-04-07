class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def climb(step):
            if step <= 2:
                return step 
            
            if step in memo:
                return memo[step]

            memo[step] = climb(step - 1) + climb(step - 2)

            return memo[step]

        return climb(n)