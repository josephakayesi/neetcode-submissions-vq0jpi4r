import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Intuition
        - Keep a min heap of {hypothenus = points[i]}
        - For each element calculate the hypothenus (i.e distance from point to origin)
        - The min heap will automatically keep the closest points at the top.
        - Iterate for k times and return the closest points
        """

        heap = []

        for (x, y) in points:
            h = math.sqrt((x ** 2) + (y ** 2))
            heapq.heappush(heap, [h, x, y]) 
        
        res = []
        for _ in range(k):
            point = heapq.heappop(heap)
            res.append(point[1:])

        return res