class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Input: piles = [1,4,3,2], h = 9
        Output: 2

        [1, 2, 3, 4] h = 9       

        Assumptions
        - Our maximum number of piles is 4. 
        - At that 4 bananas per hour, we can finish our pile in the least amount of hours. 
        - We cannot go better than that. 

        k values should live between [1, 2, 3, 4]
                                       
        O(n * m)

        Thought process
        - For the piles; at a k rate of the maximum ith pile; we cannot do better than that. 
        - THis means our available k rate that we can optimally finish our bananas is within a range of [1, max(piles)]
        - Hence to find the best k rate, we need to iterate over that range [1, max(piles)]
        - Using a normal iterator will still yield the same result except that will be an O(n * m)
        - Hence to optimize this; we use a binary search over the available k rates. 
        - Using binary search; find the mid point. 
        - Check the number of hours that the midpoint k will use to finish the piles. 
        - If the k_hours > h:
            move to right side
        - otherwise move to left side. 
        - We keep doing this whilst l <= r


        piles = [25,10,23,4],  h = 4

        hours = 5
        l = 25
        r = 24

        m = 24

        res = 25

        -------


        piles = [1,4,3,2]

        hours = 10
        k_hours = [1, 2, 3, 4]
                      l
                   m     
                   r

        
        k = 1

        res = 2
        """

        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            m = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            
            if hours > h:
                l = m + 1
            else:
                r = m - 1
                res = min(res, m)

        return res
