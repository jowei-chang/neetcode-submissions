# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None
        node_dic = {}
        for ii in range(len(lists)):
            if lists[ii]:
                node = lists[ii]
                while node:
                    if node.val in node_dic:
                        node_dic[node.val].append(node)
                    else:
                        node_dic[node.val] = [node]
                    node = node.next
        head_prev = ListNode(-1)
        node = head_prev
        for kk in sorted(node_dic.keys()):
            for nn in node_dic[kk]:
                node.next = nn
                node = node.next
        return head_prev.next