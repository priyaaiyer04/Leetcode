class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        l=[]
        if nums.count(nums[0])==len(nums):
            return nums[0]
        for i in nums:
            if i not in list(d.keys()):
                d[i]=nums.count(i)
        for i in d.keys():
            l.append(d[i])
        x=max(l)
        i=l.index(x)
        l1=list(d.keys())
        return l1[i]