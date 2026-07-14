class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        d={0:1}
        ans=0
        for i in range(len(nums)):
            c+=nums[i]
            q=c-k
            if q in d:
                ans+=d[q]
            if c in d:
                d[c]+=1
            else:
                d[c]=1
        return ans