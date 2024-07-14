class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        l1=[]
        c=0
        for i in s:
            c+=1
            if i.isalpha():
                l.append(i)
            else :
                l1.append(c-1)
        l=l[::-1]
        for i in l1:
            l.insert(i,s[i])
        s1=""
        for i in l:
            s1+=i
        return (s1)