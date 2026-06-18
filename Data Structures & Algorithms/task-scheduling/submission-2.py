from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Thought process
        - Keep a max_heap that will keep track of the most frequeent task at the top
        - Keep a queue that will keep track of the next available task and the next cycle it cab be processed.
        - Find the number of occurrences of each task
        - Store each tasks occurrence in a max_heap
        - Start counting the time elapsed while processing each task
        - For each task at the top of the max_heap; process it once and then enqueue for the next cycle (next_cycle_time = current_time + n)
        - At each task is processed; check if there is a task enqueued that needs to be processed. 
        - Process it and then add it to the max_heap
        - Keep going until max_heap or q is empty.
        - Return the elapsed time

        tasks = ["X","X","Y","Y"], n = 2

        time = 4
        heap = []
        task = 0
        q = []
        
        """

        counter = Counter(tasks)
        heap = [-count for count in counter.values()]
        heapq.heapify(heap)
        q = deque()

        time = 0
        while heap or q:
            time += 1

            if heap:
                count = 1 + heapq.heappop(heap)

                if count:
                    q.append([count, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time


