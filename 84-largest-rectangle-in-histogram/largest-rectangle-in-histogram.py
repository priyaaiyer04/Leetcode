class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        s=[]
        maxarea=0
        x=[]
        for i in range(len(heights)):
            
            start=i
            while len(s)>0 and s[-1][1]>heights[i]:
                x=s.pop()
                w=i-x[0]
                h=x[1]
                maxarea=max(maxarea,h*w)
                start=x[0]
            s.append([start,heights[i]])

        for i in s:
            
            maxarea=max((len(heights)-i[0])*i[1],maxarea)
            
        return maxarea