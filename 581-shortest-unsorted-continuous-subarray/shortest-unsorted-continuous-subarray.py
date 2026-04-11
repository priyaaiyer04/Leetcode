class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[i for i in nums]
        l.sort()
        l1=[]
        for i in range(len(l)):
            if l[i]!=nums[i]:
                l1.append(i)
       
        if len(l1)>0:
            return (l1[len(l1)-1]-l1[0]+1)
        return 0