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
                l += 1
                continue 
            
            r += 1
        return res

