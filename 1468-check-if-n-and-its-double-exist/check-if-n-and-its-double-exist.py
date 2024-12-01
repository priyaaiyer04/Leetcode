class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in arr:
            for j in arr:
                if i!=j and (2*i==j or 2*j==i):
                    print(i,j)
                    return True
                if i==j and arr.count(i)>1 and 2*i==j:
                    
                    return True
        return False