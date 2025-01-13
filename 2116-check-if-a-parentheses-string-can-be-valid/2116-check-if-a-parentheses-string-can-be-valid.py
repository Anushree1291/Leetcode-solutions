class Solution:
    def canBeValid(self, s: str, l: str) -> bool:
        if len(s)%2!=0:
            return False
        if ( l[0]==1 and s[0]==")" ) or ( l[-1]==1 and s[-1]=="("):
            return False

        a=[]
        for i in range(len(s)):
            if l[i]==0:
                a.append(i)
            