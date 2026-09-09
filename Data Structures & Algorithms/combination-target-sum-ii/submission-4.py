class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def dfs(i,comb,target):

            if target==0:
                result.append(comb[:])
                return

            if target <0 or i==len(candidates):
                return

            for j in range(i, len(candidates)):

                if j > i and candidates[j] == candidates[j-1]:
                    continue

                comb.append(candidates[j])

                dfs(j + 1, comb, target - candidates[j])

                comb.pop()
                  

               


        result=[]
        dfs(0,[],target)
        return result

                
                