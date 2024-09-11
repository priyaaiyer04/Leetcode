class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        c=0
        x=bin(start)
        y=bin(goal)
        x=x[2:len(x)]
        y=y[2:len(y)]
        if len(x)<len(y):
            z=len(y)-len(x)
            x="0"*z+x
        elif len(x)>len(y):
            z=len(x)-len(y)
            y="0"*z+y
        for i in range(len(x)-1,-1,-1):
            if x[i]!=y[i]:
                c+=1
        return (c)