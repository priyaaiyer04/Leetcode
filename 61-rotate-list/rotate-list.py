# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        c=0
        l=[]
        t=head
        while(t):
            l.append(t.val)
            t=t.next
        if len(l)==0:
            return None
        if len(l)==1:
            return head
        k=k%len(l)
        while c<k:
            c1=ListNode()
            t=head   
            while(t.next):
                c1=t
                t=t.next
            #print(t.val)
            t1=ListNode()
            t1.val=t.val
            t1.next=head
            head=t1
            c1.next=None
            c+=1
        return head
