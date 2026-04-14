class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        l=0
        r=0
        p=1
        g=1
        for i in nums:
            g*=i
        if g<k:
            return len(nums)*(len(nums)+1)//2
        while l<len(nums):
            
            if (l!=len(nums)-1 and r>=len(nums)) or p>=k:
                l+=1
                r=l
                p=1
            elif l==len(nums)-1:
                p=nums[l]
                break
            if r<len(nums):
                p*=nums[r]
                if p<k:
                    c+=1
               
            r+=1
        return c