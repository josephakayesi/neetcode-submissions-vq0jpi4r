import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Intuition:
        - Iterate through the array of stones
        - At each step pick the two heaviest stones (maxHeap)
            - if x == y:
                destroy both stones
            - if x < y:
                destroy x
                y = y -x
        
        stones = [2,3,6,2,4]

        => [2, 3, 2, 2]
        => [1, 2, 2]
        => [1]

        """

        # Create max heap from stones
        heapq.heapify_max(stones)

        # Run simulation
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x == y:
                continue 
            
            z = x - y
            heapq.heappush_max(stones, z)

        if not stones:
            return 0 
        
        return stones[0]

        