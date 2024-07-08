class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        c=0
        i=0
        s1=""
        l=[]
        l2=[]
        for i in s:
            if i!=" ":
                s1+=i
            elif i==" " :
                l.append(s1)
                s1=""
        l.append(s1)
        for i in l:
            if len(i)>0:
                l2.append(i)
        return len(l2)
        