class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=1
        l=[]
        r=[]
        for i in range(len(nums)):
            if i==0:
                l.append(1)
            else:
                p*=nums[i-1]
                l.append(p)
            
        p=1
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                r.append(1)
            else:
                p*=nums[i+1]
                r.append(p)
        r=r[::-1]    
        l1=[]
        for i in range(len(l)):
            l1.append(l[i]*r[i])
        return l1