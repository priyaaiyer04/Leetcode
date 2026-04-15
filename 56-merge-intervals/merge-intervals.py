class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        start=intervals[0]
        intervals=intervals[1:]
        l=[]

        for i in intervals:
            if i[0] in range(start[0],start[1]+1):
                start=[min(i[0],start[0]),max(i[1],start[1])]
            
            else:
                l.append(start)
                start=i
            
        l.append(start)
        return l