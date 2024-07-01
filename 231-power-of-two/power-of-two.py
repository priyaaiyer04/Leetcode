import math
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        if n<0:
            return False
        a=math.log(n, 2)
        if 2**int(a)==n :
            return True
        return False