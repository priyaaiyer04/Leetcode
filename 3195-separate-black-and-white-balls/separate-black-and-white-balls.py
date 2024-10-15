class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        s1=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="1":
                s1+=c
            else:
                c+=1
        return (s1)
                