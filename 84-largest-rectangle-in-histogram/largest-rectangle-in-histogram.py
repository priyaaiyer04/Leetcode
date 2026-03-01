class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        heights.append(0)
        maxarea=0
        for i in range(len(heights)):
            while len(stack)>0 and heights[stack[-1]]>heights[i]:
                x=stack.pop()
                if len(stack)>0:
                    w=i-stack[-1]-1
                    h=heights[x]
                    maxarea=max(w*h,maxarea)
                else:
                    h=heights[x]
                    maxarea=max(i*h,maxarea)
            stack.append(i)
        return maxarea