class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Input: prices = [7,1,5,3,6,4]
        Output: 5

        Thought process
        - Two pointers - l and r 
        - l is the buy price
        - r is the sell price 

        If my buy price > sell price:
        - move my left pointer forwards 

        If my sell price > buy price:
        - calculate the max profit 
        - move right ponter

                              r
                    l
        prices = [7,1,5,3,6,4]
                        r
                     l
        prices = [7, 6, 5, 4, 3, 2]
        l = 0
        r = 0
        max_profit = 5

        Time: O(n)
        Space = O(1)
        """

        l = 0 
        r = 1
        max_profit = 0 

        while r < len(prices):
            max_profit = max(max_profit, (prices[r] - prices[l]))

            if prices[r] < prices[l]:
                l += 1
            else:
                r += 1

        return max_profit