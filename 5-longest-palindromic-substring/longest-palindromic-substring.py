class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        c=1
        l=[]
        if s==s[::-1]:
            return s
        while i<len(s):
            c=1
            while c<=len(s):
                if s[i:c]==s[i:c][::-1] and len(s[i:c])!=0:
                    l.append(s[i:c])
                c+=1
            i+=1     
        return(max(l,key=len))