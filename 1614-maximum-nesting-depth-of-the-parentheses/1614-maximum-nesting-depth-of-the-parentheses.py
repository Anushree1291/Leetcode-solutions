class Solution:
    def maxDepth(self, s: str) -> int:
        m,c=0,0
        for i in s:
            c=c+1 if i=="(" else c
            c=c-1 if i==")" else c
            m=max(c,m)
        return m