class Solution:
    def coloredCells(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 5
        return 1+4*(n-1) + int(4*((n-1)*(n-2))/2)