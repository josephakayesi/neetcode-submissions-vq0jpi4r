class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Intuition
        - First sort the intervals. Enables comparison of adjacent intervals
        - Iterate through the intervals and check overalapping. 
        - If overlapping merge and continue
        - Return merged intervals

        intervals = [[1,3],[1,5],[6,7]]

        res = [[1, 5], [6, 7]]

        intervals = [[1,2],[2,3]]

        res = [[1, 3]]
        """

        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            last = res[-1]

            # Does not overlap
            if last[1] < start:
                res.append([start, end])
                continue 
            
            # Overlaps
            if last[1] <= end:
                l = min(last[0], start)
                r = max(last[1], end)
                res[-1] = [l, r]
                continue 
            
        return res