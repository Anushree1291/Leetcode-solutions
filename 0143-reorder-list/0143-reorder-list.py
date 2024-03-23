# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s=f=head
        while f.next and f.next.next:
            s=s.next
            f=f.next.next
        p,c=None,s.next
        while c:
            n=c.next
            c.next=p
            p=c
            c=n
        s.next=None
        
        h1,h2=head,p
        while h2:
            n=h1.next
            h1.next=h2
            h1=h2
            h2=n
        