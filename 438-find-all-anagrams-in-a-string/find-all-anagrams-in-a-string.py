class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        l=0
        r=l
        t=p
        c=list(t)
        mins=""
        s1=""
        l1=[]
        while l<len(s):
                    if len(c)==0:
                        if len(s1)==len(t):
                                    l1.append(l)
                        if s1[0] in t and t.count(s1[0])>s1[1:].count(s1[0]):
                            
                            c.append(s1[0])
                        
                        l+=1
                        s1=s1[1:]
                        
                    elif r<len(s):
                        s1+=s[r]
                        if s[r] in c:
                            c.remove(s[r])
                        r+=1
                        
                    
                    elif r==len(s) :
                        
                        if s1[0] in t and t.count(s1[0])>s1[1:].count(s1[0]):
                            if len(c)==0 :
                                if len(s1)==len(t):
                                    l1.append(l)
                                print("hi",c,s1,mins)
                                c.append(s1[0])
                        s1=s1[1:]
                        l+=1
        return l1