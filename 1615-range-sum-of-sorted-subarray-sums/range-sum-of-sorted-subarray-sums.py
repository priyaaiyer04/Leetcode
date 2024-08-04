class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        l=[]
        l2=[]
        for i in range(len(nums)):
            l1=[nums[i]]
            for j in range(i+1,len(nums)):
                l1.append(l1[len(l1)-1]+nums[j])
            l.append(l1)
        for i in l:
            for j in i:
                l2.append(j)
        l2.sort()
        l2=l2[left-1:right]
        if right==len(l2):
            print(sum(l2))
        return sum(l2)%((10**9)+7)