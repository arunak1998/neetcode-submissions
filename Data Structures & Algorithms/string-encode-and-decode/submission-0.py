class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []

        for s in strs:
            length = len(s)
            parts.append(str(length))
            parts.append("#")
            parts.append(s)

        encoded = ''.join(parts)

        return encoded
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i

            while s[j].isdigit():
                j += 1

            length = int(s[i:j])

            j += 1  # skip '#'

            ans.append(s[j:j + length])

            i = j + length

        return ans
