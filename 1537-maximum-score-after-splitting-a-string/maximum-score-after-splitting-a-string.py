class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[]
        for i in range(len(s)):
            s1=s[0:i+1]
            s2=s[i+1:len(s)]
            
            if len(s1)>0 and len(s2)>0:
                print(s1,s2)
                l.append(s1.count("0")+s2.count("1"))
        return max(l)