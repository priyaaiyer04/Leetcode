class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        src=(0,0)
        dst=(n-1,n-1)
        visited=set()
        queue=[(0,0,1)]
        while queue:
            curr=queue[0]
            queue=queue[1:]
            r=curr[0]
            c=curr[1]
            d=curr[2]
            if  r==dst[0] and c==dst[1]:
                return d
                break
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]==1:
                pass
            else:
                if (r,c) not in visited:
                    visited.add((r,c))
                    queue.append((r-1,c,d+1))
                    queue.append((r+1,c,d+1))
                    queue.append((r,c+1,d+1))
                    queue.append((r,c-1,d+1))
                    queue.append((r+1,c+1,d+1))
                    queue.append((r-1,c-1,d+1))
                    queue.append((r-1,c+1,d+1))
                    queue.append((r+1,c-1,d+1))
        return -1