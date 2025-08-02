class Solution(object):
    def specialPerm(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        memo={}
        nums.sort()
        def helper(used, path):
            key=(tuple(used),path[-1] if path else None)
            if key in memo:
                return memo[key]
            if len(path)==n:
                return 1
            count=0
            for i in range(n):
                if not used[i]:
                    if len(path)==0 or nums[i]%path[-1]==0 or path[-1]%nums[i]==0:
                        path.append(nums[i])
                        used[i]=True
                        count+=helper(used,path)
                        path.pop()
                        used[i]=False
            memo[key]=count
            return count%(10**9+7)
        return helper([False]*n,[])    
