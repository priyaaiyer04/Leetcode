class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort()
        for i in nums:
            if nums.count(i)==3:
                return "equilateral"
            if nums.count(i)==2 and nums[0]+nums[1]>nums[2]:
                return "isosceles"
        
        if nums[0]+nums[1]>nums[2]:
            return "scalene"
        return "none"