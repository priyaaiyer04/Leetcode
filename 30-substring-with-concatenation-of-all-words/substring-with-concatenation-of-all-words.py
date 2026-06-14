class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        
        x=len(words[0])
        x=x*len(words)
        d={}
        ans=[]
        for i in range(len(s)-x+1):
            d[i]=s[i:i+x]
        words=sorted(words)

        for i in list(d.keys()):
            
            c=0
            l=[]
            m=0
            while m<x:
                l.append(d[i][m:m+len(words[0])])
                m+=len(words[0])
            l=sorted(l)
            if l==words:
                ans.append(i)
        return ans