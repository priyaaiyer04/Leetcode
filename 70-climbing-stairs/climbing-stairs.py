class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        d={}
        def stairs(n):
            if n==1 or n==2:
                return n
            if n in d:
                return d[n]
            else:
                d[n]=stairs(n-1)+stairs(n-2)
                return d[n]
        return stairs(n)