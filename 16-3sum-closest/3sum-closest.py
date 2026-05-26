class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        ans=float('inf')

        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[left]+nums[right]+nums[i]<target:
                    if abs(target-ans)>abs(target-(nums[left]+nums[right]+nums[i])):
                        ans=nums[left]+nums[right]+nums[i]
                    
                    
                    x=left+1
                    while x<len(nums) and nums[left]==nums[x]:
                        x+=1
                    left=x
                elif nums[left]+nums[right]+nums[i]>target:
                    
                    if abs(target-ans)>abs(target-(nums[left]+nums[right]+nums[i])):
                        ans=nums[left]+nums[right]+nums[i]
                
                    x=right-1
                    while x>0 and nums[right]==nums[x]:
                        x-=1
                    right=x
                elif nums[left]+nums[right]+nums[i]==target:
                    
                    ans=target
                    x=left+1
                    while x<len(nums) and nums[left]==nums[x]:
                        x+=1
                    left=x
                    x=right-1
                    while x>0 and nums[right]==nums[x]:
                        x-=1
                    right=x
        return ans