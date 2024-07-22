class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l=[]
        for i in nums1:
            l.append(i)
        for i in nums2:
            l.append(i)
        l.sort()
        x=len(l)
        if x%2!=0:
            return (l[x//2])
        else:
            
            return ((float(l[x//2]+l[(x//2)-1])/2))