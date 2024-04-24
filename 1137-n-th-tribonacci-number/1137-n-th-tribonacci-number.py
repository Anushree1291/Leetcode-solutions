class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0: return 0
        if n<=2:
            return 1
        if n==3: return 2
        a,b,c,d=0,1,1,0
        for i in range(2,n):
            d=a+b+c
            a=b
            b=c
            c=d
        return d