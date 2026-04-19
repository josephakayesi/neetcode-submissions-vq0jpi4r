class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() 
        """
        intervals = [[1,3],[1,5],[6,7]]
        1 ---- 3 
        1 -----------5
        """


        stack = []

        for interval in intervals:
            if not stack:
                stack.append(interval)
                continue 

            top = stack[-1]

            # It overlaps
            if interval[0] <= top[1]:
                left = min(top[0], interval[0])
                right = max(top[1], interval[1])
                newInterval = [left, right]

                stack.pop()
                stack.append(newInterval)
                continue
            
            stack.append(interval)

        return stack

            
