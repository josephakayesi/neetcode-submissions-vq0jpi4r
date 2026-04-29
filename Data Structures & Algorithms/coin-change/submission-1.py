class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = defaultdict(lambda: float('inf'))
        memo[0] = 0

        def choose(remaining):
            if remaining in memo:
                return memo[remaining]

            if remaining == 0:
                return 0 
                
            if remaining < 0:
                return float('inf')
            
            for coin in coins:
                memo[remaining] = min(memo[remaining], 1 + choose(remaining - coin)) 
            
            return memo[remaining]

        choose(amount)

        return -1 if memo[amount] >= float('inf') else memo[amount]
        