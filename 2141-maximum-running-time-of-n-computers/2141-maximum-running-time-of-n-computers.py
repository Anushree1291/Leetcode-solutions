class Solution:
    def maxRunTime(self, n: int, b: List[int]) -> int:
        b.sort()
        extra=sum(b[:-n])
        live=b[-n:]
        
        for i in range(n-1):
            
            if extra//(i+1) < live[i+1]-live[i]:
                return live[i]+extra//(i+1)
            
            extra-=(i+1)*(live[i+1]-live[i])
            
        return live[-1]+extra//n

        