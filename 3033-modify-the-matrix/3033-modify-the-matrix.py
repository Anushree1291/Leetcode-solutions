class Solution:
    def modifiedMatrix(self, ma: List[List[int]]) -> List[List[int]]:
        m=len(ma)
        n=len(ma[0])
        answer=ma.copy()
        for i in range(n):
            maa=max(ma[j][i] for j in range(m))
            for j in range(m):
                if answer[j][i]==-1:
                    answer[j][i]=maa
        return answer