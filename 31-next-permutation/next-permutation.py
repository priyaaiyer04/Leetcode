class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=[i for i in nums]
        l.sort(reverse=True)
        if l==nums:
            nums.sort()
        else:
            org=[i for i in nums]
            for i in range(len(nums)-1,0,-1):
                if nums[i]>nums[i-1]:
                    index=-1
                    min1=float('inf')
                    for x in range(i,len(nums)):
                            if  nums[x] > nums[i-1] and nums[x] -nums[i-1]<min1:
                                min1=nums[x] -nums[i-1]
                                index=x
                                
                    nums[i-1], nums[index] = nums[index], nums[i-1]
                    l1=nums[0:i]
                    l2=nums[i:]
                    l2.sort()
                    nums[:]=l1+l2
                    break