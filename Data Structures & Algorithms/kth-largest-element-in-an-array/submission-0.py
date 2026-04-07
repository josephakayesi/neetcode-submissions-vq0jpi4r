import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        k = 2
        nums = [2, 3, 1, 5, 4]

        1. Heapify
        2. Remove elements until k largest elements in the heap
        3. Return the minimum element from the heap.

        nums = [4, 5, 5]
        k = 3
        """ 

        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]
        