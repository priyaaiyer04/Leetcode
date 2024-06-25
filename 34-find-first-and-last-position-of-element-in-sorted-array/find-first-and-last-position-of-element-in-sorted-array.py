class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[]
        l1=[]
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
        if len(l)==0:
            l1.append(-1)
            l1.append(-1)
            return l1
        l1.append(min(l))
        l1.append(max(l))
        return l1