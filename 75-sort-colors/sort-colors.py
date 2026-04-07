class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        c=0
        while i<len(nums):
            if nums[i]==0:
                c+=1
            i+=1
        for i in range(c):
            nums.remove(0)
        for i in range(c):
            nums.insert(0,0)
        i=0
        c=0
        while i<len(nums): 
            if nums[i]==2:
                c+=1
            i+=1
        for i in range(c):
            nums.remove(2)
        for i in range(c):
            nums.append(2)