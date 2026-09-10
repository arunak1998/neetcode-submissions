class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        def dfs(i,sub):

            
            result.append(sub[:])

            for j in range(i,len(nums)):

                if j>i and nums[j]==nums[j-1]:
                    continue

                sub.append(nums[j])
                dfs(j+1,sub)
                sub.pop()

        result=[]
        dfs(0,[])
        return result