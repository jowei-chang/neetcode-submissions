# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None: return None
        N = 0
        node = head
        while node:
            N += 1
            node = node.next
        if N == n: return head.next

        node = head
        for _ in range(N-n-1):
            node = node.next
        node.next = node.next.next

        return head