class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        c=0
        for i in words:
            s=""
            if s.count(i)==0:
                s+=i
            for j in s:
                if allowed.count(j)==0:
                    c+=1
                    break
        return (len(words)-c)