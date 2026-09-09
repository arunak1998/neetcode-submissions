class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        def dfs(i,comb,target):

            if target==0:
                result.append(comb[:])
                return

            if target <0 or i==len(nums):
                return

           
            comb.append(nums[i])


            dfs(i,comb,target-nums[i])

            comb.pop()

            dfs(i+1,comb,target)


        result=[]
        dfs(0,[],target)
        return result