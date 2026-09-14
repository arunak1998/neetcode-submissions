class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False


        freq=Counter(hand)

        min_heap=list(freq.keys())

        heapq.heapify(min_heap)

        while min_heap:

            while min_heap and freq[min_heap[0]]==0:
                 heapq.heappop(min_heap)

            if not min_heap:
                break

            start=min_heap[0]

            for i in range(groupSize):

                card = start + i

                if freq[card] == 0:
                    return False

                freq[card] -= 1

        return True
