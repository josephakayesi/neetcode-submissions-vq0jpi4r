class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Intuition:
        - Iterate through the intervals. 
        - For each interval check if it overlaps. 
        - If overlaps; merge and construct the remaining of the interval
        
        
        Input: intervals = [[1,3],[4,6]], newInterval = [2,5]

        1-----2 3----5     9----10
                       6--7
        """

        res = [] 

        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            # Does not overlap
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            # Overlaps (merge)
            elif newInterval[0] <= end:
                left = min(start, newInterval[0])
                right = max(end, newInterval[1])
                newInterval = [left, right]
            else:
                res.append([start, end])
        
        res.append(newInterval)
        return res