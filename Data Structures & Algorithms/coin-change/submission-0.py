class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Intuition:
        - You need to reach an amount with fewest number of coins given an unlimited list of denominations
        - For each amount you need to either choose that or not choose that amount. 
        - If you decide to choose the amount the you need a minimum number of coins from remaining amount oreach your target

        12 -> 0
        0 -> number of ways -> 12

                   0(12)
    1(10)          5(7)         10(2)
1(9) 5(5) 10(0)


    for each coin:
        min(1 + dfs(amount - coin), dfs(amount))

        It is like a shortest path problem in a tree
        """

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                remaining = a - c 

                if remaining < 0:
                    continue
                
                dp[a] = min(dp[a], 1 + dp[a - c])
            
        return dp[amount] if dp[amount] != float('inf') else -1

        # memo = {}

        # def dfs(amount):
        #     if amount == 0:
        #         return 0

        #     if amount in memo:
        #         return memo[amount]
            
        #     res = float('inf')
        #     for coin in coins:
        #         remaining = amount - coin
        #         if remaining < 0:
        #             continue

        #         res = min(res, 1 + dfs(remaining))
            
        #     memo[amount] = res
            
        #     return memo[amount]
         
        # min_coins = dfs(amount)
        # return min_coins if min_coins < float('inf') else -1