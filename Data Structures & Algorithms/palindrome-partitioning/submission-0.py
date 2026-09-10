class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[] 
        path=[] 
        def dfs(i):  

            if i==len(s):

                    result.append(path[:])

                    return 



            for j in range(i,len(s)):

                if isplaindrome(i,j):

                        path.append(s[i:j+1])

                        dfs(j+1)

                        path.pop()

        def isplaindrome(i,j):

            while i<j:

                if s[i]!=s[j]:

                        return False

                i=i+1

                j=j-1



            return True



        dfs(0)
        return result


