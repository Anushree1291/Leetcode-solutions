class Solution:
    def waysToSplitArray(self, n: List[int]) -> int:
        for i in range(1,len(n)):
            n[i]+=n[i-1]
        c=0
        for i in range(len(n)-1):
            if n[i]>=n[-1]-n[i]:
                c+=1
        return c