class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def possible(start,combinations,sum_res):

            if sum_res==0:

                result.append(combinations[:])

                return
            if sum_res<0:
                return 

            
            for i in range(start,len(nums)):
                combinations.append(nums[i])
                possible(i,combinations,sum_res-nums[i])
                combinations.pop()

        result=[]
        possible(0,[],target)
        return result



