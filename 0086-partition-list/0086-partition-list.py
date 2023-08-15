# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a=head
        b=head
        q=[]
        while a!=None:
            if a.val<x:
                b.val=a.val
                b=b.next
            else:
                q.append(a.val)
            a=a.next
        
        while b!=None:
            b.val=q.pop(0)
            b=b.next
        
        return head