class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        d={}
        def dp(i,j):
            if i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if (i,j) in d:
                return d[(i,j)]
            d[(i,j)]=dp(i+1,j) + dp(i,j+1)
            return d[(i,j)]
        return dp(0,0)
            