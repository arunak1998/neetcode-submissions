class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        newleft = newInterval[0]
        newright = newInterval[1]

        for i in range(len(intervals)):
            currentleft = intervals[i][0]
            currentright = intervals[i][1]

            if currentright < newleft:
                result.append(intervals[i])
            elif currentleft > newright:
                result.append([newleft, newright])
                newleft = currentleft 
                newright = currentright 
            else:
                 newleft = min(newleft, currentleft) 
                 newright = max(newright, currentright)

        result.append([newleft, newright])
        return result

            