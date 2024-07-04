class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1=""
        c=0
        if "+-" in s:
            return 0
                
        for i in range(len(s)):
            if s[i]==" " and len(s1)==0:
                continue
            if s[i].isalpha():
                
                break
            if s[i]==" " and len(s1)>0:
                break
            if s[0]=='-':
                
                c=-1
            
            if s[i]=='-' and s.count("+")==0 :
                if s[:i].isspace() or i==0:
                    c=-1
                else:
                    break
            if s[i]=="+" and len(s1)>1:
                break
            if s[i]=='+' and c==-1 :
                break
            if i<len(s)-1 and s[i]=='+'and s[i+1]==" " :
                break
            if i<len(s)-1 and s[i]=='+'and s[i+1]=="+":
                break
            if s[i].isdigit():
                s1+=s[i]
            if s[i]==".":
                break
       
        if  len(s1)==0:
            s1="0"
        s1=int(s1)
        if c==-1:
            s1=-s1
        if s1<-2147483648:
            return -2147483648
        if s1>2147483647:
            return 2147483647
        return s1