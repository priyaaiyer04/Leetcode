class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1 or len(nums)==0:
            return nums
        x=min(nums)
        y=max(nums)
        count=[0]*(y-x+1)
        for i in nums:
            count[i-x]+=1
        k=0
        for i in range(len(count)):
            for j in range(count[i]):
                nums[k]=i+x
                k+=1
        return nums
