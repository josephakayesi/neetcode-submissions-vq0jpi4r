class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Intuition
        - First sort the intervals so adjacent intervals are closest
        - For each interval check if it overlaps.
        - If overlaps; remove largest interval
        - Return number of intervals removed
        """
        if not intervals:
            return 0

        intervals.sort()
        res = 0

        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if prev_end <= start:
                prev_end = end
            else:
                res += 1
                prev_end = min(end, prev_end)
            
        return res
