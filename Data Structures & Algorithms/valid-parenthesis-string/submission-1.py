class Solution:
    def checkValidString(self, s: str) -> bool:


        leftmin=0
        leftmax=0
        

        for i in range(len(s)):
            if s[i] == '(':
                leftmin+=1
                leftmax+=1



            elif s[i] == ')':
                leftmin-=1
                leftmax-=1
            
            else:
                leftmin-=1
                leftmax+=1

            if leftmin<0:
                leftmin=0

            if leftmax<0:
                return False

        return leftmin==0



        def dfs(i, open):
         
            if open < 0:
             return False

            if i == len(s):
                return open == 0

            if s[i] == '(':
                return dfs(i + 1, open + 1)

            if s[i] == ')':
                return dfs(i + 1, open - 1)

            return (
                dfs(i + 1, open - 1) or
                dfs(i + 1, open + 1) or
                dfs(i + 1, open)
            )

        return dfs(0, 0)