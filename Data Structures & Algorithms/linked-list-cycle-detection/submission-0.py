# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        step1 = head        # 1 step
        step2 = head        # 2 step
        while step2 and step2.next:
            step1 = step1.next
            step2 = step2.next.next
            if step1 == step2:
                return True
        return False
