class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        d={}
        def dp(i,j):
            if i>=len(grid) or j>=len(grid[0]):
                return float('inf')
            if i==len(grid)-1 and j==len(grid[0])-1:
                return grid[i][j]
            if (i,j) in d:
                return d[(i,j)]
            d[(i,j)]=min(grid[i][j]+dp(i+1,j),grid[i][j]+dp(i,j+1))
            return d[(i,j)]
        return dp(0,0)