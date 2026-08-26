class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0

        j=1
        maxi=0

        while j<len(prices):

            if prices[i]>prices[j]:

                    i=j

                   

            else:

                    maxi=max(maxi,prices[j]-prices[i])
            j+=1

                    

        return maxi