# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        l=[]
        t=head
        while t:
            l.append(t.val)
            t=t.next
        while l.count(val)>0:
            l.remove(val)
        t1=ListNode()
        t3=t1
        for i in l:
            t2=ListNode()
            t2.val=i
            t1.next=t2
            t1=t2
        return t3.next
        