class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x=0
        c=0
        x1=0
        for i in s:
            if i.isdigit():
                x+=1
            if i=='e' or i=='E':
                c+=1
            if i=='.':
                x1+=1
            
        if x==0:
            return False
        if c==1 and x<=1:
            return False
        if c==1 and x1==1:
            if s.index('.')==0 and s[1]=='e':
                return False
        x=0
        for i in range(len(s)):
            if s[i].isdigit():
                x+=1
            if s[i]=='.' and s.count(s[i])==1 and len(s)>1 :
                x+=1
            if s[i]=='e' and s.count(s[i])==1 and i!=len(s)-1 and i!=0 and (s[i-1].isdigit()or s[i-1]=='.') :
                x+=1
                if (s[i:len(s)]).count('.')!=0:
                    x-=1
                
            if s[i]=='E' and s.count(s[i])==1 and i!=len(s)-1 and i!=0 and (s[i-1].isdigit()or s[i-1]=='.') :
                x+=1   
                if (s[i:len(s)]).count('.')!=0:
                    x-=1
            if s[i]=='+'  and  s.count('-')==0 and(i==0 or s[i-1]=='e' or s[i-1]=='E') :
                x+=1
            if s[i]=='-' and s.count(s[i])==1 and s.count('+')==0 and (i==0 or s[i-1]=='e' ) :
                x+=1
            if s[i]=='-':
                if s.count('e')==1 and s.count('+')==1 and s.count('.')==1:
                    if s.index('.')<s.index('e') and s.index('e')<s.index('+'):
                        x+=2
            if s[i]=='+':
                if s.count('e')==1 and s.count('-')==1 and s.count('.')==1:
                    if s.index('.')<s.index('e') and s.index('e')<s.index('-'):
                        x+=2 
            
        if x==len(s):
            return True
        return False