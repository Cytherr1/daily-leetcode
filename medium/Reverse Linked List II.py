# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        pos = 1
        curr = head
        values = []

        while curr != None:

            if pos == left:
                leftNode = curr
                values.insert(0, leftNode.val)

            elif pos > left and pos < right:
                values.insert(0, curr.val)

            elif pos == right:
                rightNode = curr
                values.insert(0, rightNode.val)
                newCurr = leftNode
                for value in values:
                    newCurr.val = value
                    newCurr = newCurr.next
                break

            pos += 1
            curr = curr.next

        return head