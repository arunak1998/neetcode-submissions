class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        origin=[0,0]

        max_heap=[]

        for point in points:

            dist=((origin[0] - point[0]) ** 2 + (origin[1] - point[1]) ** 2) ** 0.5
            heapq.heappush(max_heap,(-dist,point))

            if len(max_heap)>k:
                heapq.heappop(max_heap)


        result=[point for dist,point in max_heap]

        return result


        




        
