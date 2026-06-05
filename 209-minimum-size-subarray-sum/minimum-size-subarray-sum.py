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
        c=0

        while l<=r<len(nums):
            if c>=target:
                ans=min(ans,r-l)
                c-=nums[l]
                l+=1
            else:
                c+=nums[r]
                r+=1
        if c>=target:
            ans=min(ans,r-l)
        if r==len(nums):
            print("hi")
            while l<len(nums):
                c-=nums[l]
                l+=1
                print(c,l)
                if c>=target:
                    
                    ans=min(ans,len(nums)-l)
        if ans==float('inf'):
            return 0
        return ans