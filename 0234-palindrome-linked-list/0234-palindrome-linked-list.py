# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=f=head
        r=None
        while f and f.next:
            f=f.next.next
            r,r.next,s=s,r,s.next
        if f:
            s=s.next
        while r and r.val==s.val:
            s=s.next
            r=r.next
        return not r