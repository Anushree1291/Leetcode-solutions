class Solution:
    def productExceptSelf(self, n: List[int]) -> List[int]:
        z=0
        p=1
        for i in n:
            if i==0:
                z+=1
            else:
                p*=i
        if(z>1):
            return [0]*len(n)
        if(z==1):
            for i in range(len(n)):
                if n[i]==0:
                    n[i]=p
                else:
                    n[i]=0
        else:
            for i in range(len(n)):
                n[i]=int(p/n[i])
        return n