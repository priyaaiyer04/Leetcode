class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l2={}
        for i in nums:
            if l2.get(i)==1:
                return True
            else:
                l2[i]=1
        return False
