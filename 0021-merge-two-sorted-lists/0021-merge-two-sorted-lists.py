# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d=t=ListNode(0)
        while(l1!=None and l2!=None):
            if(l1.val>l2.val):
                t.next=ListNode(l2.val)
                l2=l2.next
            else:
                t.next=ListNode(l1.val)
                l1=l1.next
            t=t.next
        t.next=l1 or l2
        return d.next