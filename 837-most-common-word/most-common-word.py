class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        l=[]
        s1=""
        paragraph=paragraph.lower()
        for i in paragraph:
            if ord(i) in range(ord('a'),ord('z')+1):
                s1+=i
            else:
                l.append(s1)
                s1=""
        l.append(s1)
        for i in l:
            if i=='':
                l.remove('')
        x=0
        c=""
        for i in l:
            if len(banned)==0:
                if l.count(i)>x:
                    x=l.count(i)
                    c=i
            if banned.count(i)==0:
                if l.count(i)>x:
                    x=l.count(i)
                    c=i
        return c                