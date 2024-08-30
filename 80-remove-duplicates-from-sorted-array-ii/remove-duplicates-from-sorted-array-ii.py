class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i)>2:
                x=nums.count(i)
                c=0
                y=x-2
                while c<y:
                    nums.remove(i)
                    c+=1
        return (len(nums))
        