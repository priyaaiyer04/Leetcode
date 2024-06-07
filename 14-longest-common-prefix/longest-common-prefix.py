class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l=[]
        l1=[]
        l2=[]
        x=min(strs,key=len)
        y=len(x)
        print(y)
        for i in strs:
                l1.append(i[0:y])
        for j in l1:
            for i in range(y+1):
                l2.append(j[0:i])
        for x in l2:
            if  l2.count(x)==len(strs):
                l.append(x)
        return( max(l,key=len))
    
            
        