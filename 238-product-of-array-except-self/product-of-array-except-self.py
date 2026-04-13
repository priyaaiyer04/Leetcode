class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=1
        g=1
        for i in nums:
            if i!=0:
                g*=i
        for i in nums:
            p*=i
        l=[]
        for i in nums:
            if i!=0:
                l.append(p//i)
            else:
                if nums.count(0)>1:
                    l.append(0)
                else:
                    l.append(g)
        return l