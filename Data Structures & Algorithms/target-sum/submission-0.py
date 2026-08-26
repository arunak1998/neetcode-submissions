class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo={}
        def dfs(index,result):

            if index==len(nums):
               if result==target:
                  return 1
               else:
                  return 0
            if (index,result) in memo:
                return memo[(index,result)]

            sub=dfs(index+1,result-nums[index])

            addd=dfs(index+1,result+nums[index])

            final=sub+addd
            memo[(index,result)]=final
            return final

        return dfs(0,0)

        
