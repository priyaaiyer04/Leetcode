class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        u=len(nums)-1
        while l<=u:
            m=(l+u)//2
            if nums[m]==target:
                return m
            """check if left portion sorted"""
            if nums[l]<=nums[m]:
                if nums[l]<=target<=nums[m]:
                    u=m-1
                else:
                    l=m+1
            """check if right portion sorted"""
            if nums[m]<=nums[u]:
                if nums[m]<=target<=nums[u]:
                    l=m+1
                else:
                    u=m-1

        return -1