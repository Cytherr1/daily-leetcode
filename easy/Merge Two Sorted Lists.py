
import heapq as hq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, head1, head2):

        minHeap = []
        curr1 = head1
        curr2 = head2

        while curr1 != None:
            hq.heappush(minHeap, curr1.val)
            curr1 = curr1.next
            
        while curr2 != None:
            hq.heappush(minHeap, curr2.val)
            curr2 = curr2.next

        if not minHeap:
            return curr1
        else:
            head = ListNode(hq.heappop(minHeap))

        curr = head
        while minHeap:
            newNode = ListNode(hq.heappop(minHeap))
            curr.next = newNode
            curr = curr.next

        return head
