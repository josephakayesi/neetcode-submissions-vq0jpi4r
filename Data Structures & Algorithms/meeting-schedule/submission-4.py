"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        Intuition
        - Sort meeting times to allow adjacent times to be closest for easy comparison
        - Iterate through meeting times for overlaps
        - If overlap return False
        - Otherwise return true

        """

        if not intervals:
            return True 

        meetings = [] 

        for interval in intervals:
            meetings.append([interval.start, interval.end])

        meetings.sort()
        last = meetings[0]

        for start, end in meetings[1:]:
            if start < last[1]:
                return False 

            last = [start, end]
        return True


