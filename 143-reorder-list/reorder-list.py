# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        

        

        s=head
        f=head
        p=s
        while f and f.next!=None:
            p=s
            s=s.next
            if f and f.next!=None:
                f=f.next
            if f and f.next!=None:
                f=f.next
        if p:
            p.next=None
        if f==head:
            return
        head1=f
        t=s
        while t!=f:
            if s==t:
                t=t.next
                s.next=f.next
                f.next=s
            else:
                x=t.next
                t.next=f.next
                f.next=t
                t=x

        s=head
        f=head1
        while s and f:
            x=f.next
            f.next=s.next
            s.next=f
            f=x
            if s.next!=None:
                s=s.next
            if s.next!=None:
                s=s.next
            else:
                break
            
        if f:
            s.next=f
            f.next=None