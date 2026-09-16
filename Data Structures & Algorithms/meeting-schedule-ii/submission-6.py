"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        

        start=sorted(intervals[i].start for i in range(len(intervals)))
        end=sorted(intervals[i].end for i in range(len(intervals)))

        s=0
        e=0
        count=0
        res=0


        while s<len(start):
            if start[s]<end[e]:

                s+=1
                count+=1

            else:
                e+=1
                count-=1

            res=max(res,count)

        return res


