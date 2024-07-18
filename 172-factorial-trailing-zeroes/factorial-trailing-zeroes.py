class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=math.factorial(n)
        x=str(x)
        y=x[::-1]
        y=int(y)
        y=str(y)
        return (len(x)-len(y))
        