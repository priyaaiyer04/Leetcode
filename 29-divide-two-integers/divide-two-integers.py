class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        if dividend==0:
            return 0
        d1=abs(dividend)
        d2=abs(divisor)
        if dividend==divisor:
            return 1
        if dividend==-divisor:
            return -1
        if divisor==1:
            return dividend
        d1=abs(dividend)
        d2=abs(divisor)
        ans=0
        while d1>=abs(divisor):
            i=0
            
            while d1>=d2*2**(i+1):
                i+=1
            ans+=(2**i)
            d1=d1-d2*2**(i)
        
        if divisor>0 and dividend>0 or divisor<0 and dividend<0:
            ans=ans
        else:
            sign=False
            ans=-ans
        if ans >=2147483647:
            return 2147483647
        if ans <=-2147483648:
            return -2147483647
        return ans