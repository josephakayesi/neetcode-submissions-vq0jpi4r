class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Intuition
            - In this problem we need to find the minimum `k` rate that you con finish the pile of bananase.
            - You can use a binary search to find the average k you need. 
            - We keep shriking our k value until we find the minumum that will allow for us to finish our pile. 
            - Since we know we start at a low of 1 and the max value in the pile will finish our pile; we can search within that space using binary search
        """

        low = 1
        high = max(piles)
        k = high

        while low <= high:
            mid = (low + high) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours <= h:
                k = min(k, mid)
                high = k - 1
                continue 

            low = mid + 1

        return k


        