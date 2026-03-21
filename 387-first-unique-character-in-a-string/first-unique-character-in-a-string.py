class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.count(s[0])==len(s) and len(s)>1:
            return -1
        d={}
        for i in s:

            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1  
        print(d)
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1