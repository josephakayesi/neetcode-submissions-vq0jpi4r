from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-count for count in counter.values()]

        q = deque()
        heapq.heapify(maxHeap)

        time = 0
        while maxHeap or q:
            time += 1

            if maxHeap:
                # process task (adding one means you have processed the item once)
                count = 1 + heapq.heappop(maxHeap)

                if count:
                    # the task needs to be processed again in the future
                    # time + n; current time it was processed + the idle time gives the next time it will be processed.
                    q.append([count, time + n])

            # check if there are items in queue that needs to be processe at current time.  
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

