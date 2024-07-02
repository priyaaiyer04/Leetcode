import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        if n<=0 or n%2==0:
            return False
        a=math.log(n,3)
        a=(round(a))
        if 3**a==n and int(a)//a==1:
            return True
        return False
            
        