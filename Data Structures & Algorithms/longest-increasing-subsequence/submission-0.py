class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        memo={}


        def dfs(index,prev_index):


            if index==len(nums):
                return 0


            if (index,prev_index) in memo:

                return memo[index,prev_index]


            notpick=0+dfs(index+1,prev_index)


            pick=0

            if prev_index==-1 or nums[prev_index]<nums[index]:

                pick=1+dfs(index+1,index)


            result=max(pick,notpick)


            memo[(index,prev_index)]=result
            return result

        return dfs(0,-1)