class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
#can start from 0th or 1st step
        dp={}
        def cs(l,n):
            if n<=1:
                return 0
            if n in dp.keys():
                return dp[n]
            dp[n]=min(l[n-1]+cs(l,n-1),l[n-2]+cs(l,n-2) )
            return dp[n]

        return cs(cost,len(cost))
        print(dp)
                