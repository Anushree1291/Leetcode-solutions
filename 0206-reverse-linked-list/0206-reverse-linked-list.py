# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        l=None
        while(h!=None):
            a=ListNode(h.val,l)
            h=h.next
            l=a
        return l