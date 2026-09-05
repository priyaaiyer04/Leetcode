class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        d={}
        def dp(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return 0
            if (i,j) in d:
                return d[(i,j)]
            if grid[i][j]=="1":
                grid[i][j]=0
                dp(i+1,j)
                dp(i-1,j)
                dp(i,j+1)
                dp(i,j-1)
                return 1
            else:
                return 0
            return d[(i,j)]
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans+=dp(i,j)
        return ans