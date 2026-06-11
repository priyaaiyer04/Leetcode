class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        d={}
        for i in s:
            d[i]=0
        l=0
        r=0
        max1=-1
        ans=0
        while l<=r<len(s):
            d[s[r]]+=1
            max1=max(d[s[r]],max1)
            if r-l-max1>=k:
                ans=max(ans,r-l)
               
                d[s[l]]-=1
                l=l+1
                r+=1
            else:
                r+=1
            
        ans=max(ans,r-l)
        return ans