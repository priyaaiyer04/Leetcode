class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x1=abs(x)
        x1=str(x1)
        a=x1[::-1]
        a1=0
        if x<0:
            a1=-int(a)
        else:
            a1=int(a)
        if a1.bit_length()<32:
            return a1
        else :
            return 0

