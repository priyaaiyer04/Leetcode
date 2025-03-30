class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l=[]
        if numRows==1:
            return s
        for i in range(numRows):
            l1=[]
            for j in range(2*numRows+500):
                l1.append("")
            l.append(l1)
        i=0
        j=0
        while s:
            if i==0:
                if j!=0:
                    i+=1
                while i<numRows and s:
                    
                    l[i][j]=s[0]
                    
                    s=s[1:len(s)]
                    i+=1
            if i==numRows:
                while i>0 and s:
                    i-=1
                    if i==0:
                        break
                    j+=1
                    l[i-1][j]=s[0]
                    s=s[1:len(s)]

        s=""
        for i in l:
            s1="".join(i)
            s+=s1
        return s
                        