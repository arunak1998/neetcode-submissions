class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        left = 0
        maxi = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while freq[s[right]] > 1:
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

            maxi = max(maxi, right - left + 1)

        return maxi