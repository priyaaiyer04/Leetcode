class Solution(object):
    def specialPerm(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()  # Sort to help with early pruning
        memo = {}

        def helper(used_tuple, last):
            key = (used_tuple, last)
            if key in memo:
                return memo[key]
            if sum(used_tuple) == n:
                return 1

            total = 0
            for i in range(n):
                if not used_tuple[i]:
                    if last == -1 or nums[i] % nums[last] == 0 or nums[last] % nums[i] == 0:
                        new_used = list(used_tuple)
                        new_used[i] = 1
                        total += helper(tuple(new_used), i)
                        total %= MOD

            memo[key] = total
            return total

        return helper(tuple([0]*n), -1)