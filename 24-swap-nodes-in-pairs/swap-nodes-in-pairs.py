# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i=0
        t=head
        l=[]
        while t:
            l.append(t.val)
            t=t.next
        while i< len(l)-1:
            x=l[i]
            l[i]=l[i+1]
            l[i+1]=x
            i+=2
        t1=ListNode()
        t2=t1
        for  i in l:
            t3=ListNode()
            t3.val=i
            t1.next=t3
            t1=t3
        return t2.next
            