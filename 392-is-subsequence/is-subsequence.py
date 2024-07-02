class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1=[]
        s1=""
        if s in t:
            return True
        for i in t:
            if s.count(i)==0:
                
                t=t.replace(i,'')
        
        for i in t:
            if s.count(i)<t.count(i):
                c=0
                while c<t.count(i)-s.count(i):
                    
                    t=t.replace(i,'',1)
                    c+=1
        if t==s:
            return True
        return False
            