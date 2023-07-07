class Solution:
    def minimumRecolors(self, s: str, k: int) -> int:
        c=0
        for i in range(k):
            if(s[i]=='W'):
                c+=1

        m=c

        i=k
        j=0
        while(i<len(s)):
            if(s[i]=='W'):
                c+=1
            if(s[j]=='W'):
                c-=1
            i+=1
            j+=1
            m=min(m,c)
        return m