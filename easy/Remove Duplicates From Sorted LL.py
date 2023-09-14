class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        
        curr = head

        while curr != None:

            if curr.next == None:
                break
            elif curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head