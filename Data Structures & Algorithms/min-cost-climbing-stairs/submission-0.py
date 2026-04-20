class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(step):
            if step >= len(cost):
                return 0

            if step in memo:
                return memo[step]

            memo[step] = cost[step] + min(dfs(step + 1), dfs(step + 2))

            return memo[step]

        return min(dfs(0), dfs(1))
