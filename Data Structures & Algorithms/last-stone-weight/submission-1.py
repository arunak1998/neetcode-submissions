class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:

            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x == y:
                continue

            new = x - y
            heapq.heappush(heap, -new)

        return 0 if not heap else -heap[0]