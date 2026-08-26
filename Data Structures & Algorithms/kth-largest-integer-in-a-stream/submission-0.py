class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap=[]
        self.size=k

        for num in nums:
            heapq.heappush(self.min_heap,num)


    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap,val)

        while len(self.min_heap)>self.size:

            heapq.heappop(self.min_heap)

        return self.min_heap[0]


