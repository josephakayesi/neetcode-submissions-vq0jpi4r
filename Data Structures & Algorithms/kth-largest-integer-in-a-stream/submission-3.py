import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        return self.heap[0]

        
"""
k = 3
[6, 7, 8] -> 5


Process

- Create a heap from nums

add(self, val: int) -> int:
    - pop heap until k - 1
    
    - push heap(val)

    - return heap[0]

k = 3
[3, 7, 8] -> 6


"""