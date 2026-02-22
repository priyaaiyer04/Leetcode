class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        s=[]
        heights.append(0)
        maxarea=0
        h=0
        for i in range(len(heights)):
            while s and heights[i]<heights[s[-1]]:
                h=heights[s.pop()]
                w=i if not s else i-s[-1]-1
                maxarea=max(maxarea,h*w)
            s.append(i)
        return maxarea