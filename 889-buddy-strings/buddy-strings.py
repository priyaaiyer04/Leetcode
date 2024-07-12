class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        c=0
        y=0
        l=[]
        l1=[]
        x=0
        if len(s)!=len(goal):
            return False
        if goal==s and len(s)<2:
            return False
        for i in s:
            if s.count(i)==len(s):
                return True
        
        if goal==s and len(s)>2:
            for i in s:
                if s.count(i)==1:
                    y+=1
            if y==len(s):
                return False
            return True
        
        for i in s:
            if s.count(i)==goal.count(i):
                c+=1
        if c!=len(s):
            return (False)
        if c==len(s):
            for i in range(len(s)):
                if s[i]!=goal[i]:
                    x+=1
        
        if x==2:
            return (True)
        
        