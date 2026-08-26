class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1 = {}
        k = len(s1)

        for char in s1:
            f1[char] = f1.get(char, 0) + 1

            f2 = {}
            left = 0

        for right in range(len(s2)):
            f2[s2[right]] = f2.get(s2[right], 0) + 1

            window_size = right - left + 1

            if window_size > k:
                f2[s2[left]] -= 1

                if f2[s2[left]] == 0:
                    del f2[s2[left]]

                left += 1

            if f1 == f2:
                return True

        return False