from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q=deque()
        min=0
        f=[]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j,0))
                if grid[i][j]==1:
                    f.append((i,j))
        if len(f)==0:
            return 0
        while q:
            
            curr=q.popleft()
            r=curr[0]
            c=curr[1]
            time=curr[2]
            
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
                pass
            if (r-1>=0 and grid[r-1][c]==1 ) :
                grid[r-1][c]=2
                q.append((r-1,c,time+1))
                f.remove((r-1,c))
            if (r+1<len(grid)and grid[r+1][c]==1 ) :
                grid[r+1][c]=2
                q.append((r+1,c,time+1))
                
                
                f.remove((r+1,c))
            if  (c-1>=0 and grid[r][c-1]==1 ):
                grid[r][c-1]=2
                q.append((r,c-1,time+1))
            
                f.remove((r,c-1))
            if (c+1<len(grid[0]) and grid[r][c+1]==1 ):
                grid[r][c+1]=2
                q.append((r,c+1,time+1))
            
                f.remove((r,c+1))
            
        
        if len(f)==0:
            return time
        return -1
            