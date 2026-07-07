# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def sub_reverse(group):
            head = group[-1]
            node = head
            for nd in group[:-1][::-1]:
                node.next = nd
                node = node.next
            return head, node

        node = head
        group_idx = 0
        idx = 1
        group = [None]*k
        last = None
        while node:
            group[(idx-1)%k] = node
            idx += 1
            node = node.next

            if (idx-1)%k==0:
                hd, tail = sub_reverse(group)
                if group_idx == 0:
                    head = hd
                else:
                    last.next = hd
                last = tail
                tail.next = node
                group_idx += 1

        return head