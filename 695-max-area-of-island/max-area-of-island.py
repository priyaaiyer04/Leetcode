class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def area(r,c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
                return 0
            if grid[r][c]==0:
                return 0
            elif (r,c) not in visited and grid[r][c]==1:
                visited.add((r,c))
                return 1+area(r-1,c)+area(r+1,c)+area(r,c-1)+area(r,c+1)
            return 0 
        sum1=0
        visited=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum1=max(sum1,area(i,j))
        return sum1