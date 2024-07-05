class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l1=[]
        x=len(matrix)
        l2=len(matrix[0])
        i=0
        j=0
        while i<len(matrix):
            j=0
            while j<l2:
                l1.append(matrix[j][i])
                j+=1
            
            i+=1    
        i=0
        l3=[]
        for i in range(len(matrix)):
            j=0
            while j<l2:
                l3.append(l1[0])
                l1.pop(0)
                j+=1
                
            matrix[i]=l3[::-1]
            l3=[]