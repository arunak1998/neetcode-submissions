class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

       



        next1 = 0
        next2 = 0  

        for i in range(len(cost)-1,-1,-1):

                current = cost[i]+ min(next1, next2) 

                next2=next1

                next1=current

            

        return min(next1,next2)

        

