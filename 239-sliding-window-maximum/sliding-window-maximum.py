import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if k == 1:
            return nums
        
        heap = []
        ans = []
        
        # build first window
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        
        ans.append(-heap[0][0])
        
        l = 1
        for r in range(k, len(nums)):
            # push new element
            heapq.heappush(heap, (-nums[r], r))
            
            # remove stale elements
            while heap and heap[0][1] < l:
                heapq.heappop(heap)
            
            # take max
            ans.append(-heap[0][0])
            
            l += 1
        
        return ans