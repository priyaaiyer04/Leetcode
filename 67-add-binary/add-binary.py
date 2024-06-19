class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        
        a=a[::-1]
        sum=0
        x=0
        for i in a:
                sum=sum+((2**x)*int(i))
                x+=1
       
        sum1=0
        b=b[::-1]
        x=0
        for i in b:
                sum1=sum1+((2**x)*int(i))
                x+=1

        c=sum+sum1
        l=[]
        while c>1:
            a1=c%2
            c=c//2
            l.append(a1)
        l.append(c)
        l.reverse()
        s=""
        for i in l:
            s+=str(i)
        return s
                