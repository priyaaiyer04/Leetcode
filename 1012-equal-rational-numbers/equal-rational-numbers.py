class Solution(object):
    def isRationalEqual(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=""
        s2=""
        s3=""
        t1=""
        t2=""
        t3=""
        for i in s:
            if i.isdigit():
                s1+=i
            else:
                break
            
        for i in t:
            if i.isdigit():
                t1+=i
            else:
                break
        i=0
        if s.count('.')==1:
            x=s.index('.')
            s2+=s[x]
            while x<len(s):
                if s[x].isdigit():
                    s2+=s[x]
                x+=1
        if t.count('.')==1:
            x=t.index('.')
            t2+=t[x]
            while x<len(t):
                if t[x].isdigit():
                    t2+=t[x]
                x+=1
        if s.count('(')==1:
            x=s.index('(')
            
            while x<len(s):
                if s[x].isdigit():
                    s3+=s[x]
                x+=1

        if t.count('(')==1:
            x=t.index('(')
            while x<len(t) and t[x]!=')':
                if t[x].isdigit():
                    t3+=t[x]
                x+=1       
        s1=s1+s2+s3
        t1=t1+t2+t3
        if len(s3)==0  and len(t3)==0:
            if float(s1)==float(t1):
                return True
            print("a")
            return False
       
        if float(s1)==float(t1):
            return True
        if len(t1)>len(s1) :
            for i in t1:
                if s1.count(i)==0:
                    break
            else:return True
        if len(s1)>len(t1) and not('9' in s3 or '9'in t3):
            for i in s1:
                if t1.count(i)==0:
                    break
            else:
                return True
        if '9' in t3:
            x=t2.index('9')
            t1=float(t1)+(10**-(x+1))
            t1=str(t1)
            
        if '9' in s3:
            x=s2.index('9')
            s1=float(s1)+(10**-(x+1))
            s1=str(s1)
        if float(s1)==float(t1):
            
            return True    
        if '9' in s3 or '9'in t3 :
            if round(float(s1))==round(float(t1)):
                
                return(True)