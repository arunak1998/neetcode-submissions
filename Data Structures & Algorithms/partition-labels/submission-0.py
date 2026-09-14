class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dis = {}

        for i in range(len(s)):
            dis[s[i]] = i

        start = 0
        farthest_boundary = -1
        res = []

        for i in range(len(s)):
            farthest_boundary = max(farthest_boundary, dis[s[i]])

            if i == farthest_boundary:
                length = i - start + 1
                res.append(length)
                start = i + 1

        return res