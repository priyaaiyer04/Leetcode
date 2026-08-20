class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        ans=float('inf')
        import heapq
        dq=[]
        c=0
        for i in range(len(nums)):
            c+=nums[i]
            if c>=k:
                ans=min(ans,i+1)
            while dq and c-dq[0][0]>=k:
                ans=min(ans,i-dq[0][1])
                heapq.heappop(dq)
            heapq.heappush(dq,(c,i))

        if ans==float('inf'):
            return -1
        return ans