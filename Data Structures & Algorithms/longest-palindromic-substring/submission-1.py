class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        n, resindx,resLen= len(s), 0,0
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j]=True

                    if resLen<(j-i+1):

                        resindx=i
                        resLen=j-i+1

        return s[resindx:resindx+resLen]