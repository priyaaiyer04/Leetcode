class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        
        l=0
        r=0
        l1=list(p)
        ans=[]
        while l<=r<len(s):
            if s[r] in p:
                x=len(p)+l
                flag=-1
                if x>len(s):
                    x=len(s)
                while r<x:
                    if s[r] in l1:
                        l1.remove(s[r])
                        r+=1
                    else:
                        if s[r] in p and s[r] not in l1:
                            flag=0
                        break
                if len(l1)==0:
                    
                    ans.append(l)
                    l1.append(s[l])
                    l+=1
                    if r<l:
                        r=l
                        l1=list(p)
                    
                elif flag==-1:
                    
                    r+=1
                    l=r
                    l1=list(p)
                else:
                    
                    l1.append(s[l])
                    l+=1
                    if r<l:
                        r=l
                        l1=list(p)
                
            elif s[r] not in p:
                
                r+=1
                l=r
                l1=list(p)
        return ans