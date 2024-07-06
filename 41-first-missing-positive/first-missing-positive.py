class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        nums.sort()
        for x in nums:
            if i==x:
                i+=1
        return i