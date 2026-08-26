class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        l1=[]
        intervals.sort()
        l1.append(intervals[0])

        for i  in range(1,len(intervals)):

            start,end= intervals[i]

            prev_start,prev_end=l1[-1]

            if prev_end>=start:
                start=min(prev_start,start)

                end=max(prev_end,end)

                l1.pop()
            l1.append([start,end])
        return l1
            