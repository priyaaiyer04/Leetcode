class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        d={}
        def coins1(n):
            if n<0:
                return float('inf')
            if n==0:
                return 0
            if n in d:
                return d[n]
            d[n]=float('inf')
            for i in coins:
                d[n]=min(d[n],1+coins1(n-i))
            return d[n]
        ans=coins1(amount)
        if ans==float('inf'):
            return -1
        return ans