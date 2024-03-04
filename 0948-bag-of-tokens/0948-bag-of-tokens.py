class Solution:
    def bagOfTokensScore(self, t: List[int], p: int) -> int:
        t.sort()
        i,j=0,len(t)-1
        c=0
        while i<=j:
            if t[i]<=p:
                c+=1
                p-=t[i]
                i+=1
            elif i<j and c>0:
                p+=t[j]-t[i]
                j-=1
                i+=1
            else:
                return c
        return c