class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        left = 0
        maxi = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])

            window = right - left + 1
            replacements_needed = window - max_freq

            if replacements_needed > k:
                freq[s[left]] -= 1
                left += 1

            maxi = max(maxi, right - left + 1)

        return maxi