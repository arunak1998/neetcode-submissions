class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        def dp(nums):
            prev2 = 0
            prev = 0

            for i in range(len(nums)):
                pick = nums[i] + prev2
                notpick = prev

                curr = max(pick, notpick)

                prev2 = prev
                prev = curr

            return prev

        return max(dp(nums[1:]),dp(nums[:-1]))