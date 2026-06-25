class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l=[]
        l.append(n)
        x=str(n)
        while True:
            
            ans=0
            for i in x:
                ans+=int(i)**2
            if ans==1:
                return True
            if ans in l:
                return False
            l.append(ans)
            x=str(ans)
        