class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in nums:
            if nums.count(i)>len(nums)//3 and l.count(i)==0:
                l.append(i)
        return (l)