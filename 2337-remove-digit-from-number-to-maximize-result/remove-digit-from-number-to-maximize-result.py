class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        l=[i for i in number]
        l1=[]
        l2=[]
        l1 = [i for i, ele in enumerate(l) if ele == digit]

        for i in l1:
            l[i]=""
            x=""
            l2.append(x.join(l))
            l[i]=digit
        return (max(l2))