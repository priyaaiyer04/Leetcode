class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        x=nums.count(2)
        y=nums.count(0)
        for i in range(x):
            nums.remove(2)
        
        for i in range(x):
        
            nums.append(2)
        for i in range(y):
            
            nums.remove(0)
        for i in range(y):
            
            nums.insert(0,0) 