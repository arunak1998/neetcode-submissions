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
        intervals = sorted(intervals, key=lambda x: x.start)


        prevstart,prevend=intervals[0].start,intervals[0].end

        for i in range(1,len(intervals)):

            currentstart, currentend = intervals[i].start,intervals[i].end

            if prevend> currentstart:
                return False
            prevstart, prevend = currentstart, currentend



        return True
