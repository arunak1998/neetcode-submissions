class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxi=nums[0]

        run_sum=0

        for num in nums:

            run_sum+=num
            maxi=max(maxi,run_sum)

            if run_sum<0:

                run_sum=0

           

        return maxi        