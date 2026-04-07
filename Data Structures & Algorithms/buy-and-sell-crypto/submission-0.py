class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Thought process
        - Keep two pointers
        - Iterate through the prices. 
        - Keep a max for the difference between your buy and sell.
        - If the difference increases, move right pinter. 
        - If it decreases move left pointer until you reach the end of the iteraton
        """

        l = 0
        r = 0
        max_profit = 0

        while l < len(prices) and r < len(prices):
            if prices[l] <= prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
                r += 1
            else:
                l += 1

        return max_profit