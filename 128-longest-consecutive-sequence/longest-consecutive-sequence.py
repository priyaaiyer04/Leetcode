class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1=0
        num_set = set(nums)
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        for i in num_set:
            if i-1 not in num_set:
                c=0
                x=i
                while x+1 in num_set:
                    c+=1
                    x+=1
                max1=max(max1,c)
        return (max1+1)