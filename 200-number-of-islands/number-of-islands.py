class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        sum1=0
        def count_island(r,c):
            if r>=len(grid) or c>=len(grid[0]) or r<0 or c<0:
                return 0
            if grid[r][c]=="1":
                    grid[r][c] = "0"
                    count_island(r-1,c)
                    count_island(r+1,c)
                    count_island(r,c+1)
                    count_island(r,c-1)
                    return 1
            else:
                    return 0    
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum1+=count_island(i,j)
        return sum1