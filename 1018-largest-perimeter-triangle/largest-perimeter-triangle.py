class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        x=0
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]>nums[i+2]:
                if nums[i]+nums[i+1]+nums[i+2] >x:
                    x=nums[i]+nums[i+1]+nums[i+2]
        return x