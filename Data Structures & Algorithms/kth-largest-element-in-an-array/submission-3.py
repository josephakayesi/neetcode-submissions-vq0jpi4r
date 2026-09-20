import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Thought process
        - Keep a maxHeap
        - Iterate through the nums list and add each element into the maxHeap
        - Then iterate through the heap for k times. 
        - At each iterate pop out the element at the top of the heap
        - The last element to be popped out from the heap is the result

        Input: nums = [2,3,1,5,4], k = 2

        maxHeap = [ 3, 2, 1]




        """
        maxHeap = [] 

        for num in nums:
            heapq.heappush_max(maxHeap, num)
        
        for _ in range(k):
            res = heapq.heappop_max(maxHeap)
        
        return res

