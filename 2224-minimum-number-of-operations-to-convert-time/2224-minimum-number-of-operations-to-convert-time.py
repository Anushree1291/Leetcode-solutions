class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        a,c=map(int,current.split(":"))
        b,d=map(int,correct.split(":"))
        ma=a*60+c
        mb=b*60+d
        d=0
        if mb>=ma:
            d=mb-ma
        else:
            d=3600-(ma-mb)
        c=0
        c+=d//60
        d=d%60
        c+=d//15
        d=d%15
        c+=d//5
        d=d%5
        c+=d
        
        return c