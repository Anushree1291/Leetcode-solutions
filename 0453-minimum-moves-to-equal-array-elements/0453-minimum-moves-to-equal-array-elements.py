class Solution:
    def minMoves(self, n: List[int]) -> int:
        return sum(n) - len(n)*min(n)