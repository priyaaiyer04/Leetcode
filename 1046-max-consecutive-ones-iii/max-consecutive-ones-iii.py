class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
        l=0
        r=0
        ans=0
        c=0
        while l<=r<len(nums):
            if r-l-c>=k and nums[r]==0:
               
                ans=max(ans,r-l)
                if nums[l]==1:
                    c-=1
                l=l+1
                r-=1
                if r<l:
                    r=l-1
            elif nums[r]==1:
                c+=1
            r+=1
        ans=max(ans,len(nums)-l)
        return ans 