class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        d={0:0}
        dp={}
        sum1=0
        for i in nums:
            if i not in d:
                d[i]=i *nums.count(i)
        for i in range(max(nums)+1):
            if i in d.keys():
                z=d[i]
            else:
                z=0
            if i-2 in dp.keys():
                x=dp[i-2]
            else:
                x=0
            if i-1 in dp.keys():
                y=dp[i-1]
            else:
                y=0    
            dp[i]=max(x+z,y)
        return (dp[max(nums)])
            