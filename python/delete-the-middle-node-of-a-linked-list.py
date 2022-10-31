# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        x = y = head
        while y.next and y.next.next:
            y = y.next.next
            if y.next:
                x = x.next
        y = x.next
        x.next = x.next.next
        return head
