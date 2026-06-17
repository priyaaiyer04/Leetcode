class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t in s:
            return t
        l=0
        r=0
        ans=""
        l1=list(t)
        while l<=r<=len(s):
            if len(l1)==0:
                if len(s[l:r])<len(ans) or len(ans)==0:
                    ans=s[l:r]
                x=l
                while l<r:
                    if s[l] in t and t.count(s[l])>s[l+1:r].count(s[l]):
                        break
                    elif s[l] not in t:
                        l+=1
                    else:
                        l+=1
            
                if l==x:
                    l1.append(s[l])
                    l+=1
                    while l<r and s[l] not in t:
                        l+=1
                    
            
            elif r<len(s) and s[r] in l1:
                l1.remove(s[r])
                r+=1
            else:
                r+=1
        
        return  ans