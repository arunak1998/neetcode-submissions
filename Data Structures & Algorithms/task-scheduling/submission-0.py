class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        heap = []
        for key, value in count.items():
            heapq.heappush(heap, -value)

        q = deque()
        time = 0

        while heap or q:
            time += 1

            if heap:
                freq = 1 + heapq.heappop(heap)

                if freq:
                    q.append([freq, time + n])

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time