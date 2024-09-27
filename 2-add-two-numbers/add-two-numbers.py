# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1=""
        s2=""
        t1=l1
        t2=l2
        while(t1):
        
            s1+=str(t1.val)
            t1=t1.next
        
        while(t2):
        
            s2+=str(t2.val)
            t2=t2.next
        
        s3=int(s1[::-1])+int(s2[::-1])
        s3=str(s3)[::-1]
        l3=ListNode(s3[0])
        s3=s3[1:len(s3)]
        t=l3
        
        while(s3):
            l4=ListNode(s3[0])
            s3=s3[1:len(s3)]
            t.next=l4
            t=l4
        return l3