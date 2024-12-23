# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l=[]
        t=head
        while t:
            l.append(t.val)
            t=t.next
        t=ListNode()
        l=l[::-1]
        t1=t
        for i in l:
            t2=ListNode()
            t2.val=i
            t.next=t2
            t=t2
        return t1.next
        