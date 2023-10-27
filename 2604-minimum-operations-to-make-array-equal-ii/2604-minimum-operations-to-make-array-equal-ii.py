class Solution:
    def minOperations(self, n1: List[int], n2: List[int], k: int) -> int:
        if k==0:
            for i in range(len(n1)):
                if n1[i] != n2[i]:
                    return -1
            return 0
        s=0
        a=0
        for i in range(len(n1)):
            if n1[i]!=n2[i]:
                d=n1[i]-n2[i]
                if d%k!=0:
                    return -1
                else:
                    a+=-d if d<0 else 0
                    s+=d if d>0 else 0
        return -1 if s!=a else s//k