class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def fn(arr):
        
            if len(arr)==1:
                return arr[0]
            else:
                l=[]
                for i in range(len(arr)-1):
                    a=arr[i]%10
                    b=arr[i+1]%10
                    l.append((a+b)%10)
                return fn(l)
        return fn(nums)