class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp = [0] * len(s)
        dp[0] = 1

        for i in range(1, len(s)):
            res = 0

            if s[i] != "0":
                res += dp[i - 1]

            if s[i - 1] == "1" or (s[i - 1] == "2" and s[i] in "0123456"):
                if i == 1:
                    res += 1
                else:
                    res += dp[i - 2]

            dp[i] = res

        return dp[len(s) - 1]