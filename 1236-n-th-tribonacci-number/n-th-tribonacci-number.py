class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        d={}
        def f(n):
            if n==0 or n==1 :
                return n
            if n==2:
                return 1
            if n in d.keys():
                return d[n]
            else:
                d[n]=f(n-1)+f(n-2)+f(n-3)
                return d[n]
        f(n)
        if n==0 or n==1 :
                return n
        if n==2:
                return 1
        return d[n]