class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        p=1
        for i in nums:
            p*=i
        if p<k:
            return (len(nums)+1)*(len(nums))//2
        l=0
        ans=0
        i=0
        while i<len(nums):
            r=i+1
            p=nums[i]
            if p<k:
                ans+=1
        
            while r< len(nums) :
                if p>=k:
                    break
                p*=nums[r]
                r+=1
                if p>=k:
                    r-=1
                    break
            ans+=r-i-1
            i+=1 
        return ans