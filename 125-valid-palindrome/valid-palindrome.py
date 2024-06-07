class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        l=[]
        for i in s:
            if i.isalpha() or i.isdigit():
                    l.append(i)
        s=""
        for i in l:
            s+=i
        s1=s[::-1]    
        if s1==s:
            return True
        else:
            return False
        