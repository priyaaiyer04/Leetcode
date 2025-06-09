class Solution(object):
    def merge(self,arr,s,m,e):
        l=[]
        i=s
        j=m+1
        while i<=m and j<=e:
            if arr[i]<=arr[j]:
                l.append(arr[i])
                i+=1
            else:
                l.append(arr[j])
                j+=1
        while i<=m:
            l.append(arr[i])
            i+=1
        while j<=m:
            l.append(arr[j])
            j+=1
        for k in range(len(l)):
            arr[k+s]=l[k]
    def mergesort(self,nums,s,e):
        if e-s+1<=1:
            return nums
        m=(s+e)//2
        self.mergesort(nums,s,m)
        self.mergesort(nums,m+1,e)
        self.merge(nums,s,m,e)
        return nums
    
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=self.mergesort(nums,0,len(nums)-1)
        return nums
