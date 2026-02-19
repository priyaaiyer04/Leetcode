class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l=[]
        ans=[]
        d={}
        for i in nums2:
            while len(l)>0 and i>l[-1]:
                d[l[-1]]=i
                l.pop()
            l.append(i)
        for i in nums1:
            if i in d.keys():
                ans.append(d[i])
            else:
                ans.append(-1)
        return ans
