class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        d={}
        def dp(i,j):
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            if (i,j)  in d:
                return d[(i,j)]
            if word1[i]==word2[j]:
                d[(i,j)]=dp(i+1,j+1)
               
            else:
                d[(i,j)]=1+min(dp(i+1,j+1),dp(i,j+1),dp(i+1,j))
            return d[(i,j)]
        return dp(0,0)
            