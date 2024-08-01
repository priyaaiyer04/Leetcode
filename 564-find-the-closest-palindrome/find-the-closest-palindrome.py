class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        if len(n)>15 and len(n)%2!=0:
            a=n[0:len(n)//2]
            a=a+str(int(n[(len(n)//2)+1])-2)+a[::-1]
            return a  
        if len(n)>10 and n!=n[::-1]:

            a=n[0:len(n)//2]
            a=a+a[::-1]
            if int(a[(len(a)//2)-1])>=1:
                b=a[0:(len(a)//2)-1]+str(int(a[(len(a)//2)-1])-1)
                b=b+b[::-1]
                c=a[0:(len(a)//2)-1]+str(int(a[(len(a)//2)-1])+1)
                c=c+c[::-1]
                print(a,b,c)
            else:
                b=a[0:(len(a)//2)-1]+str(int(a[(len(a)//2)-1])+1)
                b=b+b[::-1]
                c=a[0:(len(a)//2)-1]+str(int(a[(len(a)//2)-1])+1)
                c=c+c[::-1]
            if abs(int(n)-int(b))<abs(int(n)-int(a)):
                if abs(int(n)-int(b))<abs(int(n)-int(c)):
                    return b
                else:
                    return c
            if abs(int(n)-int(a))<abs(int(n)-int(c)):
                return a
            return c
        
        x=str(int(n)-1)
        y=str(int(n)+1)
        if len(n)==1:
            return str(int(n)-1)
        
        while x!=x[::-1] and y!=y[::-1] :
            x=str(int(x)-1)
            y=str(int(y)+1)
           
        if x==x[::-1]:
            return x
        if y==y[::-1]:
            return y