class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        m=0
        for i in left:
            m=max(m,i)
        for i in right:
            m=max(m,n-i)
        return m