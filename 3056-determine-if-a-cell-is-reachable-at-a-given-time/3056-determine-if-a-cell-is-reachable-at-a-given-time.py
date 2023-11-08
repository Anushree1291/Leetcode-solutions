class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy==fy and t==1:
            return False
        a=abs(sx-fx)
        b=abs(sy-fy)
        m=min(a,b)
        c=a if m==b else b
        print(a,b,m,c)
        return t>=m+(c-m)