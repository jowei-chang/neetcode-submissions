# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        step1 = head
        step2 = head.next
        head_rev = None
        while step2 and step2.next:
            step1 = step1.next
            step2 = step2.next.next
        head_rev = step1.next
        step1.next = None

        # reverse linked node
        node = head_rev
        head_rev = None
        while node:
            head_rev, node, head_rev.next = node, node.next, head_rev

        # combine two part
        node = head
        node2 = head_rev
        while node2:
            tmp = node.next
            tmp2 = node2.next
            node2.next = node.next
            node.next = node2
            node = tmp
            node2 = tmp2