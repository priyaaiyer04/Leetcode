class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in digits:
            l.append(str(i))
        s=""
        s=s.join(l)
        a=int(s)+1
        a=str(a)
        
        digits = [int(z) for z in a]
        return digits
        