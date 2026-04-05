
class Solution(object):
    def findGoodIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
       
        l=[]
        d={}
        ans=[]
        x=2*int(n**(0.33))
        
        for i in range(1,x+1):
            for j in range(i+1,x+1):
                if i!=j:
                    if i**3+j**3 in d:
                        d[i**3+j**3]+=1
                    else:
                        d[i**3+j**3]=1
        
        for i in d:
            if d[i]>1 and i<=n:
                ans.append(i)
        ans.sort()
        return ans
        