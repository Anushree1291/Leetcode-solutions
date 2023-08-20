class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        l=[]
        s=0
        i=0
        j=1
        while i < n:
            if k-j in l:
                l.append(k-j)
            else:
                s+=j
                l.append(j)
                i+=1
            j+=1
        
        return s