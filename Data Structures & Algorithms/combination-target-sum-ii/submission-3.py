class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        def backtrack(i,l1,target_sum):
            if target_sum==target:

                result.append(l1[::])
                return
            if i==len(candidates) or target_sum>target:
                
                return
                    

            
            
            l1.append(candidates[i])
            backtrack(i+1,l1,target_sum+candidates[i])

            l1.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1,l1,target_sum)

        result=[]
        candidates.sort()

        backtrack(0,[],0)

        return result


