class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Understanding 
        - We can start at index `0` or index `1`
        - At each step we can take `i + 1` or `i + 2` step
        - Find the min cost to reach top of stairs

        Thought process
        - Start climbing stairs at index 0 and 1
        - Find the number of ways to reach to the top
        - At each decision: either `i + 1` or `i + 2` step;
            - check the min cost from that checkpoint to the top of stairs
        - Return the min cost to reach the top
        - The steps can be modelled as a tree
        - At each index we need to make a decision to either take 1 step or two steps
        - Our goal is to minimize the the cost to reach the top.
        - Let's take both directions but ensure that as we reach the top we are acconting for our minimum cost
        - Use dfs to traverse the decision tree
        """

        # self.memo = {}

        # def dfs(step):
        #     if step >= len(cost):
        #         return 0
            
        #     if step in self.memo:
        #         return self.memo[step]
            
        #     self.memo[step] =  cost[step] + min(dfs(step + 1), dfs(step + 2))
        #     return self.memo[step]

        # return min(dfs(0), dfs(1))
        n = len(cost)
        t0, t1 = cost[0], cost[1]

        for i in range(2, len(cost)):
            t0, t1 = t1, cost[i] + min(t0, t1)
            # dp[i] = cost[i] + min(dp[i- 1], dp[i - 2])

        return min(t0, t1)
