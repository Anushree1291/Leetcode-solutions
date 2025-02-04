class Solution:
    def maxAscendingSum(self, n: List[int]) -> int:
        m=n[0]
        c=n[0]
        for i in range(1,len(n)):
            if n[i]>n[i-1]:
                c+=n[i]
            else:
                c=n[i]
            m=max(m,c)
        return m