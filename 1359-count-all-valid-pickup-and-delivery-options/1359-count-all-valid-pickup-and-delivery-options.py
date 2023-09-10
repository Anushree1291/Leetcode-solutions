class Solution:
    def countOrders(self, n: int) -> int:
        if n==1:
            return 1
        p=3
        s=1
        m=1000000007
        n-=1
        while n!=0:
            n-=1
            c=(p*(p+1))//2
            p+=2
            s=(s*c)%m
        return s