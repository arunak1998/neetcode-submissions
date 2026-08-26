class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


       


        dp=[[0]*(len(nums)+1) for _ in range(len(nums)+1)]


        for i in range(len(nums)-1,-1,-1):

            for j in range(i-1,-2,-1):
                notpick=0+dp[i+1][j+1]


                pick=0

                if j==-1 or nums[i]>nums[j]:

                    pick=1+dp[i+1][i+1]

                dp[i][j+1]=max(pick,notpick)

        return dp[0][0]






                
               