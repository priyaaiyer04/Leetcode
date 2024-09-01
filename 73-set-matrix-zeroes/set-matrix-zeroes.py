class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        x=0
        c=0
        y=0
        l1=[]
        l2=[]
        for i in matrix:
            y=0
            for j in i:
                y+=1
                if j==0:
                    
                    if l1.count(y-1)==0:
                        l1.append(y-1)
                    c=matrix.index(i)
                    
                    if l2.count(c)==0:
                        l2.append(c)
        y=len(matrix[0]) 
        l=[]

        for i in range(y):
                    l.append(0)
        for i in l2:
                matrix.pop(i)
                matrix.insert(i,l)
        print(l1)      
        for i in l1:
            for j in matrix:
                    j.pop(i)
                    j.insert(i,0)