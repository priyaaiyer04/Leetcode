class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=len(nums1)
        j=i-n
        for x in range(j,i):
            nums1[x]=nums2[0]
            nums2.remove(nums2[0])
        nums1.sort()