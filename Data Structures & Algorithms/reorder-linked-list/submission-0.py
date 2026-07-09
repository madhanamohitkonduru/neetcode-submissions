# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next=None
        revSecond = self.reverseList(second)
        self.mergetwo(head, revSecond)

        

    def reverseList(self, head: Optional[ListNode]):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

    def mergetwo(self, first: Optional[ListNode], second: Optional[ListNode]):
        while second:
            ftemp,stemp = first.next, second.next
            first.next = second
            second.next = ftemp
            first, second = ftemp, stemp
