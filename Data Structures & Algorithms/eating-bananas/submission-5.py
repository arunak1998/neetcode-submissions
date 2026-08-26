import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low=1
        def possible(mid):
            balence=0
            for pile in piles:
                balence+=math.ceil(pile / mid)

            return balence<=h
               
        high=max(piles)
        minimum=high

        while(low<=high):
            mid=(low+high)//2

            if possible(mid):
                minimum = mid
                high=mid-1
            else:
                low=mid+1
                

        return minimum


