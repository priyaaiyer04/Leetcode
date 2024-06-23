class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        l=[]
        while n>1:
            a1=n%2
            n=n//2
            l.append(a1)
        l.append(n)
        l.reverse()
        s=""
        for i in l:
            s+=str(i)
        for i in s:
            if i=='1':
                c+=1
        print(c)
        return c