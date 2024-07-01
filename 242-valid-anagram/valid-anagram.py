class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x=0
        if len(s)==len(t):
            for i in s:
                if s.count(i)==t.count(i):
                    x+=1
        if x==len(s):
            return True
        return False
        