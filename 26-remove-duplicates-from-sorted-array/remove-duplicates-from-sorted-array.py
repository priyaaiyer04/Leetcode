class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=len(nums)-1
        k=0
        while x>0:
            if nums[x]==nums[x-1]:
                nums.remove(nums[x-1])
                k+=1
            x-=1
        print(nums)
        return len(nums)                