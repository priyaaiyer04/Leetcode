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
        if head.next==None:
            return head
        if head==None:
            return head
        s=head
        f=head
        while f:
            s=s.next
            if f.next and f.next.next:
                f=f.next.next
            else:
                break
        l2=ListNode(s.val)
        t=s
        t2=l2
        while t.next:
            t=t.next
            t1=ListNode(t.val)
            t2.next=t1
            t2=t1
        t=head
        t1=t
        while t!=s:
            t1=t
            t=t.next
        t1.next=None
        t=head
        def rev(head):
            tail=head
            if head is None:
                return head
            if head.next is None:
                return head
            while tail.next:
                tail=tail.next
        
            if head.next is tail:
                head.next=None
                tail.next=head
                head=tail
                return head
            else:
                while head!=tail:
                    if tail.next:
                        t=head
                        head=head.next
                        t.next=tail.next
                        tail.next=t
                    else:
                        t=head
                        tail.next=head
                        head=head.next
                        t.next=None
                return head
    
        l2=rev(l2)
        t=head
        t1=l2
        while t1 and t:
            print(t.val,t1.val)
            if t.next:
                if t1.next:
                    x=t1.next
                else:
                    x=None
                t1.next=t.next
                
                t.next=t1
                t1=x
                if t.next.next:
                    t=t.next.next
            
            else:
                t.next=t1
                t=t.next
                t1=t1.next
        return head