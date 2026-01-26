class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        nums.sort()
        i=0
        k=len(nums)-1
        j=len(nums)-2
        while i<j<k:
            while i<j:
                target=-nums[k]
                if nums[i]+nums[j]==target:
                    l=[nums[i],nums[j],nums[k]]
                    l.sort()
                    if l not in ans:
                        ans.append(l)
                    i+=1
                    j-=1
                elif nums[i]+nums[j]<target:  
                    i+=1
                elif nums[i]+nums[j]>target:  
                    j-=1
            i=0
            k-=1
            j=k-1
        return ans
              