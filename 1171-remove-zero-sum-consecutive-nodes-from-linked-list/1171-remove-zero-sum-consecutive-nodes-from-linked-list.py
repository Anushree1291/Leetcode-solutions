# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        m={}
        m[0]=dummy
        p=0
        while head!=None:
            p+=head.val
            m[p]=head
            head=head.next
            
        #print(m)
        head=dummy
        a=dummy
        p=0
        while head!=None:
            p+=head.val
            head.next=m[p].next
            head=head.next
        
        return a.next