class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap=[]

        for  i in range(len(points)):

            x2,y2=points[i]

            distance = (x2 - 0)**2 + (y2 - 0)**2

            heapq.heappush(heap,(-distance,i))
            if len(heap)>k:
                 heapq.heappop(heap)

        result=[]

        while heap:

            _,i =heapq.heappop(heap)

            result.append(points[i])

        return result
        

      