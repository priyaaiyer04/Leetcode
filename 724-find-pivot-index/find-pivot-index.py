class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        suf=[0]*len(nums)
        pref=[0]*len(nums)
        for i in range(1,len(nums)):
            pref[i]=pref[i-1]+nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suf[i]=suf[i+1]+nums[i+1]
        for i in range(len(nums)):
            if suf[i]==pref[i]:
                return i
                break
        return -1