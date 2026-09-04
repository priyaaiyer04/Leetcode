class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        ans=0
        d={}
        def dp(n,i):
            if n<0 or i>=len(coins):
                return 0
            if n==0:
                return 1
            if (n,i) in d:
                return d[(n,i)]
           
            d[(n,i)]=dp(n,i+1)+dp(n-coins[i],i)
            return d[(n,i)]
        return dp(amount,0)