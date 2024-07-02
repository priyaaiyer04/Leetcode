import math
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        if n<=0:
            return False
        a=math.log(n,4)
        
        if 4**a==n and int(a)//a==1:
            return True
        return False