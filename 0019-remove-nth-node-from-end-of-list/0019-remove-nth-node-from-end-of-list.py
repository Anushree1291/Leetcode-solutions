# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        h=head
        while h:
            h=h.next
            c+=1
        c=c-n
        if c==0:
            return head.next
        h=head
        while c>1:
            c-=1
            h=h.next
        if h.next==None:
            h.next=None
        else:
            h.next=h.next.next
        return head
