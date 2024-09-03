class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s1='abcdefghijklmnopqrstuvwxyz'
        s2=[]
        for i in s:
            s2+=str(int(s1.index(i))+1)
        s3=0
        i=0

        while i<k:
            s3=0
            for j in s2:
                s3+=int(j)
            s2=str(s3)
            
            i+=1
        return (s3)