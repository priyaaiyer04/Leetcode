class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        l=[]
        for i in range(1,n+1):
            l.append(i)
        comb = combinations(l, k)
        c=0
        l1=[]
        for i in list(comb):
            l1.append(i)
        return l1