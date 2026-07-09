class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                l=i
                break
        for i in range(len(nums)-1,0,-1):
            if nums[i]<nums[i-1]:
                r=i
                break
        min1=min(nums[l:r+1])
        max1=max(nums[l:r+1])
        c=l
        while l>=0 :
            if nums[l]>min1:
                c=l
            l-=1
        c1=r
        while r<len(nums) :
            if nums[r]<max1:
                c1=r
            r+=1
        if (c==0 and c1==0):
            return 0        
        return abs(c-c1)+1