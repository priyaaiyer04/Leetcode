class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        if k==len(nums):
            return nums
        l=[]
        l1=[]
        d={}
        for i in nums:
            if l.count(i)==0:
                d[i]=nums.count(i)
                l.append(i)
        d1=(sorted(d, key=d.get,reverse=True))
        return d1[0:k]