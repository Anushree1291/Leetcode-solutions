class Solution:
    def maxOperations(self, n: List[int], k: int) -> int:
        n.sort()
        c=0
        l,h=0,len(n)-1
        while(l<h):
            if n[l]+n[h]==k:
                c+=1
                l+=1
                h-=1
            elif n[l]+n[h]<k:
                l+=1
            elif n[l]+n[h]>k:
                h-=1  
        return c