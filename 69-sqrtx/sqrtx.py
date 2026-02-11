
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l=0
        u=x//2+1
        print(u)
        while l<=u:
            m=(l+u)//2
            print(l,u,m)
            if m*m==x:
                
                return m
                
            elif m*m>x:
                u=m-1
            elif m*m<x:
                if (m+1)*(m+1)>x:
                    
                    return m
                    break
                l=m+1
        return m