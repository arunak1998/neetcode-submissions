class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            total = 0
            while n > 0:
                last = n % 10
                total += last ** 2
                n = n // 10

            n = total

        return True