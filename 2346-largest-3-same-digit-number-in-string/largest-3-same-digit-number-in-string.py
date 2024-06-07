class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        l=[]
        l2=[]
        for i in range(len(num)-2):
            x=num[i:i+3]
            l.append(x)
        for i in l:
            if int(i)%111==0:
                l2.append(i)
        if len(l2)==0:
            return ""
        else:
            return max(l2)