# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        t=head
        c=0
        while t!=None:
            t=t.next
            c+=1

        d=c//k
        r=c%k
        t=head
        l=[]
        for i in range(k):
            a=t
            for j in range(d+(i<r)-1):
                if t: t=t.next
            if t:
                t.next,t=None,t.next
            l.append(a)
            
        return l