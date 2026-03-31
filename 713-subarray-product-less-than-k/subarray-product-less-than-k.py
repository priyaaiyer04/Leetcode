class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=0
        if k<=1:
            return 0
        c=1
        count=0
        for r in range(len(nums)):
            c=c*nums[r]
            while c>=k and l<len(nums):
                c=c//nums[l]
                l+=1
            
            
            count+=r-l+1
        if count<=0:
            return 0
        return count