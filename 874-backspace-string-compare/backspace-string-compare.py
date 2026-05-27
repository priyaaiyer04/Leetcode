class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l=[]
        for i in s:
            if i=="#" and len(l)>0:
                l.pop()
            elif i!="#":
                l.append(i)
        l1=[]
        for i in t:
            if i=="#" and len(l1)>0:
                l1.pop()
            elif i!="#":
                l1.append(i)
        print(l,l1)
        if l==l1:
            return True
        return False