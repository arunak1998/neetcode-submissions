class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        result=[]
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j=i+1
            k=len(nums)-1
            cum_sum=0

            while j<k:

                cum_sum=nums[i]+nums[j]+nums[k]

                if cum_sum==0:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    

                elif cum_sum<0:

                    j+=1

                else:
                    k-=1
        return result