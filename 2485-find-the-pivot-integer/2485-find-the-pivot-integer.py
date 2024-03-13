class Solution:
    def pivotInteger(self, n: int) -> int:
        s=(n*(n+1))//2
        t=0
        for i in range(1,n+1):
            t+=i
            if s-t+i==t:
                return i
        return -1