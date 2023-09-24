class Solution:
    def champagneTower(self, p: int, qr: int, qg: int) -> float:
        a=[[0]*i for i in range(1,102)]
        a[0][0]=p
        for r in range(qr+1):
            for c in range(r+1):
                q=(a[r][c]-1.0)/2.0
                if q>0:
                    a[r+1][c]+=q
                    a[r+1][c+1]+=q
        return min(1,a[qr][qg])