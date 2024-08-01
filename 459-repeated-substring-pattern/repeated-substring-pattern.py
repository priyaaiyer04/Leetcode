class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=""
        if len(s)==2 and s.count(s[0])==1:
            return False
        if len(s)==1:
            return False
        for i in s:
            if s1.count(i)==0:
                s1+=i
        x=s.count(s1)
        if x*len(s1)==len(s):
                return True
        s2=""
        i=0
        while x*s2!=s and i<len(s):
    
            s2+=s[i]
            x=s.count(s2)
            i+=1
        if x>1:
            return True