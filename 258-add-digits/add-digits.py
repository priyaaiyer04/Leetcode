class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum=0
        a=str(num)
        while int(a)>=10:
            for i in a:
                sum+=int(i)
            a=str(sum)
            sum=0
            if int(a)<10:
                
                break
        return int(a)        