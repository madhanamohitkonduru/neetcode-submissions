# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy = ListNode(-1001, None)
        for i in lists:
            dummy = self.mergeList(dummy, i)
        return dummy.next

    def mergeList(self ,list1, list2):
        dummy = tail = ListNode(0, None)

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail=tail.next
        tail.next = list1 or list2
        return dummy.next
        