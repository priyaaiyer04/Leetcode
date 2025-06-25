class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def helper(l,ind):
            if ind==len(nums):
                res.append(l[:])
                return
            l.append(nums[ind])
            helper(l,ind+1)
            l.pop()
            helper(l,ind+1)
        helper([],0)
        l=[]
        for i in res:
            i.sort()
            if l.count(i)==0:
                i.sort()
                l.append(i)
        return l