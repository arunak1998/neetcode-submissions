class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         

         duplicates={}
         for num in nums:

            if num  in duplicates:
                  duplicates[num]+=1
            else:
                duplicates[num]=1


         return  any(value > 1 for value in duplicates.values())