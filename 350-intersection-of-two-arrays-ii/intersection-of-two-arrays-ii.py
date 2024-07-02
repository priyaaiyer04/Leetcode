class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1=[]
        if len(nums1)<=len(nums2):
            for i in nums1:
                if nums2.count(i)>0 and l1.count(i)<nums2.count(i):
                    l1.append(i)
        if len(nums2)<len(nums1):
            for i in nums2:
                if nums1.count(i)>0  and l1.count(i)<nums1.count(i):
                    l1.append(i)
        return l1