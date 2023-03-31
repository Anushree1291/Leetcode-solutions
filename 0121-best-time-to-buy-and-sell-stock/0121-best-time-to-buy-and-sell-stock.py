class Solution:
    def maxProfit(self, pr: List[int]) -> int:
        m=pr[0]
        p=0
        for i in pr:
            m=min(i,m)
            p=max(p,i-m)
        return p