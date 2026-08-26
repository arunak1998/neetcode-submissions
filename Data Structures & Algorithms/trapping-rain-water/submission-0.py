class Solution:
    def trap(self, height: List[int]) -> int:

        maxleft = [0] * len(height)
        maxright = [0] * len(height)

        maxleft[0] = height[0]
        maxright[-1] = height[-1]

        for i in range(1, len(height)):
            maxleft[i] = max(height[i], maxleft[i - 1])

        for i in range(len(height) - 2, -1, -1):
            maxright[i] = max(height[i], maxright[i + 1])

        result=0

        for i in range(len(height)):

            h=min(maxright[i],maxleft[i])-height[i]
            h=max(0,h)
            result+=h
        return result
            





        
        