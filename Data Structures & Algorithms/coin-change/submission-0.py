class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}

        def  change(amount):

            if amount==0:
                return 0

            if amount in memo:
                return memo[amount]
            res=float('inf')
            for coin in coins:

                if amount-coin>=0:

                    res=min(res,1+change(amount-coin))

            memo[amount]=res
            return res
        mincoin=change(amount)

        return -1 if mincoin ==float('inf') else mincoin
        

            

