import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []

        for num in nums:
            heapq.heappush_max(max_heap, num)

        for _ in range(k):
            res = heapq.heappop_max(max_heap)

        return res

      