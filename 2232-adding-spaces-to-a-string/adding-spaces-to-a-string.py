class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        l=[]
        l.append(s[0:spaces[0]])
        for i in range(len(spaces)-1):
            l.append(s[spaces[i]:spaces[i+1]])
        l.append(s[spaces[len(spaces)-1]:len(s)])
        s=" ".join(l)
        return s
