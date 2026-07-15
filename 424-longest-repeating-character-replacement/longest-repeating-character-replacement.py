class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        l=0
        r=0
        ans=0
        d={}
        max_c=s[0]
        for i in s:
            d[i]=0
        while l<=r<len(s):

            while max_c in d and r-l-d[max_c]<=k:
                if r<len(s):
                    d[s[r]]+=1
                    if ( max_c in d.keys() and d[s[r]]>d[max_c]) or max_c=="":
                        max_c=s[r]
                    r+=1
                    
                elif r>=len(s):
                    break
            else:
                ans=max(ans,r-l-1)
                d[s[l]]-=1
                for i in d:
                    if (max_c in d and d[i]>d[max_c]) or max_c=="":
                        max_c=i
                if d[s[l]]<0:
                    d[s[l]]=0
                l+=1
                if r<l:
                    r=l
        if len(s)-l-d[max_c]<=k:
          
            ans=max(ans,len(s)-l)      
        return ans