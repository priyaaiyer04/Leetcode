class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l1=[]
        for i in letters:
            l1.append(ord(i)-ord(target))
        l1.sort()
        x=l1.index(min(l1))
        c=0
        for i in l1:
            if i<=0:
                c+=1
        if c==len(l1):
            return letters[x]
        if l1[x]<=0:
            while l1[x]<=0 and x<len(l1)-1:
                x=x+1
                
        return letters[x]