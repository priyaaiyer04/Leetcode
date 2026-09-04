class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        def solve(nums):
            d={}
            def dp(n):
                if n>=len(nums):
                    return 0
                if n in d:
                    return d[n]
                d[n]=max(dp(n+1),dp(n+2)+nums[n])
                return d[n]
            return dp(0)
        return max(solve(nums[1:]),solve(nums[:len(nums)-1]))