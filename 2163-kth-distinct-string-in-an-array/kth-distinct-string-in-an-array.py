class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        l=[]
        x=0
        for i in arr:
            if arr.count(i)==1:
                x+=1
            if x==k:
                return i
        return ""