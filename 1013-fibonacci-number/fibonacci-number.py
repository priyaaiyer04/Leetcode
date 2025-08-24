class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        d={}
        def f(n):
            if n==1 or n==0:
                return n
            if n in d.keys():
                return d[n]
            else:
                d[n]=f(n-1)+f(n-2)
                return d[n]
        f(n)
        if n==0 or n==1:
            return n
        return d[n]
        