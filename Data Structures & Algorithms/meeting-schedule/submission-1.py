"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        times = []
        for interval in intervals:
            times.append([interval.start, interval.end])

        times.sort()

        stack = [times[0]]

        for start, end in times[1:]:
            last = stack[-1]

            if start < last[1]:
                return False 

            stack.append([start, end])
        
        return True