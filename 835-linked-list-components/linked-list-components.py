# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """
        
        nums=set(nums)
        c=0
        t=head
        while t:
            if t.val in nums and (t.next is None or t.next.val not in nums):
                c+=1
            t=t.next
        return c