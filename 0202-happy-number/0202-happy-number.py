class Solution:
    def isHappy(self, n: int) -> bool:
        def sq(n):
            s=0
            while n:
                a=n%10
                s+=a*a
                n=n//10
            return s
        
        a=b=n
        while True:
            a=sq(a)
            b=sq(b)
            b=sq(b)
            if b==1:
                return True
            if a==b:
                return False
        return False
        