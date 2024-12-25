# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        t=head
        l=[]
        while t:
            l.append(t.val)
            t=t.next
        l1=[]
        for i in l:
            if l1.count(i)==0:
                l1.append(i)
        t=ListNode()
        t1=t
        for i in l1:
            t2=ListNode()
            t2.val=i
            t.next=t2
            t=t2
        return t1.next