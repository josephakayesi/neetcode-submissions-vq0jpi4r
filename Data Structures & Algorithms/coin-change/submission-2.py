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
            
            best = float('inf')
            for coin in coins:
                best = min(best, 1 + choose(remaining - coin)) 
            memo[remaining] = best
            
            return best

        choose(amount)

        return -1 if memo[amount] >= float('inf') else memo[amount]
        