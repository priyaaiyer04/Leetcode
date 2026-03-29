from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue=deque()
        queue.append((beginWord,1))
        visited=set()
        wordset=set(wordList)
        if endWord not in wordList:
            return 0
        while queue:
            curr=queue.popleft()
            if curr[0]==endWord:
                return (curr[1])
                break
            if curr[0] not in visited:
                
                visited.add(curr[0])
                for i in range(len(curr[0])):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        c=curr[0][:i]+j+curr[0][i+1:]
                    
                        if c in wordset and c!=curr[0]:
                            
                            queue.append((c,curr[1]+1))
        return 0