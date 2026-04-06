class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        d={}
        def c(n):
            if n==1 or n==2:
                return n
            if n in d:
                return d[n]
            else:
                d[n]= c(n-1)+c(n-2)
                return d[n]
        return c(n)