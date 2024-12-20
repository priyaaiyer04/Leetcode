# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l1=[]
        for i in lists:
            j=i
            while j:
                l1.append(j.val)
                j=j.next
        l1.sort()
        t=ListNode()
        z=t
        c=0
        while c<len(l1):
            t1=ListNode()
            t1.val=l1[c]
            t.next=t1
            t=t1
            c+=1
        return z.next