import heapq
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k==1:
            return nums
        if k==len(nums):
            return [max(nums)]
        heap=[]
        ans=[]
        for i in range(0,k):
            heapq.heappush(heap,(-nums[i],i))
        ans.append(-heap[0][0])
        l=1
        for r in range(k,len(nums)):
            heapq.heappush(heap,(-nums[r],r))
            while heap and heap[0][1]<l :
                heapq.heappop(heap)
            ans.append(-heap[0][0])
            l+=1
        return ans 
