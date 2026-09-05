class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        d={}
        def dp(i,j):
            if i>=len(matrix) or j>=len(matrix[0]) or i<0 or j<0:
                return 0
           
            if (i,j) in d:
                return d[(i,j)]
            d[(i,j)]=1
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=x<len(matrix) and 0<=y<len(matrix[0]) and matrix[x][y]>matrix[i][j]:
                    d[(i,j)]=max(d[i,j],1+dp(x,y))
            return d[(i,j)]
        return max( dp(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])))