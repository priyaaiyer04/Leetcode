# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap=[]
        current=None
        head=None
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,lists[i]))
            
        while heap:
            val,node=heapq.heappop(heap)
            if current is None:
                current=node
                head=current
            else:
                current.next=node
                current=node
            if node.next:
                heapq.heappush(heap,(node.next.val, node.next))

        return head

                