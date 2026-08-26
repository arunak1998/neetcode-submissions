class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi=0

        left=0

        right=len(heights)-1



        while left <right:

                height = min(heights[left], heights[right]) 

                width = right - left 

                capacity = height * width

                maxi=max(maxi,capacity)

                if heights[left] < heights[right]  :

                        left+=1

                elif heights[right] < heights[left]:

                        right-=1

                else:

                        left+=1

                        right-=1



                

        return maxi