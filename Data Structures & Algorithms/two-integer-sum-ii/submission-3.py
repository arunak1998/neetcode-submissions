class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
       
       

        for i in range(len(numbers) - 1):
            l = i + 1
            while l < len(numbers):
                if numbers[i] + numbers[l] == target:
                    return [i+1, l+1]
                l += 1
        return []