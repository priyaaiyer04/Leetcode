class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        ans=float('inf')
        best=float('inf')
        for j in range(len(nums)):
            
            c1=nums[j]
            c2=best+nums[j]
            best=min(c1,c2)
            ans=min(ans,best)


        ans1=-float('inf')
        best=-float('inf')
        for j in range(len(nums)):
            
            c1=nums[j]
            c2=best+nums[j]
            best=max(c1,c2)
            ans1=max(ans1,best)
        print(ans,ans1)
        if sum(nums)==ans:
            return max(sum(nums), ans1)
        return  max(sum(nums)-ans, ans1)