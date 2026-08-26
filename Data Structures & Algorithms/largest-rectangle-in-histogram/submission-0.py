class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] >= height:
                index, h = stack.pop()
                maxarea = max(maxarea, (i - index) * h)
                start = index

            stack.append((start, height))

        for i, h in stack:
            maxarea = max(maxarea, (len(heights) - i) * h)

        return maxarea