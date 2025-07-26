class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def h(curr,i):
            if i==len(nums):
                res.append(curr[:])
                return
           
            curr.append(nums[i])
            h(curr,i+1)
            curr.pop()
            h(curr,i+1)
        h([],0)
        return res
