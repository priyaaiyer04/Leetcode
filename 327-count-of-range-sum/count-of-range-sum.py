class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        psum=[0]
        for i in nums:
            psum.append(psum[-1]+i)
        psum=psum[::-1]
       
        ans=0
        sl=SortedList()
        for i in psum:
            l=lower+i
            u=upper+i
            left=sl.bisect_left(l)
            x=sl.bisect_right(u)
            ans+=x-left
            sl.add(i)
        return ans