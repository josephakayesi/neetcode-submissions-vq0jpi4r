class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        """
        intervals = [[1,3],[4,6]], newInterval = [2,5]
        """

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                left = min(newInterval[0], intervals[i][0])
                right = max(newInterval[1], intervals[i][1])
                newInterval = [left, right]
            
        res.append(newInterval)
        return res