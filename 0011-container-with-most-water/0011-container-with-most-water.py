class Solution(object):
    def maxArea(self, height):
        n=len(height)
        left=0
        right=n-1
        maximum_water=0
        while left<right:
            width=right-left
            heights=min(height[right],height[left])
            total_water=heights*width
            maximum_water=max(total_water,maximum_water)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maximum_water
        