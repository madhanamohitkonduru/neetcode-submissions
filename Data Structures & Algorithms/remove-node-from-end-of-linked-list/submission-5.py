# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0

        while curr.next:
            curr = curr.next
            count = count+1
        
        num = count+1-n
        print("num: ",num)

        prev = None
        curr = head
        for i in range(num):
            prev = curr
            curr = curr.next
        print("curr.val: ",curr.val)

        if prev is None and curr.next is None:
            return None
        elif curr.next is None:
            prev.next = None
        elif prev is None:
            head = curr.next
        else:
            prev.next = curr.next
        return head
        