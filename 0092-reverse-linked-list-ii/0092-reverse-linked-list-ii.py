# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        
        i=1
        a=ListNode(val=0,next=head)
        prev=a
        while i<left:
            prev=prev.next
            i+=1
        
        cur=prev.next
        fut=cur.next
        
        while i<right:
            i+=1
            temp=fut.next
            fut.next=cur
            cur=fut
            fut=temp
            
        
        prev.next.next=fut
        prev.next=cur
            
        return a.next