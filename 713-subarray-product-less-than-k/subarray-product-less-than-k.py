class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
                
        l=0
        r=0
        ans=0
        p=1
        while l<=r<len(nums):
            if p*nums[r]>=k:
                ans+=r-l
               
                p=p//nums[l]
               
                if p<=0:
                    p=1
                l+=1
                if l>r:
                    r=l
            else:
                p*=nums[r]
                r+=1
        ans+=len(nums)-l
        while l<len(nums):
            p=p//nums[l]
            l+=1
            if p<k:
                ans+=len(nums)-l
        return ans