from collections import defaultdict
class Solution:
    def customSortString(self, o: str, s: str) -> str:
        m=defaultdict(int)
        for i in range(len(o)):
            m[o[i]]=i
        a=[]
        b=[]
        a.append(s[0])
        if s[0] not in m:
            m[s[0]]=len(o)
        for i in range(1,len(s)):
            if s[i] not in m:
                a.append(s[i])
                m[s[i]]=len(o)
            elif m[s[i]]>m[a[-1]]:
                a.append(s[i])
            else:
                while len(a)>0 and m[s[i]]<m[a[-1]]:
                    b.append(a.pop())
                a.append(s[i])
                while b:
                    a.append(b.pop())
        s=""
        while a:
            s=a.pop()+s
        return s