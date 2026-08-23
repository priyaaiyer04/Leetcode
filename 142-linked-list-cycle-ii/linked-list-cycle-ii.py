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
        while fast!=None:
            if slow and slow.next:
                slow=slow.next
            else:
                slow=None
            if fast and fast.next and fast.next.next:
                fast=fast.next.next
            else:
                fast=None
            if slow==fast:
                break
  
        if head==fast:
            return slow
        slow=head
        
        while slow and fast:
            slow=slow.next
            fast=fast.next
            if slow==fast:
                return slow
      

