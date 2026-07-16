class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        

        l=0
        r=0
        ans=0
        d={}
        while l<=r<len(fruits):
            
            
            if fruits[r] in d.keys():
                d[fruits[r]]+=1
                r+=1
            elif fruits[r] not in d.keys() and len(d)<2:
            
                d[fruits[r]]=1
                r+=1
            elif fruits[r] not in d.keys() and len(d)>=2:
                ans=max(ans,r-l)
                x=l
                while len(d)>=2 and x<len(fruits):
                    if len(d)<2:
                        break
                    d[fruits[x]]-=1
                    if d[fruits[x]]==0:
                        del d[fruits[x]]
                    x+=1
                l=x
                if r<l:
                    l=r
            
            
        if len(d)<=2:
            ans=max(ans,len(fruits)-l)
        return ans