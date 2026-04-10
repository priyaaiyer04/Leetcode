class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums.count(0)==len(nums):
            return "0"
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if int(str(nums[i])+str(nums[j]))<int(str(nums[j])+str(nums[i])):
                    t=nums[i]
                    nums[i]=nums[j]
                    nums[j]=t
        nums=[str(i) for i in nums]
        return "".join(nums)