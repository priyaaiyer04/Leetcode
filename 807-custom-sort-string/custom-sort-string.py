class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        d={}
        s1=""
        for i in s:
            if i not in d.keys():
                d[i]=i
            else:
                d[i]=d[i]+i
        for i in order:
            if i in d.keys():
                s1+=d[i]
        for i in s:
            if s1.count(i)!=s.count(i):
                s1+=i*(s.count(i)-s1.count(i))
        return s1


