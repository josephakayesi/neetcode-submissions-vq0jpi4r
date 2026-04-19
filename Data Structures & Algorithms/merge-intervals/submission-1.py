class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0]) 
        """
        intervals = [[1,3],[1,5],[6,7]]
        1 ---- 3 
        1 -----------5
        """

        res = [intervals[0]]

        for start, end in intervals[1:]:
            last = res[-1]

            if start <= last[1]:
                res[-1] = [res[-1][0], max(last[1], end)]
                continue 
            
            res.append([start, end])
        
        return res

            
