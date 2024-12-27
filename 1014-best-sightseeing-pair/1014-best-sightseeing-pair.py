class Solution:
    def maxScoreSightseeingPair(self, v: List[int]) -> int:
        m=0
        ma=[0]*len(v)
        ma[0]=v[0]
        for i in range(1,len(v)):
            curr=v[i]-i
            m=max(m,ma[i-1]+curr)
            curl=v[i]+i
            ma[i]=max(ma[i-1],curl)

        return m
