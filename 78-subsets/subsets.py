class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def helper(curr,i):
            if i==len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            helper(curr,i+1)
            curr.pop()
            helper(curr,i+1)
        helper([],0)
        return res
