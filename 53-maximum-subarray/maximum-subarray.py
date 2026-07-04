class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b=-float('inf')
        ans=-float('inf')
        for i in range(len(nums)):
            v1=b+nums[i]
            v2=nums[i]
            b=max(v1,v2)
            ans=max(ans,b)
        return ans