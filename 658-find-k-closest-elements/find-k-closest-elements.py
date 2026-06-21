class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        
        ans1 = float('inf')
        ans = float('inf')

        for i in arr:
            if abs(i - x) < ans:
                ans1 = i
                ans = abs(i - x)
        l = []
        idx = arr.index(ans1)
        if idx==0:
            for i in arr[idx:idx+k]:
                l.append(i)
            return l
        elif idx==len(arr)-1:
            for i in arr[idx-k+1:idx+1]:
                l.append(i)
            return l
        l.append(arr[idx])
        if abs(arr[idx-1]-x)<=abs(arr[idx+1]-x) and len(l)<k:
                l.append(arr[idx-1])
                c=idx-2
                d=idx+1
        elif abs(arr[idx-1]-x)>abs(arr[idx+1]-x) and len(l)<k:
                l.append(arr[idx+1])
                c=idx-1
                d=idx+2
        else:
            return l
       
        while c>=0 and d<len(arr):
            if len(l)==k:
                break
            elif abs(arr[c]-x)<=abs(arr[d]-x):
                l.append(arr[c])
                c-=1
            else :
                l.append(arr[d])
                d+=1
        
        if len(l)<k and c>=0:
            while len(l)<k and c>=0:
                l.append(arr[c])
                
                c-=1
        if len(l)<k and d<len(arr):
            while len(l)<k and d<len(arr):
                l.append(arr[d])
                d+=1
        l.sort()
        return l