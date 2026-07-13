class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]

        l=0
        r=l+1
        while l<=r<len(nums):
            c=nums[l]+nums[r]
            print(c,nums[l],nums[r])
            c=target-c
            t=r+1
            t1=len(nums)-1
        
            while t<t1:
                if nums[t]+nums[t1]<c:
                    t+=1
                elif nums[t]+nums[t1]>c:
                    t1-=1
                else:
                    x=[nums[l],nums[r],nums[t],nums[t1]]
                    if x not in ans:
                        ans.append(x)
                    t+=1
                    t1-=1
            r+=1
            if r==len(nums):
                l+=1
                r=l+1
        return ans