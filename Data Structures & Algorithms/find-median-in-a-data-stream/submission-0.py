import heapq

"""
self.arr = [1, 3]
heap_length = 
mid_length = 1
mid_left = 1
mid_right = 3
mid = 2.0
removed = [] 
"""

class MedianFinder:

    def __init__(self):
        self.arr = [] 
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.arr, num)

    def findMedian(self) -> float:
        heap_length = len(self.arr)
        removed = [] 

        # if odd 
        if heap_length % 2 == 1:
            mid_length = heap_length // 2
            
            for _ in range(mid_length):
                top = heapq.heappop(self.arr)
                removed.append(top)

            mid = self.arr[0]

            for num in removed:
                heapq.heappush(self.arr, num)
            
            return mid 
            
        # if even 
        if heap_length % 2 == 0:
            mid_length = heap_length // 2 

            for _ in range(mid_length - 1):
                top = heapq.heappop(self.arr)
                removed.append(top)

            mid_left = self.arr[0]

            removed.append(heapq.heappop(self.arr))
            mid_right = self.arr[0]

            mid = (mid_left + mid_right) / 2

            for num in removed:
                heapq.heappush(self.arr, num)

            return mid