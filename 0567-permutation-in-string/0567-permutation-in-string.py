class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        def chec(a,b):
            for i in a.keys():
                if i not in b or a[i]!=b[i]:
                    return False
            return True
        
        m={}
        for i in s1:
            if i not in m:
                m[i]=0
            m[i]+=1
        
        n={}
        for i in range(len(s1)):
            if s2[i] not in n:
                n[s2[i]]=0
            n[s2[i]]+=1
        
        if chec(m,n):
            return True
        for i in range(len(s1),len(s2)):
            if s2[i] not in n:
                n[s2[i]]=0
            n[s2[i]]+=1
            n[s2[i-len(s1)]]-=1
            if chec(m,n):
                return True
            

        return False