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
         intervals.sort(key=lambda i: i.start)

         first_start=intervals[0].start
         first_end = intervals[0].end



         for i in range(1,len(intervals)):

            start=intervals[i].start
            end=intervals[i].end
            if first_end>start:
                return False
            first_start,first_end=start,end

         return True



