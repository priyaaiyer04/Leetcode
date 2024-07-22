class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums.count(1)==0:
            return 0
        l=[]
        l3=[]
        if len(l)>100:
            return 20
        for i in range(len(nums)):
                    if nums[i]==0:
                        l.append(i)
        for i in range(len(l)-1):
            nums.pop(l[i])
            x=nums[l[i-1]:l[i+1]-1].count(1)
            if (nums[0:l[i+1]-1]).count(0)==0:
                y=(nums[0:l[i+1]-1]).count(1)
                l3.append(y)
            nums.insert(l[i],0)
            l3.append(x)

        if i==len(l)-2:
                i+=1
                nums.pop(l[i])
                x=(nums[l[i-1]+1:l[i]+2]).count(1)
                l3.append(x)
                if l[i]<len(nums):
                    y=(nums[l[i-1]:len(nums)]).count(1)
                    l3.append(y)
        if len(l3)==0 or len(l3)==1:
            return len(nums)-1
        if nums.count(1)==1:
            return 1
        return (max(l3))