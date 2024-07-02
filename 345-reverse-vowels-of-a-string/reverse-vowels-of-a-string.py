class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l1=[]
        l2=[]
        l=[]
        x=0
        for i in s:
            if i=='a'or i=='e'or i=='i' or i=='o'or i=='u' or i=='A'or i=='E'or i=='I' or i=='O'or i=='U':
                l.append(i)
                l1.append(x)
                x+=1
            else:
                l2.append(i)
                x+=1
        c=0
        s1=""
        l=l[::-1]
        for i in l1:
            l2.insert(i,l[c])
            c+=1
            
        for i in l2:
            s1+=i
        return s1