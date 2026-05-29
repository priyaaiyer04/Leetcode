class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        l=0
        r=len(nums)-1
        while  l<len(nums)-1 and nums[l]<=nums[l+1]:
                l+=1
        while r>0 and nums[r]>=nums[r-1] :
                r-=1
        if r==0 or l==len(nums)-1:
            return 0
        x=min(nums[l:r+1])
        y=max(nums[l:r+1])
        l1=l
        r1=r
        while l1>=0 and r1<len(nums):
            if nums[l1]>x:
                l=l1
            if nums[r1]<y:
                r=r1
            l1-=1
            r1+=1
        while l1>=0 :
            if nums[l1]>x:
                l=l1
            l1-=1
        while r1<len(nums):
            if nums[r1]<y:
                r=r1
            r1+=1
        return r-l+1