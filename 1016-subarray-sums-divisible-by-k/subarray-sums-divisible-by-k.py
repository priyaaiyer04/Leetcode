class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum1=0
        ans=0
        d={}
        d[ans]=1
        for i in range(len(nums)):
            sum1+=nums[i]
            rem=sum1%k
            if rem<0:
                rem+=k
            if rem in d:
                ans+=d[rem]
                d[rem]+=1
            else:
                d[rem]=1
        return ans
