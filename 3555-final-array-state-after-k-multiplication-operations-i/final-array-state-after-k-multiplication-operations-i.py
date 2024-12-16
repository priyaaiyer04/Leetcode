class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        
        for i in range(k):
            x=min(nums)
            y=x*multiplier
            z=nums.index(x)
            nums[z]=y
            print(nums)
        return nums
