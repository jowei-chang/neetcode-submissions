# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def mergeList(node, n1, n2):
            if n1.val >= n2.val:
                node.next = n2
                if n2.next is None:
                    n2.next = n1
                    return
                mergeList(n2, n1, n2.next)
            else:
                node.next = n1
                if n1.next is None:
                    n1.next = n2
                    return
                mergeList(n1, n1.next, n2)
        
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if (list1.val >= list2.val):
            if list2.next:
                mergeList(list2, list1, list2.next)
            else:
                list2.next = list1
            return list2
        else:
            if list1.next:
                mergeList(list1, list1.next, list2)
            else:
                list1.next = list2
            return list1