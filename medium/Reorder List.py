# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head) -> None:
        l = 1
        point = 0
        tp, ap = head, ListNode()
        curr = head

        while curr.next is not None:
            l += 1
            curr = curr.next

        mid = (l // 2) + 1
        curr = head

        while curr.next is not None:
            point += 1
            if point == mid:
                ap = curr
                break
            curr = curr.next
        
        while ap.next is not None:
            curr = ap
            while curr.next is not None:
                b4 = curr
                curr = curr.next
            b4.next = None
            curr.next = tp.next
            tp.next = curr
            
            tp = tp.next.next
            