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
        l1=[abs(i) for i in l1]
        l1=l1[::-1]
        l=0
        r=0
        ans=[]
        while l<len(l1) and r<len(l2):
            if l2[r]<l1[l]:
                ans.append(l2[r])
                r+=1
            elif l2[r]>l1[l]:
                ans.append(l1[l])
                l+=1
            else:
                ans.append(l1[l])
                ans.append(l2[r])
                l+=1
                r+=1
        while l<len(l1):
            ans.append(l1[l])
            l+=1
        while r<len(l2):
            ans.append(l2[r])
            r+=1
        ans=[i**2 for i in ans]
        return ans