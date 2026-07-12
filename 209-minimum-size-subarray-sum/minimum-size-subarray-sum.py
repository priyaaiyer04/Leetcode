class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
                
        l=0
        r=0
        ans=float('inf')
        p=0
        while l<=r<len(nums):
            p+=nums[r]
            if p==target:
                
                ans=min(ans,r-l+1)
                p-=nums[l]
                l+=1
            elif p>target:
                ans=min(ans,r-l+1)
                while p>target:
                    p-=nums[l]
                    l+=1
                    if p>=target:
                        ans=min(ans,r-l+1)
            r+=1
        if p>=target:
            
            ans=min(ans,len(nums)-l)
        if ans==float('inf'):
            return 0
        return ans