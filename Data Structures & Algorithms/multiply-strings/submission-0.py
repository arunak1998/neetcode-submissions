class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
                return "0"
        m = len(num1)
        n = len(num2)

        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                result[i + j + 1] += product

                result[i + j] += result[i + j + 1] // 10
                result[i + j + 1] %= 10

        i=0
        while i<len(result) and result[i]==0:
            i+=1

        ans = ""

        for i in range(i, len(result)):
            ans += str(result[i])

        return ans


        