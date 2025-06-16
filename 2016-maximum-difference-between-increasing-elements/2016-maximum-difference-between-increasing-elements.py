class Solution:
    def maximumDifference(self, n: List[int]) -> int:
        c=-1
        m= n[0]
        for i in range(1,len(n)):
            if n[i]>m:
                c=max(c,n[i]-m)
            else:
                m=n[i]
        return c