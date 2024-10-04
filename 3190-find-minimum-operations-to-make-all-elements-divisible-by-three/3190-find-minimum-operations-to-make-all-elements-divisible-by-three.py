class Solution:
    def minimumOperations(self, n: List[int]) -> int:
        c=0
        for i in n:
            if i%3!=0:
                c+=1
        return c