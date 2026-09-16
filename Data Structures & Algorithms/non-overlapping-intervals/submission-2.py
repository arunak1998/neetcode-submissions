class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result=0
        intervals = sorted(intervals, key=lambda x: x[0])

        prev_left,prev_right=intervals[0]

        for  i in range(1,len(intervals)):

            current_left,current_right=intervals[i]

            if current_left < prev_right :

                    result+=1

                    min_right=min(prev_right,current_right)

                    prev_left =prev_left if min_right==prev_right else current_left

                    prev_right=min_right

            else:

                prev_left,prev_right=current_left,current_right



        return result