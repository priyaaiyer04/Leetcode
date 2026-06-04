class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums)<4:
            return []
        if len(nums)==4:
            if sum(nums)==target:
                return [nums]
            
        nums.sort()
        ans=[]
        for i in range(len(nums)-3):
            r=i+1
            
            while r<len(nums)-2:
                t=target-(nums[i]+nums[r])
                l1=r+1
                r1=len(nums)-1
                while l1<r1:
                    if nums[l1]+nums[r1]>t:
                        r1-=1
                    elif nums[l1]+nums[r1]<t:
                        l1+=1
                    else:
                        if [nums[i],nums[r],nums[l1],nums[r1]] not in ans:
                            ans.append([nums[i],nums[r],nums[l1],nums[r1]])
                        l1+=1
                        r1-=1
                r+=1
        return ans