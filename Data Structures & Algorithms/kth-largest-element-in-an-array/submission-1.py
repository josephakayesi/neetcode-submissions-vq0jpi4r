import heapq

"""
Intuition

- Keep a min heap
- Check for the kth largest element

[4, 5, 5]

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
            heap = nums

            heapq.heapify(heap)

            while len(heap) > k:
                heapq.heappop(heap)
            
            return heap[0]


           
        


        