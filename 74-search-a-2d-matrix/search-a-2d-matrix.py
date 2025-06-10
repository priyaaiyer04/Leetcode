class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l=[]
        for i in matrix:
            for j in i:
                l.append(j)
        if target in l:
            return True
        return False