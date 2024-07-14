class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        l1=[]
        l=[]
        l2=[]
        s=""
        for i in s1:
            if ord(i) in range(ord('a'),ord('z')+1):
                s+=i
            else:
                l.append(s)
                s=""
        l.append(s)
        s=""
        for i in s2:
            if ord(i) in range(ord('a'),ord('z')+1):
                s+=i
            else:
                l1.append(s)
                s=""
        l1.append(s)
        for i in l:
            l2.append(i)
        for i in l1:
            l2.append(i)
        l3=[]
        for i in l2:
            
            if l1.count(i)==0 and l.count(i)==1:
                l3.append(i)
                
            if l.count(i)==0 and l1.count(i)==1:
                l3.append(i)
               
        return (l3)