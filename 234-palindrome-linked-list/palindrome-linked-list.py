# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow=head
        fast=head
        if head.next==None:
            return True
        while fast!=None and fast.next!=None:
            x=fast
            if fast and fast.next!=None:
                fast=fast.next
            x=fast
            if fast and fast.next!=None:
                fast=fast.next
            if fast!=x:
                
                slow=slow.next
        slow=slow.next
        t=slow
        
        while t!=fast:
            if t==slow:
                if t:
                    t=t.next
                if slow and fast:
                    slow.next=fast.next
                if fast:
                    fast.next=slow
            else:
                slow=t
                t=t.next
                slow.next=fast.next
                fast.next=slow
        slow=head
        while slow and fast:
            
            if slow.val==fast.val:
                
                slow=slow.next
                fast=fast.next
            else:
                return False
        if fast==None:
            return True