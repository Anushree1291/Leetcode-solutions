class Solution:
    def findArray(self, p: List[int]) -> List[int]:
        a=[0]*len(p)
        a[0]=p[0]
        for i in range(1,len(a)):
            a[i]=p[i-1]^p[i]
        return a
