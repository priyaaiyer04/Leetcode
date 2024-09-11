class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[]
        l1=[]
        for i in numbers:
            if l1.count(i)==0:
                l1.append(i)
        for i in l1:
            for j in l1:
                if i==j and numbers.count(i)>1 or i!=j:
                    if i+j==target:
                        if l.count(numbers.index(i)+1)==0 and l.count(numbers.index(j)+1)==0:
                            l.append(numbers.index(i)+1)
                            if i==j:
                                l.append(numbers.index(i)+2)
                            else:
                                l.append(numbers.index(j)+1)
                            break
                       
        
        return l