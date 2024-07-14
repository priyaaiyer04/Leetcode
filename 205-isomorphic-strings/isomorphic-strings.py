class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l=[]
        l1=[]
        for i in s:
            l.append(s.index(i))
        for i in t:
            l1.append(t.index(i))
        if l==l1:
            return (True)