class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        def dp(i):
            if i>=len(nums):
                return 0
            if i in d:
                return d[i]
            d[i]=max(nums[i]+dp(i+2),dp(i+1))
            
            return d[i]
        return dp(0)