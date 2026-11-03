class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Input: prices = [10,1,5,6,7,1]
                            l     
                                       r
        Input: prices = [10,8,7,5,2]
                                  l
                                    r
        
        res = 0
        curr = 0
        
        Thought process
        - The goal is to maximize profit
        - Use two pointers; l and r 
        - both l and r starts at index 0
        - Find the profit for the current window. 
        - Update max profit
        - If current profit is negative value then move the l pointer forwards. 
        - Continue whilst l != 1 and/or r is within bounds
        
        """

        res = 0 
        l, r = 0, 0

        while r < len(prices):
            current = prices[r] - prices[l]
            res = max(res, current)

            if current < 0:
                # Move l to r since r will be on the smallest possible value in that window
                # We want to buy low and sell high. Anything in between the previous l and r will still amount
                # to a negative profit so we ignore all of them. 
                l = r
                continue 
            
            r += 1
        return res

