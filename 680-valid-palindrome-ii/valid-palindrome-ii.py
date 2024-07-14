class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        l=[]
        x=0
        if s==s[::-1]:
            return True
        if len(s)==2:
            return True
        for i in s:
                    l.append(i)
        i=0
        for i in range(len(l)//2):
            if l[i]!=l[len(s)-i-1]:
                x=l.pop(len(l)-i-1)
                if l==l[::-1]:
                    return (True)
                    break
                else:
                    l.insert(len(l)-i,x)
                    x=l.pop(i)
                    if l==l[::-1]:
                        return (True)
                    
            
                return False          