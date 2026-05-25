class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        ans=[]
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
           
            target=-1*nums[i]
            left=i+1
            right=len(nums)-1
            while left<right:
                if left<right and nums[left]+nums[right]<target:
                    x=left+1
                    while  x<len(nums) and nums[x]==nums[left]:
                        x+=1
                    left=x
                elif left<right and nums[left]+nums[right]>target:
                    x=right-1
                    while x>=0 and nums[x]==nums[right]:
                        x-=1
                    right=x    
                elif left<right and nums[left]+nums[right]==target:
                    l1=[]
                    if left!=right and right!=i and left!=i:
                        l1.append(nums[left])
                        l1.append(nums[right])
                        l1.append(nums[i])
                        ans.append(l1)
                    x=right-1
                    while x>=0 and nums[x]==nums[right]:
                        x-=1
                    right=x
                    x=left+1
                    while x<len(nums) and nums[x]==nums[left]:
                        x+=1
                    left=x
        return ans