class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=len(nums)-1
        
        while x>0:
            if nums[x]==nums[x-1]:
                del nums[x-1]
                
            x-=1
        print(nums)
        return len(nums)                