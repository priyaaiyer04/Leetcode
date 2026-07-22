# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        t=head
        f=None
        if t:
            f=t.next
        if f:
            head=f
        while t and f:
            t.next=f.next
            f.next=t
            prev=t
            
            t=t.next
            if t:
                f=t.next
                if f:
                    prev.next=f

            
        return head