class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t)>len(s):
            return ""
        if t in s:
            return t
        s1=sorted(s)
        t1=sorted(t)
        if t1 in s1:
            return t
        l=0
        r=l
        c=list(t)
        mins=""
        s1=""
        while l<len(s):
            
            
            if len(c)==0:
                if len(s1)<len(mins) or len(mins)==0:
                    mins=s1
                if s1[0] in t and t.count(s1[0])>s1[1:].count(s1[0]):
                    
                    c.append(s[l])
                l+=1
                s1=s1[1:]
            elif r<len(s):
                s1+=s[r]
                if s[r] in c:
                    c.remove(s[r])
                r+=1
            elif r==len(s) :
                if s1[0] in t and t.count(s1[0])>s1[1:].count(s1[0]):
                    if len(c)==0 and (len(s1)<len(mins) or len(mins)==0):
                        mins=s1
                        c.append(s1[0])
                s1=s1[1:]
                l+=1
            
        return (mins)