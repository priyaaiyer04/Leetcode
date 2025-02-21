# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        t=head
        l=[]
        while t:
            l.append(t.val)
            t=t.next
        if l==l[::-1]:
            return True
        return False