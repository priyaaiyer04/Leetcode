class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        c=0
        for i in range(len(nums)):
            if nums[i]==0:
                l+=1
                c+=l
            else:
                l=0
        return c