class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        max_val = 2**31 - 1
        min_val = -(2**31)

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > max_val // 10 or (res == max_val // 10 and digit > max_val % 10):
                return 0

            if res < min_val // 10 or (res == min_val // 10 and digit < min_val % 10):
                return 0

            res = res * 10 + digit

        return res