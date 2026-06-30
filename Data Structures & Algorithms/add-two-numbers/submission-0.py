# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        node = l1
        factor = 1
        while node:
            num1 = num1+node.val*factor
            node = node.next
            factor *= 10
        
        node = l2
        factor = 1
        while node:
            num2 = num2+node.val*factor
            node = node.next
            factor *= 10

        s = str(num1+num2)[::-1]
        new_head = ListNode(int(s[0]))
        node = new_head
        for ss in s[1:]:
            node.next = ListNode(int(ss))
            node = node.next

        return new_head