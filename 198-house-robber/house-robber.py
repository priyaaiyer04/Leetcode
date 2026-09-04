class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        def dp(n):
            if n>=len(nums):
                return 0
            if n in d:
                return d[n]
            d[n]=max(dp(n+1),dp(n+2)+nums[n])
            return d[n]
        return dp(0)