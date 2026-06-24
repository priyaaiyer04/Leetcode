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
        fast=head
        slow=head
        while slow and fast:
            if slow:
                slow=slow.next
            if fast and fast.next:
                fast=fast.next.next
            if slow==fast:
                break
        if slow is None or fast is None:
            return 
        mp=fast
        slow=head
        while (slow!=fast):
            slow=slow.next
            if fast:
                fast=fast.next
      
        return slow