import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Assumptions:
        - Return in any order

        Intuition:
        - Find all the euclidean distances of the points
        - Keep the points in minheap
        - Return the k closest points to the origin

        points = [[0,2],[2,2]], k = 1
        minHeap = [ [8, 2, 2]]
        res = [[0, 2]]

        """
        minHeap = []
        res = []

        for (x, y) in points:
            z = sqrt((x ** 2) + (y ** 2))
            heapq.heappush(minHeap, [z, x, y])
        
        while len(res) < k:
            (_, x, y) = heapq.heappop(minHeap)
            res.append([x, y])
        
        return res
        