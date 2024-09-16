class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        l=[]
        for i in intervals:
                    l.append(i)
        l.sort(key = lambda x: x[1])
        #print(l)
        c=0
        i=0
        c=0
        end = float('-inf')
        for i in l:
            if i[0]<end:
                c+=1
            else:
                end=i[1]
        return (c)