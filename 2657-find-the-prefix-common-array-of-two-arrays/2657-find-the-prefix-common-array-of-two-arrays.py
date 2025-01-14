class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        n=[0]*len(a)
        c=[0]*len(a)
        r=0
        for i in range(len(a)):
            c[a[i]-1]+=1
            c[b[i]-1]+=1
            if a[i]==b[i] :
                r+=1
            else :
                if c[a[i]-1]==2:
                    r+=1
                if c[b[i]-1]==2:
                    r+=1
            n[i]=r
        return n