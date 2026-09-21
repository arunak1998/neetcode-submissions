class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xFFFFFFFF

        for _ in range(32):
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        if a > 0x7FFFFFFF:
            a -= 0x100000000

        return a
        