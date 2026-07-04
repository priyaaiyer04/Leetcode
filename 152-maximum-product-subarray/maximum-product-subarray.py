class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxe=None
        mine=None
        ans=None
        for i in range(len(nums)):
            if maxe==None:
                maxe=nums[i]
            else:
                maxe*=nums[i]
            if mine==None:
                mine=nums[i]
            else:
                mine*=nums[i]
            c=nums[i]
            l=[maxe,mine,c]
            mine=min(l)
            maxe=max(l)
            ans=max(ans,maxe,mine)
        return ans