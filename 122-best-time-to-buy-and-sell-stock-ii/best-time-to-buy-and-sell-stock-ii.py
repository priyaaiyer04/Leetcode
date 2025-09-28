class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                p+=prices[i+1]-prices[i]
        return p