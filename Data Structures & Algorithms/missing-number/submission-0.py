class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        total_sum=0

        for i in range(len(nums)+1):
            total_sum+=i

        actual_sum=0
        for i in range(len(nums)):

            actual_sum+=nums[i]

        return total_sum-actual_sum
        