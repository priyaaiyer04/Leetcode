class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        def dp(n):
            if n==len(nums):
                return 0
            if n in d:
                return d[n]
            d[n]=1
            for i in range(n+1,len(nums)):
                if nums[i]>nums[n]:
                    d[n]=max(d[n],1+dp(i))
            return d[n]
      
        x=0
        for i in range(len(nums)):
            if dp(i)>x:
                x=dp(i)
        return x