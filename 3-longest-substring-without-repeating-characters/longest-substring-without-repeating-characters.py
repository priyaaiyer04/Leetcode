class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l=0
        r=0
        ans=0
        l1=[]
        while l<=r<len(s):
            if s[r] in l1:
                
                ans=max(ans,r-l)
                oldl=l
                
                x=s[l:r+1].index(s[r])
                
                l+=x
                if l==oldl:
                    l+=1
                for i in s[oldl:l]:
                    l1.remove(i)
                if r<l:
                    r=l
            elif s[r] not in l1:
                l1.append(s[r])
                r+=1
           
        ans=max(ans,r-l)
        return ans