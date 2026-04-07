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

        heap = [] 

        # Create max heap from stones
        for stone in stones:
            heapq.heappush(heap, -stone)

        # Run simulation
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x == y:
                continue 
            
            z = x - y
            heapq.heappush(heap, -z)

        if not heap:
            return 0 
        
        return abs(heap[0])

        