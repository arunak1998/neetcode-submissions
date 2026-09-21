class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = (2 ** 32) - 1

        for _ in range(32):
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        if a > (2 ** 31) - 1:
            a -= 0x100000000

        return a
        