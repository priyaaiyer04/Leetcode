class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[i]>=0:
                break
        l1=nums[:i]
        l2=nums[i:]
        l1=[i**2 for i in l1]
        l2=[i**2 for i in l2]
        l1=l1[::-1]
        t=0
        t1=0
        ans=[]
        while t<len(l1) and t1<len(l2):
            if l1[t]<l2[t1]:
                ans.append(l1[t])
                t+=1
            else:
                ans.append(l2[t1])
                t1+=1
        while t<len(l1):
            ans.append(l1[t])
            t+=1
        while t1<len(l2):
            ans.append(l2[t1])
            t1+=1
        return ans