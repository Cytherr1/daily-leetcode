# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
class Solution:
	def deleteMiddle(self, head: ListNode) -> ListNode:
		"""
		My solution also work but it is not practical.

		def findLen(head, l = 0):
            l = l
            if head:
                return findLen(head.next, l + 1)
            else:
                return l

        l = findLen(head)

        removeIndex = (l // 2) + 1

        def seekAndDestroy(head, currIndex = 1):
            if currIndex == removeIndex - 1:
                if head.next and head.next.next:
                    head.next = head.next.next
                else:
                    head.next = None
            else:
                seekAndDestroy(head.next, currIndex + 1)
        
        if l == 1:
            return None
        else:
            seekAndDestroy(head)
            return head
		"""

		if head == None : return None

		prev = ListNode(0)
		prev.next = head
		slow = prev
		fast = head

		while fast != None and fast.next != None:
			slow = slow.next
			fast = fast.next.next
		
		slow.next = slow.next.next

		return prev.next