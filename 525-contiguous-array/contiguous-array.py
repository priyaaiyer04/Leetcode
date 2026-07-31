class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        i=0
        x=0
        y=0
        ans=0
        while i<len(nums):
            if nums[i]==0:
                x+=1
            elif nums[i]==1:
                y+=1
            if x-y in d:
                ans=max(ans,i-d[x-y]+1)
                print(i,d[x-y])
            if x-y==0:
                ans=max(ans,i+1)
            elif x-y not in d:
                d[x-y]=i+1
            i+=1
        return ans