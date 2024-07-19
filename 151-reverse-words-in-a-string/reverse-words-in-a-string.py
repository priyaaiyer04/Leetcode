class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l1=[]
        s1=""
        for i in s:
            if i.isalpha() or i.isdigit():
                s1+=i
            else:
                if len(s1)>0:
                    l1.append(s1)
                s1=""
        if len(s1)>0:
            l1.append(s1)
        
        l1=l1[::-1]
        s1=" ".join(l1)
        
        return s1