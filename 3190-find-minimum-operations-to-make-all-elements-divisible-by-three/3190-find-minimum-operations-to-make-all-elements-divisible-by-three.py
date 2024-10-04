class Solution:
    def minimumOperations(self, n: List[int]) -> int:
        c=Counter([i%3 for i in n])
        return c[2] + c[1]