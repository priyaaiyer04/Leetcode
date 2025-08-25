class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        d={}
        def fun(i):
            if i>=len(nums):
                return 0
            if i in d.keys():
                return d[i]
            else:
                d[i]=max(nums[i]+fun(i+2),fun(i+1))
                return d[i]
        for i in range(len(nums)):
            l.append(fun(i))
        return (max(l))