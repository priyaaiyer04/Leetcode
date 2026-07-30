class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if x<=arr[0]:
            return arr[0:k]
        if x>=arr[len(arr)-1]:
            return arr[len(arr)-1-k+1:len(arr)]
        ans=[]
        l=[]
        for i in arr:
            l.append(abs(i-x))
        idx=l.index(min(l))
        
        ans.append(arr[idx])
        l=idx-1
        r=idx+1
        while len(ans)<k and l>=0 and r<len(arr):
                if  abs(x-arr[l])<=abs(x-arr[r]):
                    ans.append(arr[l])
                    l-=1
                elif abs(x-arr[r])<=abs(x-arr[l]):
                    ans.append(arr[r])
                    r+=1
        if len(ans)<k and l>=0:
                while len(ans)<k:
                    ans.append(arr[l])
                    l-=1
        if len(ans)<k and r<len(arr):
                while len(ans)<k:
                    ans.append(arr[r])
                    r+=1
        ans.sort()
        return ans