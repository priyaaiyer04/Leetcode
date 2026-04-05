class Solution(object):
    def mirrorFrequency(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1="abcdefghijklmnopqrstuvwxyz"
        s2=s1[::-1]
        s3="0123456789"
        s4=s3[::-1]
        d={}
        for i in range(len(s1)):
            d[s1[i]]=s2[i]
            d[s2[i]]=s1[i]
        for i in range(len(s3)):
            d[s3[i]]=s4[i]
            d[s4[i]]=s3[i]
        sum1=0
        visited=[]
        for i in s:
            l=[i,d[i]]
            l.sort()
            if l not in visited:
                sum1+=abs(s.count(i)-s.count(d[i]))
                
                visited.append(l)
        return sum1