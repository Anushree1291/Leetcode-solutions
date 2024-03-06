class Solution:
    def smallestValue(self, n: int) -> int:
        def fn(n):
            s=0
            while n%2==0:
                s+=2
                n=n//2
            for i in range(3,int(math.sqrt(n))+1,2):
                while n % i== 0:
                    s+=i
                    n = n // i
            return s+(n if n>1 else 0)
        
        while n!=(n:=fn(n)):
            continue
        return n
