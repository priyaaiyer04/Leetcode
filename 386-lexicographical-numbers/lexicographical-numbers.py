class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[]
        l1=[]
        for i in range(1,n+1):
            l.append(str(i))
        l.sort()
        for i in l:
            l1.append(int(i))
        return l1