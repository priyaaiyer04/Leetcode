from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        q=deque()
        q.append((sr,sc))
        while q:
            curr=q.popleft()
    
            r=curr[0]
            c=curr[1]
            
            if r-1>=0 and image[r-1][c]!=color and image[r-1][c]==image[r][c]:
                q.append((r-1,c))
            if c-1>=0 and image[r][c-1]!=color and image[r][c-1]==image[r][c]:
                q.append((r,c-1))
            if r+1<len(image) and image[r+1][c]!=color and image[r+1][c]==image[r][c]:
                q.append((r+1,c))
            if c+1<len(image[0]) and image[r][c+1]!=color and image[r][c+1]==image[r][c]:
                q.append((r,c+1))
            image[r][c]=color
        return image