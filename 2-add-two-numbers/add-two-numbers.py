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
        s=""
        s1=""
        while(l1):
            s+=str(l1.val)
            l1=l1.next
        while(l2):
            s1+=str(l2.val)
            l2=l2.next
        x=int(s[::-1])+int(s1[::-1])
        x=str(x)
        x=x[::-1]
        t=ListNode(int(x[0]))
        t1=t
        t2=t
        for i in x[1:len(x)]:
            t=ListNode(int(i))
            t2.next=t
            t2=t
        return t1

           
           