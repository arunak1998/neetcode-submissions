class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi=0
        nums_set=set(nums)
        for num in nums:
            if num - 1 not in nums_set:
            
                n=num

                seq_length=1

            

                while n+1 in nums_set:

                    seq_length+=1

                    n=n+1

                maxi=max(maxi,seq_length)

        return maxi