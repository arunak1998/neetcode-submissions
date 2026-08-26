class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map={}


        for num in nums:

            freq_map[num]=freq_map.get(num,0)+1

        min_heap=[]
        for key,value in freq_map.items():

            heapq.heappush(min_heap,(value,key))

            if len(min_heap)>k:

                heapq.heappop(min_heap)

        

        return  [element[1] for element in min_heap]
        