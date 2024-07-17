class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        for i in range(len(s)-1):
            s1=""
            s1=s[i]+s[i+1]
            l.append(s1)
        for i in l:
            if i in s and i in s[::-1]:
                return True
                break