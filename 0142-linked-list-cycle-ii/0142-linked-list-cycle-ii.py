# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, h: Optional[ListNode]) -> Optional[ListNode]:
        if h==None or h.next==None : return None
        
        p,q=h,h
        while q!=None and q.next!=None:
            p=p.next
            q=q.next.next
            if(p==q):
                break
        if (p!=q):
            return None
        q=h
        while q!=None and p!=None and p!=q:
            p=p.next
            q=q.next
        return p