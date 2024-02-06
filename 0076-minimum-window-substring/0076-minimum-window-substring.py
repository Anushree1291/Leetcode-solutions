from collections import defaultdict 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m=defaultdict(int)
        for i in t:
            m[i]+=1
        i=0
        j=0
        c=len(t)
        d=1000000
        h=0
        while j<len(s):
            if m[s[j]] >0:
                c-=1
            m[s[j]]-=1
            j+=1
            while c==0:
                if j-i<d:
                    h=i
                    d=j-h
                if m[s[i]]==0:
                    c+=1
                m[s[i]]+=1
                i+=1
        return "" if d==1000000 else s[h:h+d]