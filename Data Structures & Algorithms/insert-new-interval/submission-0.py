class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        l1=[]

        new_start,new_end=newInterval
        i=0
        n = len(intervals)
        while i<n and intervals[i][1]<new_start:
            l1.append(intervals[i])
            i+=1
        while i<n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1

            
        l1.append([new_start,new_end])

        while i<n:
            
            l1.append(intervals[i])
            i+=1
        return  l1




        

