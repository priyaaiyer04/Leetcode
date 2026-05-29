class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[i for i in nums]
        l.sort()
        ans=[]
        for i in range(len(nums)):
            if nums[i]!=l[i]:
                ans.append(i)
        if len(ans)<=0:
            return 0
        return (max(ans)-min(ans)+1)