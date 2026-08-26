class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sets(start,pairs):

           
            
            result.append(pairs[:])

            for i in range(start,len(nums)):
                if nums[i] in pairs:
                    continue
                pairs.append(nums[i])
                sets(i+1,pairs)
                pairs.pop()

        result=[]

        sets(0,[])
        return result

