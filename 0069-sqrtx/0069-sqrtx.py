class Solution:
    def mySqrt(self, x: int) -> int:
        l=1
        h=x
        res=0
        while ( l<=h) :
            m = l+ (h-l)//2
            if ( m*m <= x):
                res = m
                l = m+1
            else:
                h=m-1
        return res