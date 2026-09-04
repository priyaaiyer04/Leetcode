class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}
        if (sum(nums))%2!=0:
            return False
        def dp(i,sum1):
            if i>=len(nums) or sum1<0:
                return False
            if sum1==0:
                return True
            if (i,sum1) in d:
                return d[(i,sum1)]
            d[(i,sum1)]=dp(i+1,sum1) or dp(i+1,sum1-nums[i])
            return d[(i,sum1)]
        return dp(0,sum(nums)//2)