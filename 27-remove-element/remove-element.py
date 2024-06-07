class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=0
        for i in nums:
            if i!=val:
                
                k+=1
        c=len(nums)-k
        while c!=0:
            nums.remove(val)
            c-=1
        return k