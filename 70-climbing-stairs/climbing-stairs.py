class Solution(object):
    d={}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        if n==1 or n==2:
            return n
        elif n in self.d:
            return self.d[n]
        else:
            self.d[n]= self.climbStairs( n-1)+self.climbStairs( n-2)
        return self.d[n]