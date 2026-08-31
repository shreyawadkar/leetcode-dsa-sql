class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_capacity = 0

        while left < right:
            width = right - left
            length = min(height[left], height[right])
            current_capacity = width * length

            max_capacity = max(max_capacity, current_capacity)
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        
        return max_capacity
        


































       