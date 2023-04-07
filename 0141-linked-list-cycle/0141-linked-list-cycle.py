# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=head
        b=head
        c=False
        while(b!=None and b.next!=None ):
            a=a.next
            b=b.next.next
            if(a==b):
                c=True
                break
        return c