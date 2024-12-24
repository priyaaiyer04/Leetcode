class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        x=0
        for i in range(0,len(flowerbed)-1):
            if i==0:
                if flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    x+=1
            
            if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
                flowerbed[i]=1
                x+=1
        if flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0:
                    flowerbed[len(flowerbed)-1]=1
                    x+=1
        if x>=n:
            return True
        else:
            return False

