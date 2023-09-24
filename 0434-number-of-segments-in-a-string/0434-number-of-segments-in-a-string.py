class Solution:
    def countSegments(self, s: str) -> int:
        a=s.split(" ")
        c=0
        for  i in a:
            if len(i)>0:
                c+=1
        return c