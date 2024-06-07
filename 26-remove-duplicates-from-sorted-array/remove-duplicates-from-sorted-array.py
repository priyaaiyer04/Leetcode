class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        l.append(nums[0])
        for i in nums:
            if l.count(i)==0:
                l.append(i)
        while nums:
            nums.pop()
        for i in l:
            nums.append(i)
        k=len(nums)
        return k
        
            