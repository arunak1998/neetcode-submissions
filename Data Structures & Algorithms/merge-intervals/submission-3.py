class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        prev_left = intervals[0][0]
        prev_right = intervals[0][1]
        result=[]

        for i in range(1, len(intervals)):
            current_left = intervals[i][0]
            current_right = intervals[i][1]

            if current_left <= prev_right:
                prev_left = min(prev_left, current_left)
                prev_right = max(prev_right, current_right)

            else:
                result.append([prev_left, prev_right])
                prev_left = current_left
                prev_right = current_right

        result.append([prev_left, prev_right])

        return result