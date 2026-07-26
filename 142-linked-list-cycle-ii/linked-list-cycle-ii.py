# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head
        fast=head
        while True:
            if slow:
                slow=slow.next
            if fast and fast.next:
                fast=fast.next.next
            if slow==fast:
                break
            if slow==None :
                
                return slow
            if fast==None:
                return fast
        slow=head
        t=fast
        while t!=slow:
            slow=slow.next
            t=t.next
            if t==None or slow==None:
                
                return None
            if t==slow:
                
                return t
        if t==slow:
            
            return t
        return None