class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        prefix_sum={0:1}
        ps=0
        for i in nums:
            ps+=i
            if ps-k in prefix_sum:
                c+=prefix_sum[ps-k]
            prefix_sum[ps] = prefix_sum.get(ps, 0) + 1
        return c