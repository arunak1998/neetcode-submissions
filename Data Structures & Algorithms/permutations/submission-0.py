class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def possible(start,permu):
            if len(permu)==len(nums):
                result.append(permu[:])
                return

            for i in range(start,len(nums)):
                if nums[i] in permu:
                   continue
                permu.append(nums[i])
                possible(start,permu)
                permu.pop()

        result=[]

        possible(0,[])
        return result
