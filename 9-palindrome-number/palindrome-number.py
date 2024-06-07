class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        if x==x[::-1] and x>=0:
            return True
        else:
            return False