class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        def dfs(i,sub):

            
            result.append(sub[:])

            for j in range(i,len(nums)):

                sub.append(nums[j])
                dfs(j+1,sub)
                sub.pop()

        result=[]
        dfs(0,[])
        return result

