class Solution:
    def countPairs(self, n: List[int], k: int) -> int:
        c=0
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                if n[i]==n[j] and i*j/k %1 ==0:
                    c+=1
        return c