class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=[]
        for i in s:
            print(s1)
            if i=="#":
                if len(s1)>0:
                    s1.pop()
            else:
                s1.append(i)
        t1=[]
        for i in t:
            print(t1)
            if i=="#":
                if len(t1)>0:
                    t1.pop()
            else:
                t1.append(i)
        if s1==t1:
            return True
        return False