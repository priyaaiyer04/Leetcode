class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        l=sentence.split(" ")
        for i in l:
            if searchWord==i[0:len(searchWord)]:
                return l.index(i)+1
        return -1