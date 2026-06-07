class Solution(object):
    def minArraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx=max(nums)
        freq=[0]*(mx+1)
        for i in nums:
            freq[i]+=1
        ans=0
        for d in range(1,mx+1):
            if freq[d]==0:
                continue
            for m in range(d,mx+1,d):
                if freq[m]>0:
                    ans+=freq[m]*d
                    print(ans)
                    freq[m]=0
        return ans 