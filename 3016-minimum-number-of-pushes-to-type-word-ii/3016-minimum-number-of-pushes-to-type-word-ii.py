class Solution:
    def minimumPushes(self, w: str) -> int:
        m={}
        for i in w:
            if i not in m:
                m[i]=0
            m[i]+=1
        m=sorted(m.items(),key= lambda i:i[1],reverse=True)
        s=0
        for i,k in enumerate(m):
            if i<8:
                s+=k[1]
            elif i<16:
                s+=k[1]*2
            elif i<24:
                s+=k[1]*3
            else:
                s+=k[1]*4
        return s