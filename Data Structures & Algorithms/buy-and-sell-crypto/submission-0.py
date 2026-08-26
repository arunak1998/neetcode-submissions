class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_pair=0
        

        for i in range(len(prices)-1):
            j=i+1

            while(j<len(prices)):
                if prices[j]-prices[i]<0:
                    break
                max_pair=max(max_pair,prices[j]-prices[i])
                j+=1

        return max_pair



        