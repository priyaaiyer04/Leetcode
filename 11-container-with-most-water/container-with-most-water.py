class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area with the current pair of heights
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            
            # Move the pointer corresponding to the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
