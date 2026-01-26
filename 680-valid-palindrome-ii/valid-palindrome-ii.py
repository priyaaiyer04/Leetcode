class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s==s[::-1]:
            return True
        l=0
        r=len(s)-1
        c=0
        while l<r:
            print(l,r)
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                s1=s[0:l]+s[l+1:]
                if s1==s1[::-1]:
                    return True
                s1=s[0:r]+s[r+1:]
                if s1==s1[::-1]:
                    return True
                else:
                    return False