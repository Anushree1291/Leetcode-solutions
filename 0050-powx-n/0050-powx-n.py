class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            x=1.0/x
            n=-1*n
        s=1
        while n>0:
            if n%2==1:
                s*=x
                n-=1
            n=n//2
            x*=x
            #print(n,s)
        return s