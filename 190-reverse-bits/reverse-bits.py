class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
         return sum((n>>i&1)<<(31-i) for i in range(32))