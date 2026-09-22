class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev = 0

        for i in range(len(nums)):
            pick = nums[i] + prev2
            notpick = prev

            curr = max(pick, notpick)

            prev2 = prev
            prev = curr

        return prev