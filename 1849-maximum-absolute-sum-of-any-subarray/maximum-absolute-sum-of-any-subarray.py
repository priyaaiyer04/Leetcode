class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ans=-float('inf')
        best=-float('inf')
        for i in range(len(nums)):
            c1=best+nums[i]
            c2=nums[i]
            best=max(c1,c2)
            ans=max(ans,best)

        ans1=float('inf')
        best1=float('inf')
        for i in range(len(nums)):
            c1=best1+nums[i]
            c2=nums[i]
            best1=min(c1,c2)
            
            ans1=min(ans1,best1)
            
        return max(abs(ans),abs(ans1))