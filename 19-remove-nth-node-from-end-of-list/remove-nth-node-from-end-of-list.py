# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        t=head
        c=0
        while t:
            t=t.next
            c+=1
        if c==1:
            head=None
            return head    
        c=c-n
        t=head
        if c==0:
            head=head.next
            return head
        while c>1:
            t=t.next
            c-=1
        
        if t.next and t.next.next:
            t.next=t.next.next
        elif t.next:
            t.next=None
        
        return head

            