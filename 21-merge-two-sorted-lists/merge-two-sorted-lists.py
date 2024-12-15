# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        t=list1
        l=[]
        l1=[]
        t3=ListNode()
        t5=t3
        while t:
            l.append(t.val)
            t=t.next
        t1=list2
        while t1:
            l1.append(t1.val)
            t1=t1.next
        l2=l+l1
        l2.sort()
        for i in l2:
            t4=ListNode()
            t4.val=i
            t3.next=t4
            t3=t3.next
        return t5.next